# Empty list to store the pets

pets = []

# Dictiionaries for different pets

pet = {
    'Name': 'Casper',
    'Animal type': 'Maltese',
    'Owner': 'Ava'
}
pets.append(pet)

pet = {
    'Name': 'Kuma',
    'Animal type': 'Pomeranian',
    'Owner': 'Jennie'
}
pets.append(pet)

pet = {
    'Name': 'Love',
    'Animal type': 'Doberman',
    'Owner': 'Lisa'
}
pets.append(pet)

# Loop the list and print the information of each pet

for pet in pets:
    print("\nWhat I know about " + pet['Name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))