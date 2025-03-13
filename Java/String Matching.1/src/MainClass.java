import java.util.*;
public class MainClass {
    public static void main(String[] args) {
        BoyerMooreHorspool bSearch = new BoyerMooreHorspool();
        Native nSearch = new Native();
        Naive Search = new Naive();
        RabinKarp rSearch = new RabinKarp();
        Kmp kSearch = new Kmp();
        CSVReader csvReader = new CSVReader(Search);
        CSVReader csvReader1 = new CSVReader(nSearch);
        CSVReader csvReader2 = new CSVReader(rSearch);
        CSVReader csvReader3 = new CSVReader(kSearch);
        CSVReader csvReader4 = new CSVReader(bSearch);
        Scanner input = new Scanner(System.in);
        String BufferClear;
        String text;
        String filePath;
        String pattern;
        int choice = 0;
        long startTime;
        long endTime;
        boolean exit = false;
        boolean check = false;

        while (!exit) {
            choice=0;
            startTime=0;
            endTime=0;

            System.out.println("Welcome to String matching, Chose algorithm ");
            System.out.println("1: Naive Algorithm(give String and Pattern)");
            System.out.println("2: Naive Algorithm(.csv) ");
            System.out.println("3: RabinKarp Algorithm(give String and Pattern) ");
            System.out.println("4: RabinKarp Algorithm (.csv)");
            System.out.println("5: KMP Algorithm(give String and Pattern) ");
            System.out.println("6: KMP Algorithm (.csv)");
            System.out.println("7: Native Algorithm(give String and Pattern) ");
            System.out.println("8: Native Algorithm(.csv) ");
            System.out.println("9: Boyer Moore Horspool Algorithm(give String and Pattern) ");
            System.out.println("10: Boyer Moore Horspool Algorithm(.csv) ");
            System.out.println("11: Exit ");
                try {
                    choice = input.nextInt();
                    check = true;  // Exit loop if an integer is successfully read.
                } catch (InputMismatchException e) {
                    input.nextLine();  // Clear the buffer by reading the line.
                }
                    switch (choice) {
                        case 1:
                            System.out.print("Enter the String to search: ");
                            BufferClear = input.nextLine();
                            text = input.nextLine(); // Read user input
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            Search.search(text, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 2:
                            System.out.print("Enter the path to the CSV file: ");
                            BufferClear = input.nextLine();
                            filePath = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            csvReader.readCSV(filePath, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 3:
                            System.out.print("Enter the String to search for: ");
                            BufferClear = input.nextLine();
                            text = input.nextLine(); // Read user input
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            rSearch.search(text, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 4:
                            System.out.print("Enter the path to the CSV file: ");
                            BufferClear = input.nextLine();
                            filePath = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            csvReader2.rkReadCSV(filePath, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 5:
                            System.out.print("Enter the String to search for: ");
                            BufferClear = input.nextLine();
                            text = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            kSearch.search(text, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 6:
                            System.out.print("Enter the path to the CSV file: ");
                            BufferClear = input.nextLine();
                            filePath = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            csvReader3.kmpReadCSV(filePath, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 7:
                            System.out.print("Enter the String to search for: ");
                            BufferClear = input.nextLine();
                            text = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            nSearch.search(text, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 8:
                            System.out.print("Enter the path to the CSV file: ");
                            BufferClear = input.nextLine();
                            filePath = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            csvReader1.nReadCSV(filePath, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 9:
                            System.out.print("Enter the String to search for: ");
                            BufferClear = input.nextLine();
                            text = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            bSearch.search(text, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 10:
                            System.out.print("Enter the path to the CSV file: ");
                            BufferClear = input.nextLine();
                            filePath = input.nextLine();
                            System.out.print("Enter the pattern to search for: ");
                            pattern = input.nextLine();
                            startTime = System.currentTimeMillis();
                            csvReader4.bmhReadCSV(filePath, pattern);
                            endTime = System.currentTimeMillis();
                            System.out.println("Time elapsed: " + (endTime - startTime));
                            break;
                        case 11:
                            exit = true;
                            break;
                        default:
                            System.out.println("Invalid Choice");
                    }

                }
            }
        }


