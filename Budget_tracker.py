#Here is your budget tracker app

import json

def add_expense(description : str, amount, expenses):
    expenses.append({"description": description, "amount" : amount})
    print(f"Expense added: {description}, for amount {amount}")

def getexpense(expenses):
    sum = 0
    for cash in expenses:
        sum += cash["amount"]
    return sum

def show_expense(expenses, budget):
    for expense in expenses:
        print(f"{expense["description"]} : {expense["amount"]}")
    print(f"Your Total budget is {budget}")
    print("You have spent amount ", getexpense(expenses))
    print(f"Your remaining balance is ", budget - getexpense(expenses))

def get_expense_details(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []
    
def save_expense_details(filepath, initial_budget, expenses):
    data = {
        "initial_budget" : initial_budget,
        "expenses" : expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent= 4)

print("Welcome to Budget Tracker app!")
filepath = 'budget_details.json'
initial_budget, expenses = get_expense_details(filepath)
if initial_budget == 0:
    initial_budget = float(input("Enter your budget "))
budget = initial_budget

while True:
    print("Here are the list of Operations you can perform")
    print("1: Add Expense")
    print("2. Show expenses")
    print("3. Exit")
    choice = input("Enter your choice (1,2,3) ").strip()
    if choice == '1':
        description = input("Enter the expense description: ")
        amount = float(input("Enter the amount: "))
        add_expense(description, amount, expenses)
    elif choice == '2':
        show_expense(expenses, budget)
    elif choice == '3':
        save_expense_details(filepath, initial_budget, expenses)
        print("Thanks for using Budget Tracker App. Good Bye!")
        break
    else:
        print("Invalid Choice")
        break