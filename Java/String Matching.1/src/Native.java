public class Native {
    public void search(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int counter=0;

        for (int i = 0; i <= n - m; i++) {
            int j;
            for (j = 0; j < m; j++) {
                if (text.charAt(i + j) != pattern.charAt(j)) {
                    break; // If mismatch, break out of the inner loop
                }
            }
            if (j == m) { // If the whole pattern was matched
                counter++;

            }
        }
        System.out.println("the pattern showed up: "+counter+ " times");

    }
    public static boolean Search(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int counter=0;

        for (int i = 0; i <= n - m; i++) {
            int j;
            for (j = 0; j < m; j++) {
                if (text.charAt(i + j) != pattern.charAt(j)) {
                    break; // If mismatch, break out of the inner loop
                }
            }
            if (j == m) { // If the whole pattern was matched
                counter++;
            }
        }
        return counter>0;

    }
}
