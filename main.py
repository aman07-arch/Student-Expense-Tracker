import json
transactions = []
budget = 0
def load_data():
    global transactions, budget
    try:
        f = open("expenses.json", "r")
        data = json.load(f)
        f.close()
        transactions = data["transactions"]
        budget = data["budget"]
    except:
        transactions = []
        budget = 0
def save_data():
    data = {"transactions": transactions, "budget": budget}
    f = open("expenses.json", "w")
    json.dump(data, f)
    f.close()
def add_transaction():
    kind = input("Type (expense/income): ").lower()
    if kind != "expense" and kind != "income":
        print("Invalid type")
        return
    date = input("Date (DD-MM-YYYY): ")
    category = input("Category: ").lower()
    try:
        amount = float(input("Amount: "))
    except:
        print("Amount must be a number")
        return
    if amount <= 0:
        print("Amount must be greater than 0")
        return
    description = input("Description: ")
    item = {"type": kind, "date": date, "category": category, "amount": amount, "description": description}
    transactions.append(item)
    save_data()
    print("Saved successfully")
def view_transactions():
    if len(transactions) == 0:
        print("No transactions yet")
        return
    print("No  Type     Date        Category     Amount     Description")
    count = 1
    for t in transactions:
        print(count, " ", t["type"], " ", t["date"], " ", t["category"], " ", t["amount"], " ", t["description"])
        count = count + 1
def delete_transaction():
    view_transactions()
    if len(transactions) == 0:
        return
    try:
        num = int(input("Enter number to delete: "))
    except:
        print("Enter a valid number")
        return
    if num < 1 or num > len(transactions):
        print("Number out of range")
        return
    transactions.pop(num - 1)
    save_data()
    print("Deleted successfully")
def set_budget():
    global budget
    try:
        value = float(input("Enter your total budget: "))
    except:
        print("Budget must be a number")
        return
    if value < 0:
        print("Budget cannot be negative")
        return
    budget = value
    save_data()
    print("Budget updated")
def get_totals():
    spent = 0
    earned = 0
    for t in transactions:
        if t["type"] == "expense":
            spent = spent + t["amount"]
        else:
            earned = earned + t["amount"]
    return spent, earned
def show_summary():
    spent, earned = get_totals()
    remaining = budget + earned - spent
    print("Total spending:", spent)
    print("Total income:", earned)
    print("Budget:", budget)
    print("Remaining budget:", remaining)
    if remaining < 0:
        print("Warning: you are over budget!")
def show_category_totals():
    totals = {}
    for t in transactions:
        if t["type"] == "expense":
            cat = t["category"]
            if cat in totals:
                totals[cat] = totals[cat] + t["amount"]
            else:
                totals[cat] = t["amount"]
    if len(totals) == 0:
        print("No expenses yet")
        return
    print("Category-wise spending:")
    for cat in totals:
        print(cat, ":", totals[cat])
def main():
    load_data()
    print("Welcome to Personal Expense & Budget Tracker")
    while True:
        print("")
        print("1. Add expense/income")
        print("2. View all transactions")
        print("3. Set budget")
        print("4. Show summary")
        print("5. Show category totals")
        print("6. Delete a transaction")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            show_category_totals()
        elif choice == "6":
            delete_transaction()
        elif choice == "7":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")
main()