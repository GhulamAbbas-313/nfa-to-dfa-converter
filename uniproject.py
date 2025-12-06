labs = {
    'lab7': 'lab 7',
    'lab8': 'lab 8',
    'lab9': 'lab 9',
    'lab10': 'lab 10'
}


# Prompt the user for input
user1 = input("Please enter any lab numbers from (lab7 to lab10): ")

# Check if the input is in the dictionary and print the corresponding output
if user1 in labs:
    print(labs[user1])
else:
    print('Invalid lab number')
