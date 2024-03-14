# Integer variable

usb_price = 6
budget = 50

'''USB sticks she can buy
    Budget divided by the usb price '''
can_buy = budget // usb_price

# Pounds she wil have left
remaining_budget = budget % usb_price

# Results
print("The girl can buy", can_buy, "USB sticks.")
print("She will have £", remaining_budget, "left.")