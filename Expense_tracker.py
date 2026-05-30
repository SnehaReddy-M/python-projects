food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
shopping = float(input("Enter shopping expense: "))

total = food + travel + shopping

budget = float(input("Enter your budget: "))

print("Total Expense =", total)

if total <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")
