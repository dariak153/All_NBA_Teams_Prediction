# NBA Prediction Project

The objective of the project is to create a predictive model that predicts players for the All-NBA Team and All-Rookie Team based on statistical data from the file `NBA_Seasons_Dates.csv`.

## Results 

| All-NBA Team   | Player 1             | Player 2          | Player 3        | Player 4            | Player 5          |
|----------------|----------------------|-------------------|-----------------|---------------------|-------------------|
| **First Team** | Giannis Antetokounmpo | Luka Doncic    | Jayson Tatum   | Anthony Davis       | Shai Gilgeous-Alexander |
| **Second Team**| Anthony Edwards      | Kevin Durant     | LeBron James    | Nikola Jokic        | Paolo Banchero    |
| **Third Team** | Jalen Brunson        | De'Aaron Fox     | DeMar DeRozan  | Domantas Sabonis    | Devin Booker      |

| Rookie All-NBA Team        | Player 1           | Player 2          | Player 3             | Player 4          | Player 5          |
|----------------------------|--------------------|-------------------|----------------------|-------------------|-------------------|
| **First Team**             | Victor Wembanyama | Chet Holmgren     | Brandon Miller       | Keyonte George    | Scoot Henderson   |
| **Second Team**            | Jaime Jaquez Jr.  | Amen Thompson     | Brandin Podziemski  | Cason Wallace     | Ausar Thompson    |


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
