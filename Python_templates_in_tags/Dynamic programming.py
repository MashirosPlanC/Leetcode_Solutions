#Typically, dynamic programming problems can be solved with three main components. 

#First, we need some function or array that represents the answer to the problem from a given state. For many solutions on LeetCode, you will see this function/array named "dp". For this problem, let's say that we have an array dp. As just stated, this array needs to represent the answer to the problem for a given state, so let's say that dp[i] represents the length of the longest increasing subsequence that ends with the ithi^{th}i 
th element. 

#Second, we need a way to transition between states, such as dp[5] and dp[7]. This is called a recurrence relation and can sometimes be tricky to figure out. 

#The third component is the simplest: we need a base case. 


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
120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.
If you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        if n == 1:
            return triangle[0][0]

        dp = [[0] * x for x in range(1, n + 1)]

        for j in range(n):
            dp[n - 1][j] = triangle[n - 1][j]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
        
        return dp[0][0]
