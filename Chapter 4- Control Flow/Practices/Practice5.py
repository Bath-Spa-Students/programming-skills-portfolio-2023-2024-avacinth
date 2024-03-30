# Ask user to enter a month
month = int(input("Enter a month (1-12): "))

if month in [3, 4, 5]:  
    print("Spring")  #If the month is March, April, or May
elif month in [6, 7, 8]:
    print("Summer")  #If the month is June, July, or August
elif month in [9, 10, 11]:
    print("Autumn")  #If the month is September, October, or November
else:
    print("Winter")  #If the month is January, February, or December