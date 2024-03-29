amount1 = 11  # Example value for amount1 that is greater than 10
amount2 = 99  # Example value for amount2 that is less than 100

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print("Greater amount:", amount1)
        else:
            print("Greater amount:", amount2)
    else:
        print("amount2 is not less than 100")
else:
    print("amount1 is not greater than 10")