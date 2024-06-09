# NBA Prediction Project

## Cel projektu
Celem projektu jest stworzenie modelu predykcyjnego, który wytypuje zawodników do All-NBA Team oraz All-Rookie Team na podstawie danych statystycznych z pliku `NBA_Seasons_Dates.csv`.

## Użyte metody
- Ładowanie danych z pliku CSV.
- Przetwarzanie danych: usunięcie brakujących wartości, standaryzacja, wybór cech.
- Modelowanie: Random Forest Classifier do klasyfikacji zawodników.

## Preprocessing
- Usunięcie brakujących wartości.
- Standaryzacja cech numerycznych.
- Wybór najważniejszych cech: punkty, zbiórki, asysty, przechwyty, bloki (dostosuj do rzeczywistych cech w danych).

## Uruchomienie
1. Ładowanie danych:
   ```bash
   python src/data_loader.py
