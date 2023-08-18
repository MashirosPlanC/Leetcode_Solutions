# Initiate and Iterate

# Bottom-up or Top-down

# Template 1: Fibonacci sequence (1 dimensions DP)
''' 
A fibonacci sequence is expressed as 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
where each number is the sum of the two preceding numbers  
Return Nth Fibonacci number

Example:
fib(19) = 4181
'''
def fib(n: int):
    #initiate
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    #iterate
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n] if n >= 2 else dp[1] if n == 1 else dp[0]

# Template 2: 2 dimensions DP
'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
'''
