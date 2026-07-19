# Online Store Discount System
purchase = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ")

if purchase < 1000:
    discount = 0

elif purchase < 5000:
    discount = 5

elif purchase < 15000:
    discount = 10

else:
    discount = 20

final_amount = purchase - (purchase * discount / 100)

if member.lower() == "yes":
    final_amount = final_amount - (final_amount * 5 / 100)

print("Final payable amount: NPR", final_amount)