# Expense Tracker

## Overview
The Expense Tracker is a simple command-line application written in Python that allows users to record and view their expenses. It uses a MySQL database to store expense records, making it easy to track spending over time.

## Features
- Add new expenses, including amount, category, and date.
- View all recorded expenses.
- Simple menu-based interface for ease of use.

## Prerequisites
Before running the program, ensure you have the following installed:
- Python (version 3.x recommended)
- MySQL Server
- MySQL Connector for Python

## Database Setup
1. Create a MySQL database named `expense_tracker`:
   ```sql
   CREATE DATABASE expense_tracker;
   ```
2. Switch to the database:
   ```sql
   USE expense_tracker;
   ```
3. Create the `expenses` table:
   ```sql
   CREATE TABLE expenses (
       id INT AUTO_INCREMENT PRIMARY KEY,
       amount DECIMAL(10,2) NOT NULL,
       category VARCHAR(255) NOT NULL,
       date DATE NOT NULL
   );
   ```

## Installation
1. Clone this repository or copy the script.
2. Install MySQL Connector for Python if not already installed:
   ```sh
   pip install mysql-connector-python
   ```
3. Update the database connection details in the `connect_to_database()` function:
   ```python
   def connect_to_database():
       return mysql.connector.connect(
           host="localhost",
           user="your_mysql_username",
           password="your_mysql_password",
           database="expense_tracker"
       )
   ```

## Usage
1. Run the script:
   ```sh
   python expense_tracker.py
   ```
2. Choose an option from the menu:
   - `1`: Add a new expense
   - `2`: View all expenses
   - `3`: Exit the program

## Error Handling
- The program will display an error message if it fails to connect to the database.
- Invalid user input (e.g., incorrect formats) may cause the program to crash. Future improvements can include validation.

## Future Enhancements
- Add functionality to delete or update expenses.
- Implement filtering options (e.g., view expenses by category or date range).
- Improve input validation and error handling.

## License
This project is open-source and available under the MIT License.

## Author
Tanveer Shakeel
