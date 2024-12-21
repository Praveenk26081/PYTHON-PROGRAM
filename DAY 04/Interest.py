principal = float(input("Enter the principal amount: "))
years = float(input("Enter the no of years: "))
is_senior = input("Is customer senior citizen (y/n): ").strip().lower()
if principal <= 0 or years <= 0:
    print("Error: Principal and years must be greater than 0.")
else:
    rate_of_interest = 12 if is_senior == 'y' else 10
    interest = (principal * years * rate_of_interest) / 100
    print("Interest:", interest)
