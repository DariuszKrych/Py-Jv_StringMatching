import pandas as pd
import ast
import time
import os


def raw_review_dataframe_to_split(print_docstrings):
    """-----
raw_review_dataframe_to_split:
Info - Splits the main database.csv of ~6.4 million rows into smaller csv files which are up to a few dozen thousand rows at most.
Uses a reference dictionary to make parsing through the rows of data a few times faster than an earlier versions brute force filtering method.
The reference dictionary keys are a given game_id num and a respective list value with two nums, the first and last rows in which reviews
for the given game_id exist in the dataset.csv. This allows all rows to be skipped until the first row which reviews appear then for game_id,
the next end_row-start_row+1 count rows of reviews are saved and then the filtered results are saved.
Details - The database is filtered into smaller csv files with reviews only for a specific game instead of for all games
to ensure that algorithms take a reasonable amount of time to execute as if the database.csv was passed through them instead
of a smaller csv split off of it would take an unreasonable amount of time to execute.
-----
"""
    if print_docstrings:
        print(raw_review_dataframe_to_split.__doc__)

    if not os.path.exists('..\Put_Dataset_Here\dataset.csv'):
        print("The required dataset.csv is missing from the Put_Dataset_Here folder."
              "\nPlease reference \'Step 4: (EXTRA - for additional functionality)\' in the readme.md file.")
    elif not os.path.exists('..\Put_Dataset_Here\App_ID_Row_Reference.txt'):
        print("The required App_ID_Row_Reference.txt is missing from the Put_Dataset_Here folder."
              "\nPlease run the second option from the main menu to re-create this required reference dictionary file.")
    else:
        print("Extracting review data for specific games from 2017 steam dataset.")
        game_id = input("Please enter the game_id as an integer (Can be found as App ID on sites like steamdb.info):")

        # Getting the specific rows for given app_id from reference dictionary stored as a txt.
        # Open the file and read the contents
        with open('..\Put_Dataset_Here\App_ID_Row_Reference.txt', 'r') as file:
            data = file.read()
        # Converts the string representation of the dictionary into an actual dictionary
        app_id_ranges = ast.literal_eval(data)
        # Check if the user inputted id is valid.
        while True:
            if str(game_id) in app_id_ranges:
                break
            else:
                game_id = input("Please re-enter the game_id,ensure it is for a game available on steam in 2017 as "
                                "only those are included in the dataset.")

        # Get name for csv review file and ensure there are no spaces in it.
        game_name = input("Please enter the game name in format name_xyz without spaces: ")
        while True:
            if ' ' in game_name:
                game_name = input("Please enter the game name in format name_xyz without spaces: ")
            else:
                break

        initial_time = time.time()

        # Takes the relevant start/end row numbers from the given key based on the earlier user inputted game_id.
        # The whole thought behind this is to skip all rows other than the ones for the given game_id, making you
        # look through a few thousand lines instead of 6.4 million and change for the whole database.
        # The dictionary can also be used for input validation for the game_id as seen above.
        start_row, end_row = app_id_ranges[str(game_id)]

        # Skipping all rows until the first row with review data and then reading only the rows in which the desired review data is located.
        # Reading only data from the review text column ignoring all other columns as their data is not necessary.
        filtered_reviews = pd.read_csv('../Put_Dataset_Here/dataset.csv', usecols=['review_text'], skiprows=list(range(1, int(start_row)-1)), nrows = end_row-start_row+1)
        # Saving the data read as a csv.
        filtered_reviews.to_csv("../Separate_Game_Reviews/" + str(game_name) + "_reviews.csv", index=False)

        end_time = time.time();  time_spent = end_time - initial_time

        print(f"Filtering reviews for {game_name} took {round(time_spent, 3)} seconds."
              f"\nSaved {end_row - start_row + 1} reviews to {str(game_name) + '_reviews.csv'}.")
