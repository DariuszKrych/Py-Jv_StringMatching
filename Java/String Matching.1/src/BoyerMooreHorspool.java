public class BoyerMooreHorspool {
    public void search(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int counter = 0;

        if (m > n) {
            System.out.println("Pattern not found");
            return;
        }

        // Step 1: Create the bad character shift table
        int[] badCharShift = new int[256]; // 256 for all possible characters
        for (int i = 0; i < 256; i++) {
            badCharShift[i] = m; // Default shift is the length of the pattern
        }
        for (int i = 0; i < m - 1; i++) {
            badCharShift[pattern.charAt(i) & 0xFF] = m - i - 1; // Set the shift value for this character
        }

        // Step 2: Search
        int offset = 0;
        while (offset <= n - m) {
            int j = m - 1;
            while (j >= 0 && pattern.charAt(j) == text.charAt(offset + j)) {
                j--;
            }
            if (j < 0) {
                counter ++;

            }
            offset += badCharShift[text.charAt(offset + m - 1) & 0xFF]; // Use the bad character shift
        }
        System.out.println(counter);


    }
    public boolean Search(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int counter = 0;

        if (m > n) {
            System.out.println("Pattern not found");

        }

        // Step 1: Create the bad character shift table
        int[] badCharShift = new int[256]; // 256 for all possible characters
        for (int i = 0; i < 256; i++) {
            badCharShift[i] = m; // Default shift is the length of the pattern
        }
        for (int i = 0; i < m - 1; i++) {
            badCharShift[pattern.charAt(i) & 0xFF] = m - i - 1; // Set the shift value for this character
        }

        // Step 2: Search
        int offset = 0;
        while (offset <= n - m) {
            int j = m - 1;
            while (j >= 0 && pattern.charAt(j) == text.charAt(offset + j)) {
                j--;
            }
            if (j < 0) {
                counter++;

            }
            offset += badCharShift[text.charAt(offset + m - 1) & 0xFF]; // Use the bad character shift
        }


        return counter>0;
    }
}
