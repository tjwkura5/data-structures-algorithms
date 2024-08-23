def max_profit(prices):
    max_profit = 0
    profit = 0
    L = 0
    for R in range(len(prices)):
        profit = prices[R] - prices[L]
        if profit < 0:
            L = R
        max_profit = max(profit, max_profit)

    return max_profit

print(max_profit([7,2,3,1,4,5,6]))