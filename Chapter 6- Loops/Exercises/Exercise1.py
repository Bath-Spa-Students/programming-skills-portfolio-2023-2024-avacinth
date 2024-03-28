# Prompt where user will be asked to enter pizza topping

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you're done: "

# Empty list to store toppings

toppings = []

# Loop 

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)  #Adding the topping to the list
    else:
        #Remove the script path from the list of toppings
        if __file__ in toppings:
            toppings.remove(__file__)
        print("\nYour pizza will have the following toppings:")
        for added_topping in toppings:
            print("- " + added_topping)  #Print each added topping
        break