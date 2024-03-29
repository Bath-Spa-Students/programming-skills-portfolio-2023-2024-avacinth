def describe_city(city, country = "Unknown"):
    '''Printing a sentence describing the city and its country.'''
    print(f"{city} is in {country}.")

# Calling the function for different cities
    
describe_city("Amsterdam", "Netherlands")
   
describe_city("Paris", "France")

# Defualt value

describe_city("New York")