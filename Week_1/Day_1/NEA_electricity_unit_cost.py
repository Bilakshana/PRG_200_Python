previous_units = int(input("Enter previous units: "))
recent_units = int(input("Enter recent units: "))

units = recent_units - previous_units

per_unit_rate = 11
service_charge = 0.05 

price = units * per_unit_rate
final_amount = price + (price * service_charge)

print(f"Final amount charged is {final_amount:.2f}")