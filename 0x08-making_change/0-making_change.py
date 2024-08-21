#!/usr/bin/python3
"""
Script determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins
    # needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: No coins are needed to make 0 total

    # Iterate over each coin
    for coin in coins:
        # For each coin, update the dp list for all amounts greater
        # than or equal to the coin's value
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we couldn't
    # make the amount with the given coins
    return dp[total] if dp[total] != float('inf') else -1
