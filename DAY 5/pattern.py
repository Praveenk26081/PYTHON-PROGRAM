def print_pattern(rows):
    for i in range(1, rows + 1):
        # Print spaces for alignment
        print(" " * (rows - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

# Sample Input and Output
rows = int(input("Enter the number of rows for the pattern: "))
print_pattern(rows)
