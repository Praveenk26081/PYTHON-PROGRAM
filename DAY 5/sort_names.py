# Accept a list of names from the user
names = input("Enter names separated by commas: ").split(',')

# Get the sorting order from the user (A for ascending, D for descending)
order = input("Order(A/D): ").upper()

# Sort the names based on user input
if order == 'A':
    names.sort()
elif order == 'D':
    names.sort(reverse=True)

# Print the sorted names
for name in names:
    print(name)
