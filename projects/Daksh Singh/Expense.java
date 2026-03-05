import java.time.*;
import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;
import java.text.*;
import java.time.format.DateTimeFormatter;

/**
 * Represents a single expense with amount, category, and date.
 */
public class Expense {

    private double amount;
    private String category;
    private LocalDate date;

    // Formatter for amount (₹ and two decimals)
    private static final DecimalFormat moneyFormat = new DecimalFormat("#,##0.00");

    // Formatter for date (e.g., 25 Aug 2025)
    private static final DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("dd MMM yyyy");

    public Expense(double amount, String category, LocalDate date) {
        this.amount = amount;
        this.category = category;
        this.date = date;
    }

    public double getAmount() {
        return amount;
    }

    public String getCategory() {
        return category;
    }

    public LocalDate getDate() {
        return date;
    }

    @Override
    public String toString() {
        return "Expense{" +
                "amount=" + moneyFormat.format(amount) +
                ", category='" + category + '\'' +
                ", date=" + date.format(dateFormatter) +
                '}';
    }
}
