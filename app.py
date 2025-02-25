# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def connect_to_database():
    """
    Connect to the MySQL database.

    Connects to the MySQL database using the environment variables
    DB_HOST, DB_USER, DB_PASSWORD, and DB_NAME.

    Returns:
        connection: the MySQL connection object

    Raises:
        mysql.connector.Error: if there is an error connecting to the database
    """
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        exit()

@app.route("/")
def home():
    """
    Display all expenses from the database.

    Queries the database for all expenses and renders the index.html
    template with the expenses passed as a parameter.
    """
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    """
    Insert a new expense into the database.

    Inserts a new expense into the database using the form data
    passed from the index.html template.
    """
    amount = request.form.get("amount")
    category = request.form.get("category")
    date = request.form.get("date")
    
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)"
    values = (amount, category, date)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for("home"))

@app.route("/delete/<int:id>")
def remove_expense(id):
    """
    Delete an expense from the database by ID.

    Deletes the expense with the given ID from the database.

    Args:
        id: the ID of the expense to be deleted

    Returns:
        HTTP redirect to /
    """
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "DELETE FROM expenses WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)