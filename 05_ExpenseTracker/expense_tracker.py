import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            expenses = json.load(file)
            return expenses if isinstance(expenses, list) else []
    except (json.JSONDecodeError, OSError):
        print("Could not read saved expenses. Starting with an empty list.")
        return []


def save_expenses(expenses):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def get_amount():
    while True:
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                raise ValueError
            return round(amount, 2)
        except ValueError:
            print("Enter a positive number, for example 12.50.")


def add_expense(expenses):
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    category = input("Category: ").strip().title() or "Other"
    amount = get_amount()
    expense = {
        "id": max((item["id"] for item in expenses), default=0) + 1,
        "date": date.today().isoformat(),
        "description": description,
        "category": category,
        "amount": amount,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nID  Date         Category        Description                 Amount")
    print("-" * 70)
    for expense in expenses:
        print(
            f'{expense["id"]:<3} {expense["date"]:<12} '
            f'{expense["category"]:<15} {expense["description"][:27]:<27} '
            f'${expense["amount"]:>8.2f}'
        )


def show_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)
    by_category = {}
    for expense in expenses:
        category = expense["category"]
        by_category[category] = by_category.get(category, 0) + expense["amount"]

    print(f"\nTotal expenses: ${total:.2f}")
    print("By category:")
    for category, amount in sorted(by_category.items()):
        print(f"- {category}: ${amount:.2f}")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)
    try:
        expense_id = int(input("Enter the ID to delete: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense deleted successfully.")
            return

    print("No expense found with that ID.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show summary")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
