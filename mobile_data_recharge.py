def recharge_cost(gb, validity_days=30):
    if gb == 1:
        price = 100
    elif gb == 5:
        price = 400
    elif gb == 10:
        price = 700
    else:
        return "Data pack not available"

    return price


data = int(input("Enter data pack size (1GB/5GB/10GB): "))

cost = recharge_cost(data)

print("Recharge cost:", cost)
print("Validity:", 30, "days")