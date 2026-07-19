def build_profile(name, **details):
    print("\nStudent Profile")
    print("Name:", name)

    for key, value in details.items():
        print(key + ":", value)


name = input("Enter student name: ")
program = input("Enter program: ")
semester = input("Enter semester: ")
portfolio = input("Enter portfolio link (optional): ")


build_profile(
    name,
    program=program,
    semester=semester,
    portfolio=portfolio
)