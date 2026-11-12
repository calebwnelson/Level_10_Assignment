# Author: Caleb Nelson
# Program to help people explore college football results from a CSV file.

import pandas as pd
from pathlib import Path

football_data = pd.read_csv(
    Path(__file__).resolve().parent / "cfb.csv"
)

# Find the earliest and latest seasons in the CSV
first_season = int(football_data["Season"].min())
last_season = int(football_data["Season"].max())

# Loop to allow the user to select a season to analyze. The loop will continue until the user enters 'x' or 'X' to quit.
while True:
    current_season = input(
        f"Enter a season to analyze ({first_season}-{last_season}) or 'x' to quit: "
    )

    # If the user enters 'x' or 'X', break the loop and end the program
    if current_season.lower() == "x":
        break

    # Check if the user entered a valid season. If not, let them know and continue the loop
    if not current_season.isdigit():
        print(f"Please enter a valid year between {first_season} and {last_season}.")
        continue

    # Convert the user input to an integer and check if it is within the range of seasons in the CSV. If not, let them know and continue the loop
    current_season = int(current_season)

    # Check if the user entered a season that is within the range of seasons in the CSV. If not, let them know and continue the loop
    if current_season < first_season or current_season > last_season:
        print(f"Please enter a year between {first_season} and {last_season}.")
        continue

    # Create an empty dataframe with the same columns as the main one
    season_data = pd.DataFrame(columns = football_data.columns)

    # Loop through the main dataframe and add rows to the new one if they match the current season
    for index,row in football_data.iterrows():
        if row["Season"] == int(current_season):
            season_data.loc[len(season_data)] = row

    # Check if the new dataframe is empty, if it is, let the user know that the season was not found
    if season_data.empty:
        print("Season not found. Please try again.")
        continue
    # Create a dictionary to hold the teams and their win categories
    team_dictionary = {
    1: [],
    2: [],
    3: [],
    4: []
    }

    # Loop through the new dataframe and add the teams to the appropriate category in the dictionary
    for index, row in season_data.iterrows():
        if int(row["Win"]) < 6:
            category = 1
        elif int(row["Win"]) <= 7:
            category = 2
        elif int(row["Win"]) <= 9:
            category = 3
        else:
            category = 4

        team_dictionary[category].append(row["Team"])

    # Print the results to the user
    print()
    print("Here are the results for " + str(current_season) + ":")
    print("-------------------------")
    # Create a list of the win categories to use in the loop
    win_categories = ["Fewer than 6", "6-7", "8-9", "10 or more"]
    # Loop through the dictionary in reverse order to print the categories from highest to lowest
    for i in range(3, -1, -1):
        print(win_categories[i] + " wins:")
        print()
        # Loop through the teams in the current category and print them
        for team in team_dictionary[i + 1]:
            print(team)
        print("-------------------------")