# Expense Tracker

## Overview
This is a simple web-based expense tracker application built using Flask and MySQL. It allows users to add, view, and delete expenses. The application is designed to be easy to set up and use.

## Features
- **Add Expenses**: Users can add new expenses by providing the amount, category, and date.
- **View Expenses**: All expenses are displayed in a tabular format on the homepage.
- **Delete Expenses**: Users can delete any expense by clicking the delete button associated with it.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- MySQL Server
- pip (Python package installer)

## Installation
1. Clone this repository.
2. Install MySQL Connector for Python if not already installed:
   ```sh
   pip install mysql-connector-python
   ```

### Set up the MySQL database:
1. Create a new database in MySQL.
2. Create a table named `expenses` with the following schema:
```sql
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(255) NOT NULL,
    date DATE NOT NULL
);
```

### Configure environment variables:
1. Create a `.env` file in the root directory of the project.
2. Add the following environment variables to the `.env` file:
```ini
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

## Running the Application
### Start the Flask development server:
```bash
python app.py
```

### Access the application:
Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Author
Tanveer Shakeel