from dataset_sorting import dataframe_sorting
from dataset_sorting import get_dataset_rows_per_id
import dataframe_to_list
from string_matching import StringMatchingAlgorithms
import time
import tracemalloc


algo_intro = {"3": 'Custom simple native string matching algorithm',
              "4": 'Custom simple native string matching algorithm (pre-processing repeatedly used variables for reference)',
              "5": 'Naive string matching algorithm',
              "6": 'Rabin-karp string matching algorithm (own python hashing implementation used)',
              "7": 'Rabin-karp string matching algorithm (mmh3 library written in C used for hashing)',
              "8": 'Boyer Moore Horspool string matching algorithm. (Bad character rule only.)',
              "9": 'KMP string matching algorithm.',
              "10": 'Run ALL algorithms one after another. (3->9)',
              "11": 'Run ALL algorithms one after another in reverse order. (9->3)'}
all_algo_names = {"3": ['native'], "4": ['native-pre'], "5": ['naive'], "6": ['rabin-karp-py'], "7": ['rabin-karp-lib'],
                  "8": ['boyer-moore-h'],"9": ['kmp'],
                  "10": ['native', 'native-pre', 'naive', 'rabin-karp-py', 'rabin-karp-lib', 'boyer-moore-h', 'kmp'],
                  "11": ['kmp', 'boyer-moore-h', 'rabin-karp-lib', 'rabin-karp-py', 'naive', 'native-pre', 'native']}

def usr_main_menu_chk(usr_input):
    """-----
usr_main_menu_chk:
Checks user input made for the main menu to ensure it is valid. Uses the all_algo_names dictionary to ensure
input is valid so the code works without a hitch when extra algorithm execution options are added.
-----
"""
    if print_docstrings:
        print(usr_main_menu_chk.__doc__)

    usr_input_invalid = True
    while usr_input_invalid:
        if usr_input in all_algo_names or usr_input in ['1', '2']:
            usr_input_invalid = False
        else:
            usr_input = input("Please enter a valid option:")

    return usr_input


def print_info_n_time(algo_data, initial_time, initial_stat):
    """-----
print_info_n_time:
Info - Takes algorithm output data, initial time and memory. Finds time taken for algorithm to execute and memory change since
algorithm execution has taken place. Prints all data.
Details - This is in a separate definition as it can be easily called over again for any given
algorithm execution to print data describing its execution results/statistics. This makes it quicker to change what info is printed for
algorithm execution as it is in one place for all algorithms. Each algorithm returns its algorithm ID and number of matches found.
The algorithm ID is then used by the print_info_n_time function to determine which algorithm introduction message to print from the 'algo_intro' dictionary.
-----
"""
    if print_docstrings:
        print(print_info_n_time.__doc__)


    # End memory tracking for algo and find memory change.
    end_stat = tracemalloc.take_snapshot();  stats = end_stat.compare_to(initial_stat, 'lineno')
    mem_changed = 0
    for stat in stats:
        mem_changed += stat.size_diff
    # Ending time tracking and pulling data out of algo_data list into separate variables.
    end_time = time.time();  time_spent = end_time - initial_time;  algo_id_num = algo_data[0];  matches = algo_data[1]
    print(f"{algo_intro[algo_id_num]}:\nFound {matches} matches for your input in the review strings.\n"
          f"The time spent running was {round(time_spent, 3):.3f} sec.\n"
          f"There was a {mem_changed} byte change in memory while the algorithm ran.\n ")


def call_string_match(algo_names):
    """-----
call_string_match:
Info - Asks the user for a string pattern which can be anything. Calls a function to get the text for string matching.
Loops over an input list from the 'all_algo_names' dictionary. First starting data recording as needed just before algorithm execution begins.
Uses a switch statement to execute the given algorithm in the inputted list based on the 'all_algo_names' dictionary.
When a case is chosen for a given algorithm to execute first the algorithm definition itself is called with teh text string list
along with the input pattern being passed through to it. Then after the algo finishes execution the print_info_n_time function is called.
Then once all entries in the list have been executed for the for loop ends.
Details - The reason each value entry in the 'all_algo_names' dictionary is in a list is to allow it to be run through a loop which in turn
allows each algorithm to be easily called separately along with easily being able to call execution of all algorithms
in any order as is required.
-----
"""
    if print_docstrings:
        print(call_string_match.__doc__)

    input_pattern = str(input("Please enter a string for which to search for matches in the reviews:\n"))
    reviews_text = dataframe_to_list.get_review_string_list(print_docstrings)

    for algo_name in algo_names:
        # Starting time tracking for algo.
        initial_time = time.time()
        # Starting memory tracking for algo.
        tracemalloc.start();  initial_stat = tracemalloc.take_snapshot()
        # initial_mem = sum(stat.size for stat in initial_stat)
        # Switch: runs code specifically for case = match. Faster than a line of if statements.
        match algo_name:
            case 'native':
                print_info_n_time(StringMatchingAlgorithms.native_algo(reviews_text, input_pattern, print_docstrings), initial_time, initial_stat)
            case 'native-pre':
                print_info_n_time(StringMatchingAlgorithms.native_algo_preprocessing(reviews_text, input_pattern, print_docstrings), initial_time, initial_stat)
            case 'naive':
                print_info_n_time(StringMatchingAlgorithms.naive_algo(reviews_text, input_pattern, print_docstrings), initial_time, initial_stat)
            case 'rabin-karp-py':
                print_info_n_time(StringMatchingAlgorithms.rabin_karp_algo_py(reviews_text, input_pattern, print_docstrings), initial_time, initial_stat)
            case 'rabin-karp-lib':
                print_info_n_time(StringMatchingAlgorithms.rabin_karp_algo_lib(reviews_text, input_pattern, print_docstrings), initial_time, initial_stat)
            case 'boyer-moore-h':
                print_info_n_time(StringMatchingAlgorithms.boyer_moore_horspool_algo(reviews_text, input_pattern, print_docstrings), initial_time, initial_stat)
            case 'kmp':
                print_info_n_time(StringMatchingAlgorithms.kmp_algo(reviews_text, input_pattern, print_docstrings), initial_time, initial_stat)


print_docstrings = False
docstrings_input = input("All functions explained through docstrings. (Reasoning behind the code.)\n"
                        "Enabling this option will make it easier to understand what the code is doing.\n"
                         "To change this option the program must be restarted.\n\n"
                         "Would you like to enable docstring printing at the start of every function being called?\nEnter 1 to enable and anything else to disable.\n")
if docstrings_input == '1':
    print_docstrings = True
    print("You have enabled the docstrings option.")
else:
    print("You have disabled the docstrings option.")

def main_menu():
    """-----
main_menu:
Info - Prints out basic info for the user explaining all options the program has to offer.
With an elif statement to execute based on user input.
After execution the code will ask if you would like to exit or restart from the beginning of the main menu again.
Details - The length of the main menu input options printed depends on the of the 'algo_intro' dictionary.
Throughout the project code wherever useful depends on the key respective values of the 'all_algo_names' or 'algo_intro' dictionaries as much
as possible in order to make adding extra algorithm execution options as easy as possible by simply adding extra entries to the two dictionaries.
-----
"""
    if print_docstrings:
        print(main_menu.__doc__)
    while True:

        # Forcing Python to flush the buffer right after the first print.
        # Other-wise the text would sometimes not print into the terminal when returning to the main menu.
        # Likely to do with Python buffering csv row data, holding a load of data in memory and outputting later.

        print("\n\nWelcome to the string matching main menu.\n", flush=True)

        print("To run options 1 or 2 the dataset.csv file must be present in the Put_Dataset_Here folder as described in the readme.md.\n"
              "Enter 1: To retrieve separate game review data from the main dataset and store the csv. [Warning can take up to 15s.]\n"
              "Enter 2: To create a reference dictionary specifying rows for all game_id's, increases the speed of option 1.\n"
              "         This reference dictionary should already exist, option 2 is here incase the dataset changes although it should remain the same.\n"
              "\nThe below algorithms will match your input pattern to a string list from a stored csv review file of your choice.\n")
        for algo_id in range(3, 2+len(algo_intro)+1):
            print(f"Enter {algo_id}: {algo_intro[str(algo_id)]}")
        menu_choice = int(usr_main_menu_chk(input('\n')))

        if menu_choice == 1:
            dataframe_sorting.raw_review_dataframe_to_split(print_docstrings)
        elif menu_choice == 2:
            get_dataset_rows_per_id.create_row_id_num_reference(print_docstrings)
        elif menu_choice >= 3:
            call_string_match(all_algo_names[str(menu_choice)])

        run_again = input("Enter 'x' to exit. Enter anything else to return to the main menu.")
        if run_again == 'x':
            break

main_menu()