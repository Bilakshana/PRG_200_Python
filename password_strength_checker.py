# Password Strength Checker
password = input("Enter your password: ")

special = "!@#$%^&*"

upper = False
lower = False
digit = False
special_char = False

for ch in password:

    if ch.isupper():
        upper = True

    elif ch.islower():
        lower = True

    elif ch.isdigit():
        digit = True

    elif ch in special:
        special_char = True

print()

if len(password) < 8:
    print("- Must be at least 8 characters")

if upper == False:
    print("- Missing uppercase letter")

if lower == False:
    print("- Missing lowercase letter")

if digit == False:
    print("- Missing digit")

if special_char == False:
    print("- Missing special character")

if len(password) >= 8 and upper and lower and digit and special_char:
    print("Strong Password")
else:
    print("Weak Password")