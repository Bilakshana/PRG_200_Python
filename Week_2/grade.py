# # Report of 20 students
# for i in range(20):
#     print(f"\nStudent {i + 1}")

#     name = input("Enter your name: ")
#     marks = int(input(f"Enter marks for {name}: "))

#     if marks > 100 or marks < 0:
#         print("Invalid marks! Please enter marks between 0 and 100.")

#     elif marks >= 90:
#         print(f"Congratulations, {name}! You got Distinction.")

#     elif marks >= 75:
#         print(f"Excellent, {name}! You got First Division.")

#     elif marks >= 60:
#         print(f"Good, {name}! You got Second Division.")

#     elif marks >= 35:
#         print(f"{name}, you got Third Division.")

#     else:
#         print(f"Sorry, {name}. You failed. Try hard next time.")

names = []
marks_list = []

for i in range(20):
    print(f"\nStudent {i + 1}")

    name = str(input("Enter your name: "))

    while True:
        marks = int(input("Enter your marks: "))

        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")

    names.append(name)
    marks_list.append(marks)

    if marks >= 90:
        print(f"Congratulations, {name}! You got Distinction.")
    elif marks >= 75:
        print(f"Excellent, {name}! You got First Division.")
    elif marks >= 60:
        print(f"Good, {name}! You got Second Division.")
    elif marks >= 35:
        print(f"{name}, you got Third Division.")
    else:
        print(f"Sorry, {name}. You failed. Try hard next time.")

print("\n----- Student Report -----")

for i in range(len(names)):
    print(f"Student {i + 1}: {names[i]} - {marks_list[i]} marks")