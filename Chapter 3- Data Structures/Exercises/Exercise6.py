# Shrinking Guest List

# List inviting people to dinner
guests_name = ['Jennie Kim', 'Rose Park', 'Jisoo Kim']

# List index + message
print(guests_name[0] + ", I would like to invite you to dinner.")

print(guests_name[1] + ", I would like to invite you to dinner.")

print(guests_name[2] + ", I would like to invite you to dinner.")

guest = guests_name[1]
print("\nSorry, " + guest + " can't make it to dinner.")

# Changing the guest list
del(guests_name[1])
guests_name.insert(1, 'Lisa Monoban')

# Updated invites
print("\n" + guests_name[0] + ", I would like to invite you to dinner.")

print(guests_name[1] + ", I would like to invite you to dinner.")

print(guests_name[2] + ", I would like to invite you to dinner.")

# String variable
print("Sorry, we can only invite two people to dinner.\n")

# Removing guests
while len(guests_name) > 2:
    name = guests_name.pop()
    print("Sorry, " + name + " there's no room at the table.")

# Printing a message they are still invited
for name in guests_name:
    print(name + ", you are still invited to dinner.")

# Empty out the list
del(guests_name[0])
del(guests_name[0])

# Prove the list is empty
print("\nProof we have an empty list:")
print(guests_name)