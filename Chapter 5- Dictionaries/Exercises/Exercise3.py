# Dictionaries

glossary = {
    'Variables': 'It is a container where data values are stored.',
    'String': 'Is a sequence of characters enclosed within quotes.',
    'List': 'Is a mutable and ordered collection of items inside a square brackets.',
    'Integer': 'Is a data type that represents a whole number and not a fractional number.',
    'Float': 'Is a data type that represents a number with decimal points.',
    'Boolean': 'Is a data type that is a value of either True or False.',
    'Loop': 'It means repeating a set of instructions until a condition is satisfied.',
    'Dictionaries': 'Is a data structure that store collections of key-value pairs.',
    'String': 'Is a sequence of characters enclosed within a quotation marks.',
    'Function': 'Is a block of code that you can use multiple times to perform a specific task.',
}

# Loop through a dictionary

for word, definition in glossary.items():
    print ("\n" + word + ": " + definition)