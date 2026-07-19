orders = []

number_of_orders = int(input("Enter number of orders: "))


for i in range(number_of_orders):
    order_id = input("Enter order ID: ")
    delivery_time = int(input("Enter delivery time in minutes: "))

    orders.append((order_id, delivery_time))


orders.sort(key=lambda order: order[1])


print("\nOrders sorted by delivery time:")

for order in orders:
    print("Order ID:", order[0], "| Delivery Time:", order[1], "minutes")