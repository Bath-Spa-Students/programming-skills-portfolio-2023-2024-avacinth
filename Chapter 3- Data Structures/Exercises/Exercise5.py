# Change Guest List

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