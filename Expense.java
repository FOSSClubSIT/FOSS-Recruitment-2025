import java.time.*;
import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;

/**
 * Represents a single expense with amount, category, and date.
 */
public class Expense {

    private double amount;
    private String category;
    private LocalDate date;

    /**
     * Constructor for Expense
     * 
     * @param amount   The expense amount
     * @param category The category of the expense (e.g. Food, Travel)
     * @param date     The date of the expense
     */
    public Expense(double amount, String category, LocalDate date) {
        this.amount = amount;
        this.category = category;
        this.date = date;
    }

    /** @return amount of this expense */
    public double getAmount() {
        return amount;
    }

    /** @return category of this expense */
    public String getCategory() {
        return category;
    }

    /** @return date of this expense */
    public LocalDate getDate() {
        return date;
    }

    /**
     * Returns a string representation of the expense
     */
    @Override
    public String toString() {
        return "Expense{" +
                "amount=" + amount +
                ", category='" + category + '\'' +
                ", date=" + date +
                '}';
    }

}
