# Integer variable

usb_stick_price = 6
budget = 50

# How many USB sticks she can buy
num_usb_sticks = budget // usb_stick_price

# How many pounds she will have left
remaining_budget = budget % usb_stick_price

# Print the results
print("The girl can buy", num_usb_sticks, "USB sticks.")
print("She will have £", remaining_budget, "left.")