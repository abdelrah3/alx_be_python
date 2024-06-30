monthly_income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
MonthlySavings = monthly_income - expenses
Projected_Savings = MonthlySavings * 12 + (MonthlySavings * 12 * 0.05)
print(f"Your monthly savings are {MonthlySavings}")
print(f"Projected savings after one year, with interest 5%, is: {Projected_Savings}")