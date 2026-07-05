n = int(input("Enter number of trekkers: "))

total_cost = 0

for i in range(n):
    print(f"\nTrekker {i+1}")

    trekker_type = input("Enter type (Foreign/SAARC): ").lower()

    tims = int(input("Enter TIMS fee: "))
    acap = int(input("Enter ACAP fee: "))

    person_cost = tims + acap

    if trekker_type == "foreign":
        person_cost = person_cost * 1.2
    elif trekker_type == "saarc":
        person_cost = person_cost * 1.0
    else:
        print("Invalid type, assuming SAARC rate.")
        person_cost = person_cost * 1.0

    total_cost += person_cost

service_charge = total_cost * 0.05
final_total = total_cost + service_charge

average_cost = final_total / n

print("TREKKING COST REPORT")
print("Total Cost (before service):", total_cost)
print("Service Charge (5%):", service_charge)
print("Final Total Cost:", final_total)
print("Average Cost per person:", average_cost)