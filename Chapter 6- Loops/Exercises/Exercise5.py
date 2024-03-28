# Create a List

sandwich_orders = ["pastrami", "cheese", "pastrami", "chicken", "meatball", "tuna", "chicken", "pastrami"]

# Empty list to store the sandwich orders

finished_sandwich = []

# Message saying the deli has run out of pastrami

print("Sorry, the deli has run out of pastrami.")

# Using a while loop to remove all occurences of pastrami

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop of list of sandwich orders

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwich.append(order)

# Printing the list of finished sandwiches

print("\nList of finished sandwiches: ")
for sandwich in finished_sandwich:
    print(sandwich.title() + " is done.")