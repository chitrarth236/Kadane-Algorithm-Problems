#Best Time to Buy and Sell Stock Problem, Leetcode 121.

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

#Time Complexity of the solution: O(n)


def maxProfit(prices):
    maxP = 0
    minV = prices[0]
    for i in range(1,len(prices)):
        currMax = max(maxP,prices[i] - minV)
        if prices[i] < minV:
            minV = prices[i]
        if maxP < currMax:
            maxP = currMax
    return maxP
        
