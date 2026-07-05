weight = float(input("Enter weight (kg): "))
height_cm = float(input("Enter height (cm): "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

bmi = round(bmi, 1)

print("\n BMI Result")
print("BMI:", bmi)