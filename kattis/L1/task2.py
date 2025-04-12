"""
We can solve this problem using a dp approach. 
We define a dp[i][j] = "maximum value using the first i items with the capacity j"
So we have rows i that correspond to considering items up to the ith item
And cols j corresponding to the capacity
   

dp[i][j]=maximum possible value using items from 1…i
So we fill the table using this: 
dp[i][j] = max (dp[i-1][j], dp[i-1][j-w_i] + v_i) assuming that w_i \leq j

after we fill out the table we do backtracking to find the the items 

the idea: 
- begin at (n,C) where n = #items and C = capasity
- if dp[i][j] = dp[i-1][j] we know that item i was not chosen 
- if dp[i][j] = dp[i-1][j-w_i] + v_i we know that item i was chosen 
- redo until (i or j) = 0
"""

import sys 

def solve():
    # General parsing 
    data = sys.stdin.read().strip().split()
    data = iter(data) 
    test_cases = int(next(data))

    for _ in range(test_cases):  #solve the problem for each testcase 
        C = int(next(data))
        n = int(next(data))

        weights : list  = [0]

        values : list = [0]



        for _ in range(1, n+1):
            weights.append(int(next(data)))
            values.append(int(next(data)))
        # Create a 2D dp table for the problem with comprehensive list filled with zeroes  
        # Note that we couldve done something similar for weights instead of appending to make the code faster
        # Because then we'd need less memory access 


        dp = [[0] * (C+1) for _ in range(n+1)]
        

        # Fill the dp table! 
        for i in range(1, n+1):
            for j in range(C+1):
                dp[i][j] = dp[i-1][j]
                if weights[i-1] <= j:
                    new_value = dp[i-1][j - weights[i-1]] + values[i-1]
                    if new_value > dp[i][j]:
                        dp[i][j] = new_value

        # Now we've filled the dp and to get the correct solution we need to do the backtracking.   

        items : list = []
        current_capacity = C 
        
        #backwards loop
            # here we compare the current cell with the cell above it
            # If they are different, we know that the i-th item was chosen.
        for i in range(n, 0, -1):
            if dp[i][current_capacity] != dp[i-1][current_capacity]:
                items.append(i)  # or items.append(i-1) depending on your desired output
                current_capacity -= weights[i-1]

        items.reverse()

        #print output: 
        output : list = []

        output.append(str(len(items)))
        output.append(" ".join(map(str, items)))

        sys.stdout.write("\n".join(output))

solve()