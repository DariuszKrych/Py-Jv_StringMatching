public class Kmp {
    //Function to compute the Longest Prefix Suffix (LPS) array
    public  int[] computeLPSArray(String pattern, int m, int[] lps) {
        m = pattern.length();
        lps = new int[m];
        int length = 0; // Length of the previous longest prefix suffix
        int i = 1;

        lps[0] = 0; // LPS of the first character is always 0

        // Loop to calculate lps[i] for i = 1 to m-1
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        return lps;
    }

    // Function to implement the KMP Search
    public  int search(String pattern, String text) {
        int m = pattern.length();
        int n = text.length();
        int counter = 0;

        // Preprocess the pattern to get the LPS array
        int[] lps = new int[0];
        lps = computeLPSArray(pattern, m, lps);

        int i = 0; // Index for text
        int j = 0; // Index for pattern

        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }

            if (j == m) {
                counter++;
                j = lps[j - 1];
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        System.out.println(counter);
        return m;
    }
    public boolean Search(String txt, String pat) {
        int M = pat.length();
        int N = txt.length();
        int[] lps = new int[M];
        int j = 0; // index for pat[]

        computeLPSArray(pat, M, lps);

        int i = 0; // index for txt[]
        while (i < N) {
            if (pat.charAt(j) == txt.charAt(i)) {
                j++;
                i++;
            }
            if (j == M) {
                return true;
            } else if (i < N && pat.charAt(j) != txt.charAt(i)) {
                if (j != 0)
                    j = lps[j - 1];
                else
                    i = i + 1;
            }
        }
        return false;
    }
}