import mmh3

class StringMatchingAlgorithms:

    @staticmethod
    def native_algo(review_list, pattern, print_docstrings):
        """-----
native_algo:
Info - This is the simplest string matching algorithm which simply slides the pattern along the text with all characters in the pattern being
compared directly to all characters in that part of the text(input strings from review_list), until all possible comparison positions
have been passed through. This is the only algorithm which has no pre-processing of variables to showcase that it is decidedly quicker
to pre-process variables instead of re-computing them over and over as in this example.
Details - Maximum time complexity is O(n*m) while Minimum time complexity is O(n).  Where m is the pattern length and n is the text length.
-----
"""
        if print_docstrings:
            print(StringMatchingAlgorithms.native_algo.__doc__)

        # Initialising variable(s).
        matches = 0

        # Loop through each string in the review list one at a time.
        for string in review_list:
            n = 0
            while len(str(string)) > n:
                if str(string)[n:n+len(pattern)] == str(pattern):
                    matches = matches + 1
                n = n + 1

        return ['3', matches]



    @staticmethod
    def native_algo_preprocessing(review_list, pattern, print_docstrings):
        """-----
native_algo_preprocessing:
Info - This is the simplest string matching algorithm which simply slides the pattern along the text with all characters in the pattern being
compared directly to all characters in that part of the text(input strings from review_list), until all possible comparison positions
have been passed through. This is the same as the native_string_matching_algo other than variables being pre-processed which is much quicker
and is implemented in all other algorithms.
Details - Maximum time complexity is O(n*m). Minimum time complexity is O(n).  Where m is the pattern length and n is the text length.
-----
"""
        if print_docstrings:
            print(StringMatchingAlgorithms.native_algo_preprocessing.__doc__)

        # Pre-processing and storing: 'pattern' var as a string type and pattern length.
        pattern = str(pattern);  pattern_length = len(pattern)
        # Initialising variable(s).
        matches = 0

        for string in review_list:
            # Pre-processing and storing: 'string' var as a string type and string length.
            string = str(string);  string_length = len(string);  n = 0
            # Compare input string to whole string by moving along the character range one by one.
            while string_length > n:
                if string[n:n+pattern_length] == pattern:
                    matches = matches + 1
                n = n + 1

        return ['4', matches]



    @staticmethod
    def naive_algo(review_list, pattern, print_docstrings):
        """-----
naive_algo:
Info - This is the simplest string matching algorithm which simply slides the pattern along the text with all characters in the pattern being
compared directly to all characters in that part of the text(input strings from review_list), until all possible comparison positions
have been passed through. This is the same as the native algorithms other than it actually comparing each character in the pattern to each
character in the text one by one properly instead of using built-in python string comparison.
Details - Maximum time complexity is O(n*m). Minimum time complexity is O(n).  Where m is the pattern length and n is the text length.
-----
"""
        if print_docstrings:
            print(StringMatchingAlgorithms.naive_algo.__doc__)

        # Pre-processing and storing: 'pattern' var as a string type and pattern length.
        pattern = str(pattern);  pattern_length = len(pattern)
        # Initialising variable(s).
        matches = 0

        for string in review_list:
            string = str(string);  string_length = len(str(string))
            # Loops from 0 to x-1. Sliding along string with first loop and for pattern length with second loop.
            for string_slide in range(string_length + 1 - pattern_length):
                # Assumes match, checks if the part string segment is different from pattern if so mismatch.
                match = 1 # Slightly faster to have match=1,0 if match==1: than match=True,False if match:
                for pattern_slide in range(pattern_length):   # Loops from 0 to len(pattern)-1.
                    # Comparing chars, if different move onto next string slide.
                    if string[string_slide+pattern_slide] != pattern[pattern_slide]:
                        match = 0; break
                if match == 1:
                    matches = matches + 1

        return ['5', matches]



    # Runs really slowly as some ord (ascii char id's) can be quite large so doing calcs can take a while.
    # Also is fully implemented in slow Python calls etc. Running hashing in libraries written in C etc... would be much faster.
    @staticmethod
    def rabin_karp_algo_py(review_list, pattern,print_docstrings):
        """-----
rabin_karp_algo_py:
Info - The rabin karp string matching algorithm hashes the pattern and text and then compares the hashes of these characters
using the exact same principle the native string matching algorithm uses sliding the pattern along the text but now checking if
the hashes match instead of if characters match. This algorithm implementation uses my own custom hashing with the ASCII number codes which
works fine with the fact that it can accept real world data which will be passed through it as all characters has an ASCII number code.
The main downside is that depending on the specific character the code number can be quite large slowing down the algorithm significantly
if such characters are found in the input text or pattern.
Details - Maximum time complexity is O(n*m). Minimum time complexity is O(n+m). Where m is the pattern length and n is the text length.
-----
"""
        if print_docstrings:
            print(StringMatchingAlgorithms.rabin_karp_algo_py.__doc__)

        # Pre-processing and storing: 'pattern' var as a string type and pattern length.
        pattern = str(pattern);  pattern_length = len(pattern)
        # Initialising variable(s).
        hash_matches = [];  matches = 0

        # Getting hash of pattern string by summing ascii id's & getting remainder of div by a prime num(13).
        check_ascii_id = 0
        for char in pattern:
            check_ascii_id = check_ascii_id + ord(char)
        check_hash = check_ascii_id % 13

        # Getting all string segments of pattern length where hash equals pattern hash.
        for string in review_list:

            # Pre-processing and storing: 'string' var as a string type and string length.
            string = str(string);  string_length = len(string)
            # Initialising variable(s).
            n = 0

            while string_length > n:
                string_ascii_id = 0
                # Getting the hash of set of chars in string of length of pattern.
                for char in string[n:n+pattern_length]:
                    string_ascii_id = string_ascii_id + ord(char)
                string_hash = string_ascii_id % 13
                # If the hash of the string chars = pattern chars add it to the list to native match for.
                if string_hash == check_hash:
                    hash_matches.append(string[n:n+pattern_length])
                n = n + 1

        # print(f"{hash_matches}")

        # Loop through each string in the hash matches list one at a time.
        for string in hash_matches:
            if string == pattern:
                matches = matches + 1

        return ['6', matches]



    @staticmethod
    def rabin_karp_algo_lib(review_list, pattern, print_docstrings):
        """-----
rabin_karp_algo_lib:
Info - The rabin karp string matching algorithm hashes the pattern and text and then compares the hashes of these characters
using the exact same principle the native string matching algorithm uses sliding the pattern along the text but now checking if
the hashes match instead of if characters match. This algorithm implementation uses hashing with the mmh3 library which is mostly
written in C which means it will run much faster than my own custom hashing algorithm. This library has deterministic hashing which is
fast, this is not secure but for this algorithm where speed is the most important factor it is ideal.
Details - Maximum time complexity is O(n*m). Minimum time complexity is O(n+m). Where m is the pattern length and n is the text length.
-----
"""
        if print_docstrings:
            print(StringMatchingAlgorithms.rabin_karp_algo_lib.__doc__)

        # Pre-processing and storing: 'pattern' var as a string type and pattern length.
        pattern = str(pattern);  pattern_length = len(pattern)
        # Initialising variable(s).
        hash_matches = [];  matches = 0

        # mmh3 is a quick deterministic hashing library.
        # The downside is it has no security which isn't relevant here.
        check_hash = mmh3.hash(pattern)

        for string in review_list:

            # Pre-processing and storing: 'string' var as a string type and string length.
            string = str(string);  string_length = len(string)
            # Initialising variable(s).
            n = 0

            while string_length > n:
                string_hash = mmh3.hash(string[n:n+pattern_length])
                if string_hash == check_hash:
                    hash_matches.append(string[n:n+pattern_length])
                n = n + 1

        # Loop through each string in the hash matches list one at a time.
        for string in hash_matches:
            if string == pattern:
                matches = matches + 1

        return ['7', matches]



    @staticmethod
    def boyer_moore_horspool_algo(review_list, pattern,print_docstrings):
        """-----
boyer_moore_horspool_algo:
Info - Moves the pattern across the text but instead of always sliding by 1 like the native/naive/rabin karp algorithms the boyer moore horspool
algorithm uses the bad character rule to skip over character comparisons using the bad character rule.
A bad character table is generated for the pattern which stores the last occurrence index of each character in the pattern,
enabling the algorithm to skip comparisons which are definitely not going to be matches.
Details - Maximum time complexity is O(n*m). Minimum time complexity is O(n/m). Where m is the pattern length and n is the text length.
As a cool sidenote this is from my understanding the most commonly used string matching algorithm so this algorithm is what is
running when you press ctrl+f to search something on a website online. It is not theoretically the fastest algorithm although with real-world
data it tends to be which is why I implemented it as it seems too interesting to not implement.
-----
"""
        if print_docstrings:
            print(StringMatchingAlgorithms.boyer_moore_horspool_algo.__doc__)

        # Pre-processing and storing: 'pattern' var as a string type and pattern length.
        pattern = str(pattern);  pattern_length = len(pattern)
        # Initialising variable(s).
        matches = 0;  bad_char_ref = {}

        # Bad Character Rule Pre-Processing.
        # Enumerate will increase 'index' val by 1 for each next loop over.
        # Starting at the value n enumerate(str, n). By default n is 0.
        # Loop iterates for all of 'char' in 'pattern' str.
        for index, char in enumerate(pattern, 0):
            # Setting current 'index' value as a value for the current 'char' key. Only one value can be set per given key.
            # The most recent 'index' val will overwrite the previous 'index' val for a given 'char' key. dict[key]=val
            bad_char_ref[char] = index

        # Searching in each review string (text).
        for string in review_list:

            # Pre-processing and storing: 'string' var as a string type and string length.
            string = str(string);  string_length = len(string)
            # Initialising variable(s).
            string_parse_pos = 0

            # Parsing text from left to right.
            while string_parse_pos <= string_length - pattern_length:
                # Start from the end of the pattern
                skip = 0
                # Parsing pattern from right to left.
                # Range(start,stop,step), Range(a, z, n) contains a,a+n,a+2n...until a+Xn>=z
                # From (pattern_length-1) to -1 in steps of -1 will yield index positions for the pattern string in reverse.
                for pattern_parse_pos in range(pattern_length - 1, -1, -1):
                    if pattern[pattern_parse_pos] != string[string_parse_pos + pattern_parse_pos]:
                        skip_char = string[string_parse_pos + pattern_parse_pos]
                        # Calculate the shift based on bad character rule.
                        # pattern_parse_pos increased by at least 1 or more depending on bad_char_ref for the character
                        # mismatched to in the text.
                        if skip_char in bad_char_ref:
                            skip = max(1, pattern_parse_pos - bad_char_ref[skip_char])
                        else:
                            skip = pattern_parse_pos + 1
                        # Mismatch has been found so further char comparisons are unnecessary for the same pattern_parse_pos.
                        break
                # If no mismatch found then no skips based on mismatch info have been performed.
                # Pattern match has been found. Can skip past for pattern length.
                if skip == 0:
                    matches += 1
                    skip = pattern_length
                string_parse_pos += skip

        return ['8', matches]


    @staticmethod
    def kmp_algo(review_list, pattern,print_docstrings):
        """-----
kmp_algo:
Info - The Knuth Morris Pratt (KMP) algorithm improves string matching by avoiding unnecessary re-evaluations of characters
comparisons between the pattern and text after a mismatch between characters occurs.
Instead of restarting the match, the algorithm uses a prefix table (also called the "partial match table")
to determine the next position to continue matching based on the pattern's prefix-suffix properties.
Details - Maximum time complexity is O(n+m). Minimum time complexity is O(n). Where m is the pattern length and n is the text length.
-----
"""
        if print_docstrings:
            print(StringMatchingAlgorithms.kmp_algo.__doc__)

        pattern = str(pattern);  pattern_length = len(pattern)

        matches = 0

        for string in review_list:
            string = str(string);  string_length = len(string)

            # Preprocess the pattern to build the longest prefix suffix array
            length = 0  # length of the previous longest prefix suffix
            pattern_slide = 1
            longest_prefix_suffix = [0] * pattern_length
            string_slide = 0  # index for review string
            longest_prefix_suffix[0] = 0  # lps[0] is always 0

            # the loop calculates lps[i] for (i = 1) to (pattern_length-1)
            while pattern_slide < pattern_length:
                if pattern[pattern_slide] == pattern[length]:
                    length += 1
                    longest_prefix_suffix[pattern_slide] = length
                    pattern_slide += 1
                else:
                    if length != 0:
                        length = longest_prefix_suffix[length - 1]
                    else:
                        longest_prefix_suffix[pattern_slide] = 0
                        pattern_slide += 1

            pattern_slide = 0  # index for pattern
            while string_slide < string_length:
                if pattern[pattern_slide] == string[string_slide]:
                    pattern_slide += 1
                    string_slide += 1

                if pattern_slide == pattern_length:
                    matches = matches + 1
                    # print("Found pattern at index", string_slide - pattern_slide)
                    pattern_slide = longest_prefix_suffix[pattern_slide - 1]

                # mismatch after j matches
                elif string_slide < string_length and pattern[pattern_slide] != string[string_slide]:
                    # Do not match lps[0..lps[i-1]] characters,
                    # they will match anyway
                    if pattern_slide != 0:
                        pattern_slide = longest_prefix_suffix[pattern_slide - 1]
                    else:
                        string_slide += 1

        return ['9', matches]