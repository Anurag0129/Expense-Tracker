from datetime import date
import json

expenses = []

# *********  START  *** function to add the expenses*** START ***********
def add_expense():
    category = input("Enter category (e.g. Food, Travel, Rent): ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Expense not added.")
        return

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


# ********* START *** function to delete an expense *** START ***********
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()
    try:
        choice = int(input("\nEnter the row number to delete (1, 2, 3...): "))
        index = choice - 1

        if index < 0 or index >= len(expenses):
            print("Invalid row number.")
            return

        removed = expenses.pop(index)
        save_expenses()
        print(f"Deleted: {removed['category']} - {removed['amount']} ({removed['note']})")

    except ValueError:
        print("Please enter a valid number.")
# ********* END *** function to delete an expense *** END ***********

# ********* START *** function to show summary *** START ***********
def show_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal spent: {total:.2f}")

    category_totals = {}
    for expense in expenses:
        cat = expense["category"]
        category_totals[cat] = category_totals.get(cat, 0) + expense["amount"]

    print("\nSpending by category:")
    for cat, amt in category_totals.items():
        print(f"  {cat:<15} {amt:.2f}")
# ********* END *** function to show summary *** END ***********


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
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()