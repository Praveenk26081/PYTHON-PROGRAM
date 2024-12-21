import itertools

# Accept a 3-digit number as input
num = input("Enter a 3-digit number: ")

# Find all permutations of the digits
combinations = list(itertools.permutations(num))

# Print all combinations
for combo in combinations:
    print("".join(combo))
