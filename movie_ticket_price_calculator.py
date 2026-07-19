def ticket_price(seat_type, count):
    if seat_type.lower() == "regular":
        price = 200
    elif seat_type.lower() == "recliner":
        price = 500
    else:
        return "Invalid seat type"

    total_cost = price * count
    return total_cost


seat = input("Enter seat type (Regular/Recliner): ")
number_of_tickets = int(input("Enter number of tickets: "))

cost = ticket_price(seat, number_of_tickets)

print("Total ticket cost:", cost)