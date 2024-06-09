# NBA Prediction Project

The objective of the project is to create a predictive model that predicts players for the All-NBA Team and All-Rookie Team based on statistical data.

## Results ALL-NBA

| All-NBA Team   | Player 1             | Player 2          | Player 3        | Player 4            | Player 5          |
|----------------|----------------------|-------------------|-----------------|---------------------|-------------------|
| **First Team** | Giannis Antetokounmpo | Luka Doncic    | Jayson Tatum   | Anthony Davis       | Shai Gilgeous-Alexander |
| **Second Team**| Anthony Edwards      | Kevin Durant     | LeBron James    | Nikola Jokic        | Paolo Banchero    |
| **Third Team** | Jalen Brunson        | De'Aaron Fox     | DeMar DeRozan  | Domantas Sabonis    | Devin Booker      |

## Results ALL-Rookie

| Rookie All-Rookie Team        | Player 1           | Player 2          | Player 3             | Player 4          | Player 5          |
|----------------------------|--------------------|-------------------|----------------------|-------------------|-------------------|
| **First Team**             | Victor Wembanyama | Chet Holmgren     | Brandon Miller       | Keyonte George    | Scoot Henderson   |
| **Second Team**            | Jaime Jaquez Jr.  | Amen Thompson     | Brandin Podziemski  | Cason Wallace     | Ausar Thompson    |


### Methods Used

- Loading data from a CSV file
- Data preprocessing including handling missing values, standardization, and feature selection
- Modeling using Random Forest Classifier for player classification
- Evaluation of different models including Random Forest, Support Vector Regressor (SVR), and XGBoost

### Files Overview

- `all_nba.ipynb`: Jupyter Notebook containing the data analysis process including data loading, preprocessing, modeling, and evaluation.

### Plot and Statistics Descriptions:

1. **Number of All-NBA Nominations for Top 20 Players:**
   - Displays the number of All-NBA nominations for the top 20 players with the highest number of nominations.
     [](https://github.com/dariak153/Prediction_Awards/blob/main/20_players.png)
     
2. **Feature Correlation Matrix:**
   - Illustrates how various features correlate with each other, aiding in feature selection and understanding feature relationships.
     [](https://github.com/dariak153/Prediction_Awards/blob/main/correlation.png)

3. **Features Most Correlated with All-NBA Nomination:**
   - Presents the features (player statistics) most correlated with All-NBA nomination, helping identify key predictors.

4. **Average Age of All-NBA Nominated Players in Each Season:**
   - Shows the average age of players nominated for All-NBA in each season, indicating if age influences nomination chances.
      [](https://github.com/dariak153/Prediction_Awards/blob/main/nba_age.png)

5. **Teams with the Most Players in All-NBA:**
   - Displays teams with the highest number of players nominated for All-NBA, highlighting teams with significant impact.

6. **Teams with the Most Players in All-NBA in Each Season:**
   - Shows teams with the highest number of players nominated for All-NBA in each season, indicating changes in dominant teams over time.


## 2. Implementation
### [check files exist ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L31-L37)

- A function check_files_exist checks if the required files are present in the specified directory. It returns a list of missing files if any.

### [load data ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L39-L43)

- The load_data function reads the necessary CSV files into pandas DataFrames for further processing.

### [preprocess_data ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L45-L56)

- The preprocess_data function prepares the player statistics data by performing the following steps:
  
 * Dropping Unnecessary Columns: Columns that are not needed for analysis are removed.
 * Converting Data Types: The "GP" (games played) column is converted to integers to ensure proper numerical operations.
 * Filtering Players: Only players who played more than 40 games in a season are retained.
 * Filtering Seasons: The data is filtered to include only the specified seasons.
 * Adding All-NBA Nominations: A new column "ALL_NBA_NOMINATION" is added to indicate whether a player received an All-NBA nomination. This column is initially set to 0 for all players.
   
### [features and target variables](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L58-L64)
* The target variable, "ALL_NBA_NOMINATION", is separated from the features.
* Columns that are not needed for the model are removed from the features DataFrame.
* The "DRAFT_YEAR" and "DRAFT_NUMBER" columns are converted to integer type, with undrafted players assigned a value of -1.
* Categorical data in the "TEAM_ABBREVIATION" column is converted to dummy variables.

 ### [ standardize function ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L66-L72)
  
 - The standardize_features function standardizes the features using a StandardScaler. This ensures that all features have a mean of 0 and a standard deviation of 1.
   
  ### [train random forest ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L74-L83)
  
- The train_random_forest function trains a Random Forest model. The dataset is split into training and testing sets, the model is trained on the training set, and predictions are made on the testing set.
  
 ### [predict for a new season ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L85-L98)
  
- The predict_new_season function uses the trained Random Forest model to predict All-NBA nominations for a new season. It preprocesses the new season's data similarly to the training data, standardizes it, and makes predictions.
  
 ### [generate award predictions ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L100-L116)
 
- The generate_award_predictions function assigns predicted players to different All-NBA teams based on their predicted probabilities.
  
 ### [save results and model ](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L118-L124)
 
- The save_results function saves the predicted results to a JSON file.
- The save_model function saves the trained model and the scaler to a file using pickle.
  
### [main execution](https://github.com/dariak153/Prediction_Awards/blob/1938cd594d48ab4ff5ed1781081064ec27659b36/src/main.py#L126-L143)

- The main checks for missing files, loads the data, preprocesses it, trains the model, makes predictions, and saves the results.
