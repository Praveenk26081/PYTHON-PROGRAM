def max_profit(prices):
    if not prices:
        return 0

    n = len(prices)
    
    # profit1[i] will hold the maximum profit for one transaction until day i
    profit1 = [0] * n
    # profit2[i] will hold the maximum profit for one transaction from day i to the end
    profit2 = [0] * n

    # Calculate profit1 (maximum profit with one transaction till each day)
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit1[i] = max(profit1[i - 1], prices[i] - min_price)

    # Calculate profit2 (maximum profit with one transaction from each day to end)
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        profit2[i] = max(profit2[i + 1], max_price - prices[i])

    # Now find the maximum profit by considering both profits (profit1 and profit2)
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, profit1[i] + profit2[i])

    return max_profit

# User input for prices
prices = list(map(int, input("Enter the stock prices separated by space: ").split()))

# Output the maximum profit
print("Maximum profit:", max_profit(prices))
