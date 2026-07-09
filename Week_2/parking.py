vehicles = []

n = int(input("Enter number of vehicles: "))

for i in range(n):
    number = input("Enter vehicle number: ")
    hours = int(input("Enter parking hours: "))

    fee = hours * 50

    vehicles.append([number, hours, fee])

print("\nVehicle Details")

for v in vehicles:
    print("Vehicle:", v[0])
    print("Hours:", v[1])
    print("Fee: Rs.", v[2])