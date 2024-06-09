from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playerawards
from nba_api.stats.endpoints import boxscoreadvancedv2
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import leagueleaders
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBClassifier
from sklearn.svm import SVR
from sklearn.preprocessing import LabelEncoder
from itertools import product
from bs4 import BeautifulSoup
from lxml import html
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import time
import json
import requests
import json
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.join(ROOT_DIR, '..', 'data')
REQUIRED_FILES = ['player_stats.csv', 'all_nba_nominations.csv', 'player-stats-2023-24.csv']

def check_files_exist(workdir, files):
    missing_files = []
    for file in files:
        file_path = os.path.join(workdir, file)
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    return missing_files

def load_data(workdir):
    players_stats = pd.read_csv(os.path.join(workdir, 'player_stats.csv'))
    all_nba_nominations = pd.read_csv(os.path.join(workdir, 'all_nba_nominations.csv'))
    to_predict = pd.read_csv(os.path.join(workdir, 'player-stats-2023-24.csv'))
    return players_stats, all_nba_nominations, to_predict

def preprocess_data(players_stats, all_nba_nominations, seasons):
    players_stats.drop(columns=['Unnamed: 0', 'LEAGUE_ID'], inplace=True)
    players_stats["GP"] = players_stats["GP"].astype(int)
    players_stats = players_stats[players_stats["GP"] > 40]
    players_stats = players_stats[players_stats["SEASON_ID"].isin(seasons)]
    players_stats["ALL_NBA_NOMINATION"] = [0 for _ in range(len(players_stats))]
    for season in all_nba_nominations.columns[1:]:
        for player in all_nba_nominations[season].dropna():
            con1 = players_stats["SEASON_ID"] == season
            con2 = players_stats["DISPLAY_FIRST_LAST"] == player
            players_stats.loc[con1 & con2, 'ALL_NBA_NOMINATION'] = 1
    return players_stats

def prepare_features_and_target(players_stats):
    target = players_stats["ALL_NBA_NOMINATION"]
    features = players_stats.drop(columns=['ALL_NBA_NOMINATION', 'TEAM_ID', 'SEASON_ID', 'PLAYER_ID', 'DISPLAY_FIRST_LAST'])
    features['DRAFT_YEAR'] = features['DRAFT_YEAR'].replace('Undrafted', -1).astype(int)
    features['DRAFT_NUMBER'] = features['DRAFT_NUMBER'].replace('Undrafted', -1).fillna(-1).astype(int)
    features = pd.get_dummies(features, columns=['TEAM_ABBREVIATION'])
    return features, target

def standardize_features(features, scaler=None):
    if not scaler:
        scaler = StandardScaler()
        scaled_array = scaler.fit_transform(features)
    else:
        scaled_array = scaler.transform(features)
    return pd.DataFrame(scaled_array, columns=features.columns), scaler

def train_random_forest(features, target):
    split = int(len(features) * 0.8)
    train_features = features[:split]
    test_features = features[split:]
    train_target = target[:split]
    test_target = target[split:]
    random_forest = RandomForestRegressor(n_estimators=500, random_state=1, max_depth=5, max_features='sqrt', min_samples_leaf=1)
    random_forest.fit(train_features, train_target)
    predictions = random_forest.predict(test_features)
    return random_forest, train_features, test_features, train_target, test_target, predictions

def predict_new_season(random_forest, to_predict, train_features_columns, scaler):
    features = to_predict.drop(columns=['Unnamed: 0', 'LEAGUE_ID', 'TEAM_ID', 'SEASON_ID', 'PLAYER_ID', 'DISPLAY_FIRST_LAST'])
    features['DRAFT_YEAR'] = features['DRAFT_YEAR'].replace('Undrafted', -1).astype(int)
    features['DRAFT_NUMBER'] = features['DRAFT_NUMBER'].replace('Undrafted', -1).fillna(-1).astype(int)
    features = pd.get_dummies(features, columns=['TEAM_ABBREVIATION'])
    missing_columns = set(train_features_columns) - set(features.columns)
    for col in missing_columns:
        features[col] = 0
    features = features[train_features_columns]
    features, _ = standardize_features(features, scaler)
    final_predictions = random_forest.predict(features)
    to_predict["PREDICTIONS"] = final_predictions
    result = to_predict.sort_values(by="PREDICTIONS", ascending=False)
    return result

def generate_award_predictions(result, not_rookies):
    award_names = ("first all-nba team", "second all-nba team", "third all-nba team", "first rookie all-nba team", "second rookie all-nba team")
    result_json = {award: [] for award in award_names}
    results_probs = list(result["DISPLAY_FIRST_LAST"])
    i = 0
    players_count = 0
    while players_count < 25:
        if players_count < 15:
            award = award_names[players_count // 5]
        else:
            award = award_names[3 + (players_count - 15) // 5]
            while results_probs[i] in not_rookies:
                i += 1
        result_json[award].append(results_probs[i])
        players_count += 1
        i += 1
    return result_json

def save_results(result_json, filename):
    with open(filename, 'w') as file:
        json.dump(result_json, file, indent=4)

def save_model(model, scaler, filename):
    with open(filename, 'wb') as file:
        pickle.dump({'model': model, 'scaler': scaler}, file)

if __name__ == "__main__":
    missing_files = check_files_exist(WORKDIR, REQUIRED_FILES)
    if missing_files:
        print("The following required files are missing:")
        for file in missing_files:
            print(file)
    else:
        players_stats, all_nba_nominations, to_predict = load_data(WORKDIR)
        seasons = ['1988-89', '1989-90', '1990-91', '1991-92', '1992-93', '1993-94', '1994-95', '1995-96', '1996-97', '1997-98', '1998-99', '1999-00', '2000-01', '2001-02', '2002-03', '2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23']
        players_stats = preprocess_data(players_stats, all_nba_nominations, seasons)
        features, target = prepare_features_and_target(players_stats)
        features, scaler = standardize_features(features)
        random_forest, train_features, test_features, train_target, test_target, predictions = train_random_forest(features, target)
        not_rookies = list(players_stats['DISPLAY_FIRST_LAST'].unique())
        result = predict_new_season(random_forest, to_predict, train_features.columns, scaler)
        result_json = generate_award_predictions(result, not_rookies)
        save_results(result_json, os.path.join(ROOT_DIR, "Daria_Kubacka.json"))
        save_model(random_forest, scaler, os.path.join(ROOT_DIR, "random_forest_model.pkl"))
