# Get inputs
M = int(input("Enter M: "))
N = int(input("Enter N: "))
K = int(input("Enter K: "))

# Generate and print the numbers from M to N, skipping K numbers in between
numbers = list(range(M, N+1, K))
print(", ".join(map(str, numbers)))
