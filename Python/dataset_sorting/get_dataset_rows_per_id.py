import pandas as pd
import json
import os


def create_row_id_num_reference(print_docstrings):
    """-----
create_row_id_num_reference:
Info - Set chunks parsed as 1 to load one row at once. Loop through the dataset csv file one chunk at a time.
Go through all rows and when the app_id (i.e. game_id) changes save the last row the given app_id appears.
Then save the next row as the first row of the next app_id. Repeat the above until all rows are parsed.
Save the created dictionary of app_id: [first_row_appeared, last_row_appeared] of all app_id in the dataset.csv file.
Details - Creates a reference dictionary which is needed for the execution of the csv splitting function.
To ensure that correct values were saved for the first and last rows of a given game_id saved csvs were compared manually.
-----
"""
    if print_docstrings:
        print(create_row_id_num_reference.__doc__)

    # Set chunks parsed as 1 to load one row at once.
    row_first_n_last = [];  row_num = 1;  ref_table = {};  previous_id = 1


    # Loop through the CSV file one chunk at a time.
    if os.path.exists('..\Put_Dataset_Here\dataset.csv'):
        for chunk_data in pd.read_csv('..\Put_Dataset_Here\dataset.csv', chunksize=100000, usecols=['app_id']):
            current_ids = chunk_data['app_id']  # Extract the single app_id value from the Series

            for current_id in current_ids:
                # Append the filtered rows to the DataFrame where the app_id column matches the inputted game_id.
                if previous_id != current_id:
                    # Get last row number for old specific app_id.
                    row_first_n_last.append(row_num)
                    # Save both start and end num for specific app_id.
                    ref_table[previous_id] = row_first_n_last
                    # Get first row number for new specific app_id.
                    row_first_n_last = [row_num+1]
                previous_id = current_id
                # Print parsing progress.
                row_num += 1

                # Check if the current ID is NaN and break the loop
                if pd.isna(current_id):
                    break

            print(f"{row_num / 6500000:.2%}")

        # There is no steam app with an app id of 1 so removing this is fine as it's the first id from the loop getting started.
        del(ref_table[1])
        # To save values for the last app_id key.
        row_first_n_last.append(row_num)
        ref_table[previous_id] = row_first_n_last
        print(ref_table)

        with open('..\Put_Dataset_Here\App_ID_Row_Reference.txt', 'w') as file:
            json.dump(ref_table, file)

        print("Saved App_ID_Row_Reference.txt")
    else:
        print("The required dataset.csv is missing from the Put_Dataset_Here folder."
         "\nPlease reference \'Step 4: (EXTRA - for additional functionality)\' in the readme.md file.")