
public class Naive {
    private int n;
    private int m;

    // Method to perform the naive string matching
    public void search(String text, String pattern) {
        n = text.length();
        m = pattern.length();
        int count = 0; // Counter to track the number of matches
        // Loop over the text until we reach a point where there are enough characters left for a full match
        for (int i = 0; i <= n - m; i++) {
            int j;

            // Check if pattern matches at this position
            for (j = 0; j < m; j++) {
                if (text.charAt(i + j) != pattern.charAt(j)) {
                    break; // Mismatch found, break inner loop
                }
            }

            // If the pattern fully matched the text substring
            if (j == m) {
                count++; // Increment the counter
            }
        }
        System.out.println("The patter showed up:" + count + " times");
    }

    public boolean Search(String text, String pattern) {
        n = text.length();
        m = pattern.length();
        int count = 0; // Counter to track the number of matches
        // Loop over the text until we reach a point where there are enough characters left for a full match
        for (int i = 0; i <= n - m; i++) {
            int j;

            // Check if pattern matches at this position
            for (j = 0; j < m; j++) {
                if (text.charAt(i + j) != pattern.charAt(j)) {
                    break; // Mismatch found, break inner loop
                }
            }

            // If the pattern fully matched the text substring
            if (j == m) {
                count++; // Increment the counter
            }
        }

        return count>0;
    }
}

