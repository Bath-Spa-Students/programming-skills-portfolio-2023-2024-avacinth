# Create a List

sandwich_orders = ["ham", "cheese", "egg", "chicken", "nutella"]

# Empty list to store the sandwich orders

finished_sandwich = []

# Loop of list of sandwich orders

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwich.append(order)

# Printing the list of finished sandwiches

print("\nList of finished sandwiches: ")
for sandwich in finished_sandwich:
    print(sandwich.title() + " is done.")