# CMPS 2200 Assignment 5
## Answers

**Name:** Ella Moses


Place all written answers from `assignment-05.md` here for easier grading.




- **1a.**

Find the most valuable coin, largest power of 2, that is less than or equal to N. Subtract the value of that coin from N and repeat the process until zero is reached. Keep track of the coins used. 

Start with value N and an empty list of coins

While N > 0
    coin_value = largest power of 2 less than or equal to N
    add coin with value coin_value to list of coins
    N - coinvalue

At the end of the algorithm N is 0, return the list of coins to see how many coins and what values are necessary to make correct change. 

- **1b.**

 The optimal substructure property states that the optimal solution can be constructed from optimal solutions of smaller subproblems. This is true for this algorithm because the optimal solution for N is a set of coins C with the largest coin being C1, the subproblem of N - the value of C1 has the solution C without the first element. So, if we combine the results of these two subproblems, we get the optimal solution.

The greedy choice property states that a greedy choice must be in some optimal solution (of a given size). Let G1-Gn be the coins in the greedy solution and O1-On be the coins in the optimal solution. Let i be the first index where the values in G and O differ. Assume that Gi < Oi. If G is not the optimal solution but we can replace a value in O with a value in G and make the total value smaller, then the original O was not optimal. This contradicts the idea that G is not equal to the optimal solution therefore G is equal to the optimal solution.  


- **1c.**

The work is O(nlogn) and span is O(n)


- **2a.**

Say a bank has the denominations {1,3,4,5} and we need to make change for 7. Using the greedy alorigthm from problem 1, we should take the most valuable denomination not exceeding N, in this case 5, and subtract it from 7. Now we have 2 remaining. Repeating this process, the most valuable coin not exceeding 2 is 1 so we subtract 1 from 2 and end up with 1. Repeat again to get to 0. This greedy algorithm results in us using 3 coins, {1,1,5} to make change for 7. This is not the optimal algorithm because it does not result in the optimal solution of 2 coins {3,4}. 


- **2b.**

The optimal substructure property states that the optimal solution can be constructed from optimal solutions of smaller subproblems. This is true for this algorithm because the optimal solution for N is a set of coins C with the largest coin being C1, the subproblem of N - the value of C1 has the solution C without the first element. So, if we combine the results of these two subproblems, we get the optimal solution.



- **2c.**


define a minimum coins function:

starting value of min coins is inf

While N > 0:
for each denomination (Di) that is less than or equal to N:
minimum_coins = min(minimum_coins, minimum_coins_fucntion(N-Di))


The work and span are both O(n)


