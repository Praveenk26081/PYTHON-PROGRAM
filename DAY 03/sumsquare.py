n = int(input("Enter the number of elements: "))
numbers = []
for _ in range(n):
    numbers.append(int(input("Enter the element: ")))
odd_sum = sum(x**2 for x in numbers if x % 2 != 0)
even_sum = sum(x**2 for x in numbers if x % 2 == 0)
print("Output:", [odd_sum, even_sum])
