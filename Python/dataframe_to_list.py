import csv
import os
import glob


def get_review_string_list(print_docstrings):
    """-----
get_review_string_list:
Gets the text as a list of strings from stored csv files by appending each row as a string to a list.
-----
"""
    if print_docstrings:
        print(get_review_string_list.__doc__)


    # Initialise lists & int.
    review_strings_list = [];  csv_file_names = [];  csv_nums = [];  n = 0

    # Get all file paths for .csv files from 'Separate_Game_Reviews' directory.
    csv_files_dir = glob.glob('../Separate_Game_Reviews/*.csv')
    # Format each directory in list into numbered csv file names.
    for csv_path in csv_files_dir:
        csv_file_names.append(csv_path[25:])

    print(f'The current review files include:')
    # Print numbered csv files names. Then re-format list to remove 'n: ' leaving only file names.
    for csv_file in csv_file_names:
        print(f"{n}: {csv_file}");  csv_nums.append(str(n));  n = n + 1


    # Ask user to choose a review file based on position number in list.
    review_file_num = input('\nPlease choose a review file by entering its respective number.\n')
    # Check if user input is valid.
    usr_input_invalid = True
    while usr_input_invalid:
        if review_file_num in csv_nums:
            usr_input_invalid = False
        else:
            review_file_num = input("Please enter a valid num:")
    # Stores path to review file in csv_path.
    chosen_review_file_name = csv_file_names[int(review_file_num)]
    csv_path = os.path.join("../Separate_Game_Reviews", chosen_review_file_name)

    # Opens file at path in 'r' (read mode) with an encoding which takes into
    # account any possible characters from the real world review strings.
    with open(csv_path, 'r',encoding='utf-8',) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Append strings currently being read as the list.
            review_strings_list.append(row['review_text'])

    total_review_chars = 0
    for string in review_strings_list:
        total_review_chars = total_review_chars + len(str(string))
    print(f"Review data chosen as text for pattern matching includes: {len(review_strings_list):,} review strings with {total_review_chars:,} characters.\n")

    # print(review_strings_list)
    return review_strings_list