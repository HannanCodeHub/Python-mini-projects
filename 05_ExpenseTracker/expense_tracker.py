import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    expense = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSES =====")

    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"Amount: {expense['amount']:.2f} | "
            f"Category: {expense['category']} | "
            f"Description: {expense['description']} | "
            f"Date: {expense['date']}"
        )


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        expense_id = int(input("\nEnter expense ID to delete: "))
    except ValueError:
        print("Invalid ID!")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense deleted successfully!")
            return

    print("Expense not found.")


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: {total:.2f}")


def show_category_total(expenses):
    if not expenses:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    print("\n===== CATEGORY TOTALS =====")

    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total")
        print("5. Category-wise Total")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            delete_expense(expenses)

        elif choice == "4":
            show_total(expenses)

        elif choice == "5":
            show_category_total(expenses)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()