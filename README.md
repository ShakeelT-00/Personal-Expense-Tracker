# Expense Tracker

A simple command-line based expense tracking application.

## Features

- **Add Expenses**: Add new expenses with details such as amount, category, and date.
- **View Expenses**: View all expenses that have been added.
- **Save and Exit**: Save the expenses to a CSV file and exit the application.

## Usage

1. Run the application using `python main.py`.
2. Follow the prompts to:
   - Add a new expense.
   - View all expenses.
   - Save expenses and exit the application.

## Code Structure

The application is structured into the following functions:

- **`load_expenses(filename="expenses.csv")`**: Loads expenses from a CSV file. If the file does not exist, it initializes an empty list.
- **`add_expense(expenses)`**: Prompts the user to input the amount, category, and date of the expense, then adds it to the list.
- **`view_expenses(expenses)`**: Displays all expenses in a readable format.
- **`save_expenses(expenses, filename="expenses.csv")`**: Saves the list of expenses to a CSV file.
- **`main()`**: The main application loop that handles user input and calls the appropriate functions.

## Example Usage

```bash
$ python main.py

1. Add Expense
2. View Expenses
3. Save and Exit
Enter your choice: 1
Enter the amount: 25.50
Enter the category: Food
Enter the date (YYYY-MM-DD): 2023-10-01
Expense added.

1. Add Expense
2. View Expenses
3. Save and Exit
Enter your choice: 2
Amount: 25.5, Category: Food, Date: 2023-10-01

1. Add Expense
2. View Expenses
3. Save and Exit
Enter your choice: 3
Expenses saved.