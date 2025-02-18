import csv


def load_expenses(filename="expenses.csv"):
    expenses = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
            pass
    return expenses


def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Expense added.")


def view_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")


def save_expenses(expenses, filename="expenses.csv"):
    with open(filename , mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "date"])
        writer.writeheader()
        writer.writerows(expenses)


def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            save_expenses(expenses)
            print("Expenses saved.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
