public class RabinKarp {
    /// Prime number for hash calculation
    private final int PRIME = 101;

    public  void search(String text, String pattern) {
        int m = pattern.length();
        int n = text.length();
        int counter = 0;

        // Calculate the hash of the pattern and the initial hash of the text substring
        long patternHash = createHash(pattern, m);
        long textHash = createHash(text, m);

        for (int i = 0; i <= n - m; i++) {
            // If the hash values match, then check the characters to confirm
            if (patternHash == textHash && checkEqual(text, i, i + m - 1, pattern)) {
                counter++;
            }
            // Compute the hash of the next substring (rolling hash)
            if (i < n - m) {
                textHash = recalculateHash(text, i, i + m, textHash, m);
            }
        }
        System.out.println(counter);
    }
    public boolean  Search(String text, String pattern) {
        int m = pattern.length();
        int n = text.length();
        int counter = 0;

        // Calculate the hash of the pattern and the initial hash of the text substring
        long patternHash = createHash(pattern, m);
        long textHash = createHash(text, m);

        for (int i = 0; i <= n - m; i++) {
            // If the hash values match, then check the characters to confirm
            if (patternHash == textHash && checkEqual(text, i, i + m - 1, pattern)) {
                counter++;
            }
            // Compute the hash of the next substring (rolling hash)
            if (i < n - m) {
                textHash = recalculateHash(text, i, i + m, textHash, m);
            }
        }
        return counter > 0;
    }

    // Hash function for initial substring hash
    private  long createHash(String str, int end) {
        long hash = 0;
        for (int i = 0; i < end; i++) {
            hash += str.charAt(i) * Math.pow(PRIME, i);
        }
        return hash;
    }

    // Rolling hash function to update the hash when sliding the window
    private  long recalculateHash(String str, int oldIndex, int newIndex, long oldHash, int patternLength) {
        long newHash = oldHash - str.charAt(oldIndex);
        newHash /= PRIME;
        newHash += str.charAt(newIndex) * Math.pow(PRIME, patternLength - 1);
        return newHash;
    }

    // Utility to confirm hash match with actual substring
    private boolean checkEqual(String text, int start1, int end1, String pattern) {
        for (int i = 0; i <= end1 - start1; i++) {
            if (text.charAt(start1 + i) != pattern.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
