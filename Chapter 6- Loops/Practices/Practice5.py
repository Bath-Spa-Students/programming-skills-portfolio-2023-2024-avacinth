# Storing the largest number
largest = float('-inf')

# Input from user to enter numbers until they input '0'
while True:
    number = float(input("Enter a number (0 to exit): "))
    if number == 0:
        break
    largest = max(largest, number)

# Print the largest number
print("The largest number entered is:", largest)