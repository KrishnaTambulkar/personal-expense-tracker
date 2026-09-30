expenses = []


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = (amount, category, description)
    expenses.append(expense)

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- ALL EXPENSES -----")

    for expense in expenses:
        print("Amount:", expense[0],
              "| Category:", expense[1],
              "| Description:", expense[2])


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense[0]

    print("Total Expense:", total)


def category_expense():
    categories = {}

    for expense in expenses:
        category = expense[1]
        amount = expense[0]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n----- CATEGORY WISE EXPENSE -----")

    for category, amount in categories.items():
        print(category, ":", amount)


while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Category-wise Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_expense()
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice!")
