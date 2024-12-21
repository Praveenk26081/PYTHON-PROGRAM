def count_factors(n):
    if n <= 0:
        return "Please enter a positive integer."
    
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1 if i == n // i else 2
    return count

# Sample Input and Output
n = int(input("Enter a positive integer: "))
result = count_factors(n)
print(f"The number of factors of {n} is: {result}")
