budget = float(input("Enter monthly budget: "))
expenses = 0
moreExpenses = True
while moreExpenses:
    expenses += float(input("Enter expenses: "))
    question = input("Do you have more expenses? (y/n): ")
    if question == "y":
        moreExpenses = True
    else:
        moreExpenses = False
if expenses <= budget:
    print("You are", budget-expenses, "dollars under budget.")
else:
    print("You are", expenses-budget, "dollars over budget.")