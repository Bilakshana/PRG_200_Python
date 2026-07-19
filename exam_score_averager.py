def average_score(*marks):
    if len(marks) == 0:
        return "No marks provided"

    average = sum(marks) / len(marks)

    return average


number_of_subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(number_of_subjects):
    score = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(score)


result = average_score(*marks)

print("Average score:", result)