# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from dotenv import load_dotenv
import os
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    """
    User class for handling user authentication.

    Attributes:
        id (str): User ID.
        username (str): Username of the user.
    """
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    @property
    def is_authenticated(self):
        """Checks if the user is authenticated."""
        return True

    @property
    def is_active(self):
        """Checks if the user is active."""
        return True

    @property
    def is_anonymous(self):
        """Checks if the user is anonymous."""
        return False

    def get_id(self):
        """Returns the user's ID."""
        return self.id

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
@login_required
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
@login_required
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
@login_required
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

@login_manager.user_loader
def load_user(user_id):
    """
    Load a user from the database by user ID.

    Args:
        user_id: the ID of the user to be loaded

    Returns:
        User object if user is found, None otherwise
    """
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()
    if user_data:
        return User(user_data["id"], user_data["username"])
    return None

@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register a new user.

    Handles user registration by inserting new user data
    into the database if the username is not already taken.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        connection = connect_to_database()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash("Username already exists. Please choose another.", "error")
            else:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
                connection.commit()
                flash("Registration successful! Please log in.", "success")
                return redirect(url_for("login"))
        except mysql.connector.Error as err:
            flash("An error occurred during registration. Please try again.", "error")
        finally:
            cursor.close()
            connection.close()
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in an existing user.

    Authenticates the user by verifying the username and password
    against the database records.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()

        if user_data and check_password_hash(user_data["password"], password):
            user = User(user_data["id"], user_data["username"])
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password. Please try again.", "error")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    """
    Log out the current user.

    Logs out the current user and redirects to the login page.
    """
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("login"))

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)