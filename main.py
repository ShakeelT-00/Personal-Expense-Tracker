def load_expenses():
    pass


def add_expense(expenses):
    pass


def view_expenses(expenses):
    pass


def save_expenses(expenses):
    pass


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
