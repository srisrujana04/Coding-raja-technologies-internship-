import pickle
income = 0
expenses = []
categories = {}

def main():
    load_data()  
    while True:
        print("Budget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. View Remaining Budget")
        print("5. Save and Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            view_budget()
        elif choice == "5":
            save_data()
            break
        else:
            print("Invalid choice. Please try again.")

def add_income():
    global income
    amount = float(input("Enter income amount: "))
    income += amount

def add_expense():
    global income
    global expenses
    global categories
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses.append((category, amount))
    income -= amount
    categories[category] = categories.get(category, 0) + amount

def view_expenses():
    global expenses
    for category, amount in expenses:
        print(f"Category: {category}, Amount: {amount}")

def view_budget():
    global income
    global expenses
    remaining_budget = income - sum(amount for _, amount in expenses)
    print(f"Remaining Budget: {remaining_budget}")

def save_data():
    global income
    global expenses
    global categories
    data = {
        "income": income,
        "expenses": expenses,
        "categories": categories,
    }
    with open("budget_data.pkl", "wb") as file:
        pickle.dump(data, file)

def load_data():
    global income
    global expenses
    global categories
    try:
        with open("budget_data.pkl", "rb") as file:
            data = pickle.load(file)
            income = data["income"]
            expenses = data["expenses"]
            categories = data["categories"]
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    main()