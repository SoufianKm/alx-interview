#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    if x <= 0 or not nums:
        return None

    # Determine the maximum n in nums
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False

    # Precompute the number of primes up to each i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Precompute if Maria wins for each number up to max_n
    maria_wins_at = [False] * (max_n + 1)
    for i in range(1, max_n + 1):
        if prime_count[i] % 2 == 1:
            maria_wins_at[i] = True

    # Count the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if maria_wins_at[n]:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
