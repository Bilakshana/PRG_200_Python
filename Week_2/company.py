companies = []

for i in range(10):
    name = input("Enter company name: ")
    buy = int(input("Enter buying price: "))
    sell = int(input("Enter selling price: "))

    companies.append([name, buy, sell])

print("\nResult")

for company in companies:
    profit = company[2] - company[1]

    print("Company:", company[0])

    if profit > 0:
        print("Profit =", profit)
    elif profit < 0:
        print("Loss =", -profit)
    else:
        print("No Profit No Loss")