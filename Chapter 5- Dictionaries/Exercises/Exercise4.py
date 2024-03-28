# Dictionaries

river = {
    'Nile': 'Egypt',
    'Amazon': 'Colombia',
    'Yangtze': 'China',
    'Mississippi': 'United States',
    'Volga': 'Russia'
}

# Loop to print a sentence about each river

for river_name, country in river.items():
        print("\nThe " + river_name.title() + " flows through " + country.title() + ".")

# Loop to print the name of each river

print("\nList of rivers:")
for river_name in river.keys():
    print("- " + river_name.title())

# Loop to print the name of each country

print("\nList of rivers:")
for country_name in river.values():
    print("- " + country_name.title())