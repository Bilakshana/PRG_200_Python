salary = float(input("Enter monthly basic salary: "))

bonus = salary


deduction_rate = 0.10
deduction = bonus * deduction_rate

take_home = bonus - deduction

print("\n Dashain Bonus Report")
print("Basic Salary:", salary)
print("Bonus (1 month):", bonus)
print("Deduction (10%):", deduction)
print("Take-home Bonus:", take_home)