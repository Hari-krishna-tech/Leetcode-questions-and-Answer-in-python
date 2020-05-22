"""Coin Change 2
------------------------------
You are given coins of different denominations and a total amount of
money. Write a function to compute the number of combinations that
make up that amount. You may assume that you have infinite number of
each kind of coin.
Note:
You can assume that
 0 <= amount <= 5000
 1 <= coin <= 5000
 the number of coins is less than 500
 the answer is guaranteed to fit into signed 32-bit integer
Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
Input: amount = 10, coins = [10]
Output: 1
--------------------------"""
"""
concept-dynamic programing
//split your amount from o to n
   0   1   2   3    4   5    ...  n  //the amount
       //consider you have only one coin in the beginning
1  1   1   1   1    1   1    ...  1 //you can have only one combinations
 //for 0 it is always 1 combinations 0! = 1 remember
//now you have 1&2 if denominations < coin values copy above value
//if it is greater than or equal than copy the above and add current row[denominations - coin value]
2  1   1   1+1 1+1  1+2 1+2 ...   1+curRow[n-coin value]
          //deno-coin value is 0 its value is 1


3  1   1   2   2+1  3+1 3+2       1+curRow[n-coin value]+curRow[n-coin value]

now the last row last column value is the answer


"""

def no_of_combinations_of_coin(amount,coins):
  grid = [[0]*(amount+1) for i in range(len(coins))]
  for i in range(len(coins)):

    for j in range(amount+1):
      if coins[i] <= amount:
        if (i == 0 or j == 0):
          grid[i][j] = 1
        elif coins[i] > j and coins[i] <= amount:
          grid[i][j] = grid[i-1][j]
        elif coins[i] <= j and coins[i] <= amount:
          grid[i][j] = grid[i-1][j] + grid[i][j-coins[i]]
  
  return grid[len(coins)-1][amount] 


print(no_of_combinations_of_coin(2,[3]))

