monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
finance_calculator = monthly_income - monthly_expenses
projected_savings = finance_calculator * 12 + (finance_calculator * 12 * 0.05)
print(f"Your monthly savings are {finance_calculator}")
print(f"Projected savings after one year, with interest 5%, is: {projected_savings}")
