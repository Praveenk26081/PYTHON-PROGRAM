def is_perfect_number(num):
    """Check if a number is a perfect number."""
    if num < 2:
        return False
    divisors_sum = 1
    for i in range(2, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

def get_first_m_factors(num, m):
    """Get the first m factors of a number."""
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
        if len(factors) == m:
            break
    return factors

def print_perfect_numbers_and_factors(n, m):
    """Print the first n perfect numbers and their first m factors."""
    if n <= 0 or m <= 0:
        print("Both N and M must be positive integers.")
        return

    count = 0
    num = 2

    while count < n:
        if is_perfect_number(num):
            count += 1
            factors = get_first_m_factors(num, m)
            print(f"First {m} factors of {num} are: {', '.join(map(str, factors))}")
        num += 1
5
