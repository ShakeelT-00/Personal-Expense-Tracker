import mysql.connector

"""
Connect to the MySQL database.

Returns:
    connection: the MySQL connection object

Raises:
    mysql.connector.Error: if there is an error connecting to the database
"""
def connect_to_database():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="M@Desktop19",
            database="expense_tracker"
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        exit()


"""
Add a new expense to the database.

Prompts the user for the expense amount, category, and date.
"""
def add_expense():
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)"
    values = (amount, category, date)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    
    print("Expense added successfully.")


"""
View all the expenses in the database.

Prints out a list of all expenses in the database, including the ID,
amount, category, and date.
"""
def view_expenses():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    
    print("\n--- All Expenses ---")
    for expense in expenses:
        print(f"ID: {expense[0]}, Amount: {expense[1]}, Category: {expense[2]}, Date: {expense[3]}")
    
    cursor.close()
    connection.close()


"""
Main function to run the program.

Displays a menu for the user to choose from, and calls the appropriate
function based on the user's choice.
"""
def main():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
