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
    # Read all the input to a list 
    #O(n)
    data = list(map(int, sys.stdin.read().split()))
    i = 0
    out = [] 

    while i < len(data):

        C = data[i] #read the capacity 
        i += 1
        
        n = data[i] #read the number of items 
        i += 1

        # read n (value, weight) also O(n) 
        values = []
        weights = []
    
        for _ in range(n):
            values.append(data[i])
            weights.append(data[i+1])
            i += 2

        dp = [0] * (C + 1)               # create the dp table 

        # create a keep[j][cap] == True which is the same as  item j is used to reach dp[cap]
        keep = [[False]*(C + 1) for _ in range(n)]

        # for each item j scan cap. from C to w_j
        #So we have O(n C)
        for j in range(n):
            v = values[j]
            w = weights[j]
            for cap in range(C, w-1, -1): 
                newv = dp[cap - w] + v
                if newv > dp[cap]:
                    dp[cap] = newv
                    keep[j][cap] = True   # remember that j is taken here

        #reconstruct an optimal solution O(n)
        
        cap = C
        chosen = []

        for j in range(n-1, -1, -1):      #check every item once
            if keep[j][cap]:              # was item j used for this cap
                chosen.append(j)
                cap -= weights[j]         # move to the remaining capacity

        chosen.reverse()                  # put indices in ascending order to get the correct output

        # record the result for the test case O(n)
        out.append(str(len(chosen)))
        out.append(" ".join(str(x) for x in chosen))


    sys.stdout.write("\n".join(out)) #output everything at the same time so we get O(k)


"""
thus we have a solution that is O(n * C) in complexity! 
"""
solve()