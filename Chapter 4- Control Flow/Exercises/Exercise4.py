# Input from the user

age = int(input("Input your age: "))

# If-elif-else statement

if age < 2:
    print ('The person is a baby.')
elif age < 4:
    print ('The person is a toodler.')
elif age < 13:
    print ('The person is a kid.')
elif age < 20:
    print ('The person is a teenager.')
elif age < 65:
    print ('The person is a adult.')
else:
    print ('The person is a elder.')