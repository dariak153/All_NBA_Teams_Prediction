# NBA Prediction Project

The objective of the project is to create a predictive model that predicts players for the All-NBA Team and All-Rookie Team based on statistical data.

## Results ALL-NBA

| All-NBA Team   | Player 1             | Player 2          | Player 3        | Player 4            | Player 5          |
|----------------|----------------------|-------------------|-----------------|---------------------|-------------------|
| **First Team** | Giannis Antetokounmpo | Luka Doncic    | Jayson Tatum   | Anthony Davis       | Shai Gilgeous-Alexander |
| **Second Team**| Anthony Edwards      | Kevin Durant     | LeBron James    | Nikola Jokic        | Paolo Banchero    |
| **Third Team** | Jalen Brunson        | De'Aaron Fox     | DeMar DeRozan  | Domantas Sabonis    | Devin Booker      |

## Results ALL-Rookie

| All-Rookie Team        | Player 1           | Player 2          | Player 3             | Player 4          | Player 5          |
|----------------------------|--------------------|-------------------|----------------------|-------------------|-------------------|
| **First Team**             | Victor Wembanyama | Chet Holmgren     | Brandon Miller       | Keyonte George    | Scoot Henderson   |
| **Second Team**            | Jaime Jaquez Jr.  | Amen Thompson     | Brandin Podziemski  | Cason Wallace     | Ausar Thompson    |


### Files Overview

- `all_nba.ipynb`: Jupyter Notebook containing the data analysis process including data loading, preprocessing, modeling, and evaluation.

### Plot and Statistics Descriptions:

1. **Number of All-NBA Nominations for Top 20 Players:**
   - Displays the number of All-NBA nominations for the top 20 players with the highest number of nominations.
     ![team](https://github.com/dariak153/Prediction_Awards/blob/main/20_players.png)
     
2. **Feature Correlation Matrix:**
   - Illustrates how various features correlate with each other, aiding in feature selection and understanding feature relationships.
     ![matrix](https://github.com/dariak153/Prediction_Awards/blob/main/correlation.png)

3. **Features Most Correlated with All-NBA Nomination:**
   - Presents the features (player statistics) most correlated with All-NBA nomination, helping identify key predictors.

4. **Average Age of All-NBA Nominated Players in Each Season:**
   - Shows the average age of players nominated for All-NBA in each season, indicating if age influences nomination chances.
      ![age](https://github.com/dariak153/Prediction_Awards/blob/main/nba_age.png)

5. **Teams with the Most Players in All-NBA:**
   - Displays teams with the highest number of players nominated for All-NBA, highlighting teams with significant impact.

6. **Teams with the Most Players in All-NBA in Each Season:**
   - Shows teams with the highest number of players nominated for All-NBA in each season, indicating changes in dominant teams over time.
