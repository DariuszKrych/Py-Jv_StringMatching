import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class CSVReader {
    private Naive matcher;
    private Native nMatcher;
    private RabinKarp rkMatcher;
    private Kmp KmpMatcher;
    private BoyerMooreHorspool  bmhMatcher;

    public CSVReader(Naive matcher) {
        this.matcher = matcher;
    }

    public CSVReader(Native nMatcher) {
        this.nMatcher = nMatcher;
    }

    public CSVReader(RabinKarp rkMatcher) {
        this.rkMatcher = rkMatcher;
    }

    public CSVReader(Kmp KmpMatcher){
        this.KmpMatcher = KmpMatcher;
    }

    public CSVReader(BoyerMooreHorspool bmhMatcher) {
        this.bmhMatcher = bmhMatcher;
    }

    public void readCSV(String filePath, String pattern) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            int count = 0;
            String line;
            while ((line = br.readLine()) != null) {
                if (matcher.Search(line, pattern)) {
                    count++;
                }
            }
            System.out.println("Total Times: "+count);
        } catch (IOException e) {
            System.err.println("Error reading the CSV file: " + e.getMessage());
        }
    }

    public void nReadCSV(String filePath, String pattern) {
        int count = 0;
        String line;
        int lineNumber = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            while ((line = br.readLine()) != null) {
                lineNumber++;
                if(Native.Search(line, pattern)){
                    count++;
                }
            }
            System.out.println("Total Times: "+count);
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }
    }

    public void rkReadCSV(String filePath, String pattern) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            int count = 0;
            String line;
            while ((line = br.readLine()) != null) {
                if (rkMatcher.Search(line, pattern)) {
                    count++;
                }
            }
            System.out.println("Total Times: "+count);
        } catch (IOException e) {
            System.err.println("Error reading the CSV file: " + e.getMessage());
        }
    }
    public void kmpReadCSV(String filePath, String pattern) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            int count = 0;
            String line;
            while ((line = br.readLine()) != null) {
                if (KmpMatcher.Search(line, pattern)) {
                    count++;
                }
            }
            System.out.println("Total Times: "+count);
        } catch (IOException e) {
            System.err.println("Error reading the CSV file: " + e.getMessage());
        }
    }
    public void bmhReadCSV(String filePath, String pattern) {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            int count = 0;
            String line;
            while ((line = br.readLine()) != null) {
                if (bmhMatcher.Search(line, pattern)) {
                    count++;
                }
            }
            System.out.println("Total Times: "+count);
        } catch (IOException e) {
            System.err.println("Error reading the CSV file: " + e.getMessage());
        }
    }
}
