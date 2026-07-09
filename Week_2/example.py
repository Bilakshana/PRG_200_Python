age = int(input("Enter your age: "))

if age < 18:
    print("Sorry! You are not eligible to watch this movie.")
else:
    print("You are eligible to watch this movie.")

    while True:
        tickets = int(input("How many tickets do you want? "))

        for i in range(tickets):
            print(f"Ticket {i + 1} booked successfully!")

        choice = input("Do you want to book more tickets? (yes/no): ").lower()

        if choice != "yes":
            break

    print("Thank you for visiting!")