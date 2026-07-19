def estimate_fare(distance_km, vehicle_type, surge=1.0):
    if vehicle_type.lower() == "bike":
        rate = 30
    elif vehicle_type.lower() == "car":
        rate = 60
    else:
        return "Invalid vehicle type"

    fare = distance_km * rate
    final_fare = fare * surge

    return final_fare


distance = float(input("Enter distance in km: "))
vehicle = input("Enter vehicle type (Bike/Car): ")

fare = estimate_fare(distance, vehicle)

print("Final ride fare:", fare)