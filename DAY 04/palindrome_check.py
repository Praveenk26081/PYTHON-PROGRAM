x = int(input("Enter an integer: "))
if x < 0:
    print("False")  # Negative numbers are not palindromes
else:
    original = str(x)
    reversed_x = original[::-1]
    if original == reversed_x:
        print("True")
    else:
        print("False")
