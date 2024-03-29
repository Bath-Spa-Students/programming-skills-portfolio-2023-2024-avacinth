def make_shirt(size = 'large', message = 'I Love Python!'):
    '''Printing a sentence about the size of the shirt and message printed on it.'''
    print(f"Making a shirt of size {size} with the message: '{message}'.")

# Large shirt with a default message
    
make_shirt()

# Medium shirt with a default message
    
make_shirt(size = "Medium")

# Any size shirt with a different message

make_shirt(size = "Small", message = "Look at Me!")