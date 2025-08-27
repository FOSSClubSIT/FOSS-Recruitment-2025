import java.time.*;
import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.text.*;
import java.time.format.DateTimeFormatter;

/**
 * ExpeneTracker is the main application class.
 * It provides a simple menu system to add and view expenses.
 */
public class ExpenseTracker {
    private static String fileName = "expenses.txt";
    // List to hold all expense objects
    private static ArrayList<Expense> expenses = new ArrayList<>();

    // Scanner object for user input
    private static Scanner scanner = new Scanner(System.in);

    /**
     * Main method: entry point of the program.
     * Displays a menu to interact with the expense tracker.
     */
    public static void main(String[] args) {
        loadExpenses();
        boolean running = true;

        // Loop until user chooses to exit
        while (running) {
            System.out.println("\n--- Expense Tracker ---");
            System.out.println("1. Add Expense");
            System.out.println("2. Show All Expenses");
            System.out.println("3. Save Expenses to File");
            System.out.println("4. Show Total Expenses");
            System.out.println("5. Show Category-wise Summary");
            System.out.println("6. Exit");

            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    addExpense();
                    break;
                case 2:
                    showExpenses();
                    break;
                case 3:
                    saveExpensesToFile();
                    break;
                case 4:
                    showTotalExpenses();
                    break;
                case 5:
                    showCategorySummary();
                    break;
                case 6:
                    saveExpensesToFile(); // auto-save before quitting
                    running = false;
                    System.out.println("Exiting... Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice, try again.");
            }
        }
    }

    /**
     * Prompts the user to enter expense details and adds it to the list.
     */
    private static void addExpense() {
        double amount = 0;
        boolean valid = false;

        // keep asking until user gives a valid number
        while (!valid) {
            System.out.print("Enter amount: ");
            String input = scanner.nextLine();
            try {
                amount = Double.parseDouble(input);
                valid = true;
            } catch (NumberFormatException e) {
                System.out.println(" Invalid amount. Please enter a number.");
            }
        }

        System.out.print("Enter category (e.g. Food, Travel): ");
        String category = scanner.nextLine();

        Expense expense = new Expense(amount, category, LocalDate.now());
        expenses.add(expense);

        System.out.println(" Expense added: " + expense);
    }

    /**
     * Displays all expenses stored in memory.
     * 
     * If no expenses exist, it shows a message. Otherwise, it prints all
     * expenses with their details using the `toString()` method of Expense.
     */
    private static void showExpenses() {
        // Check if the expenses list is empty
        if (expenses.isEmpty()) {
            System.out.println("No expenses recorded yet.");
        } else {
            System.out.println("\n--- All Expenses ---");

            // Loop through each expense and print it
            for (Expense e : expenses) {
                System.out.println(e);
            }
        }
    }

    /**
     * Saves all expenses into a text file chosen by the user.
     * The file will be created in the same directory where the program is run.
     */
    private static void saveExpensesToFile() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (Expense e : expenses) {
                writer.write(e.getAmount() + "," + e.getCategory() + "," + e.getDate());
                writer.newLine();
            }
            System.out.println(" Expenses saved to " + fileName);
        } catch (IOException e) {
            System.out.println("Error saving expenses: " + e.getMessage());
        }
    }

    /**
     * Calculates and displays the total of all recorded expenses.
     */
    private static void showTotalExpenses() {
        if (expenses.isEmpty()) {
            System.out.println("No expenses recorded yet.");
        } else {
            double total = 0;
            for (Expense e : expenses) {
                total += e.getAmount(); // make sure Expense class has getAmount()
            }
            System.out.println(" Total Expenses: " + total);
        }
    }

    /**
     * Loads expenses from the text file (if it exists) at startup.
     */
    private static void loadExpenses() {
        File file = new File(fileName);

        if (!file.exists()) {
            System.out.println("No previous expenses found, starting fresh.");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // format: amount,category,date
                String[] parts = line.split(",");
                if (parts.length == 3) {
                    double amount = Double.parseDouble(parts[0]);
                    String category = parts[1];
                    LocalDate date = LocalDate.parse(parts[2]);
                    expenses.add(new Expense(amount, category, date));
                }
            }
            System.out.println(" Loaded " + expenses.size() + " expenses from file.");
        } catch (IOException e) {
            System.out.println("Error loading expenses: " + e.getMessage());
        }
    }

    /**
     * Shows the total expenses grouped by category.
     */
    private static void showCategorySummary() {
        if (expenses.isEmpty()) {
            System.out.println("No expenses recorded yet.");
            return;
        }

        Map<String, Double> categoryTotals = new HashMap<>();
        for (Expense e : expenses) {
            categoryTotals.put(e.getCategory(),
                    categoryTotals.getOrDefault(e.getCategory(), 0.0) + e.getAmount());
        }

        System.out.println("\n--- Category-wise Summary ---");
        for (Map.Entry<String, Double> entry : categoryTotals.entrySet()) {
            System.out.println(entry.getKey() + " = R" + String.format("%.2f", entry.getValue()));
        }
    }

}
