# Best Time To Buy And Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.


def maxProfit(prices):
    minBuy = float('inf') # track minimum price of stock to buy
    maxProfit = 0 # store the total profit from stock selling
    for i in prices:
        if i < minBuy: # if current price of stock is cheaper from previous then buy on these day
            minBuy = i
        else:
            maxProfit += i - minBuy # else we have profit on selling, then sell it, and register the profit
            minBuy = i # and same day buy the stock
    return maxProfit # return maximum profit earned from it


print(maxProfit([7,1,5,3,6,4]))