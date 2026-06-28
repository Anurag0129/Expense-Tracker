from datetime import date
import json

expenses = []

# *********  START  *** function to add the expenses*** START ***********
def add_expense():
    category = input("Enter category (e.g. Food, Travel, Rent): ")
    amount = input("Enter amount: ")
    note = input("Enter a short note (optional): ")
    expense = {
        "date": str(date.today()),
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")
# ********* End *** function to add the expenses***End ***********


# ********* START *** function to view the expenses *** START ***********
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n{:<12} {:<15} {:<10} {:<20}".format("Date", "Category", "Amount", "Note"))
    print("-" * 60)
    for expense in expenses:
        print("{:<12} {:<15} {:<10} {:<20}".format(
            expense["date"],
            expense["category"],
            expense["amount"],
            expense["note"]
        ))
# ********* END *** function to view the expenses *** END ***********


# ****** function to save the expenses *********
DATA_FILE = "expenses.json"

def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


# ****** function to load the expenses *********
def load_expenses():
    global expenses
    try:
        with open(DATA_FILE, "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []


def main():
    load_expenses()
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()