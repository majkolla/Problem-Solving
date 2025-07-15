"""
Michael Birtman micbi949

We can solve the 0/1-knapsack problem with dynamic programming.

basic idea

dp[i][j] = maximum value obtainable using the first i items without exceeding total weight j

We build the table row-by-row:


if we have room for it we do
    dp[i][j] = max( dp[i-1][j], dp[i-1][j-w_i] + v_i )      # skip or take item i 
or we are unable to take it because it's heviear than j 
    dp[i][j] = dp[i-1][j]                       # cannot take item i

After filling the table, we back-track from (n, C) to recover the chosen
indices using backtracking 

Complexities
------------------------------------------
Time:  O(n*C) we fill an (n + 1)*(C + 1) table once.  
Memory: O(n * C)
"""

import sys 

def solve_case(capacity: int, values: list[int], weights: list[int]) -> tuple[int, list[int]]:
    n = len(values)
    # DP table and a parallel keep table to reconstruct the solution
    dp   = [[0]*(capacity + 1) for _ in range(n + 1)]
    keep = [[False]*(capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_i, v_i = weights[i-1], values[i-1]
        for c in range(capacity + 1):
            if w_i <= c and dp[i-1][c - w_i] + v_i > dp[i-1][c]:
                dp[i][c] = dp[i-1][c - w_i] + v_i
                keep[i][c] = True                    # we took item i-1
            else:
                dp[i][c] = dp[i-1][c]                # we did not take item i-1

    # Back-track
    chosen: list[int] = []
    i, c = n, capacity
    while i > 0 and c >= 0:
        if keep[i][c]:
            chosen.append(i-1)
            c -= weights[i-1]
        i -= 1
    chosen.reverse()
    return len(chosen), chosen

def main() -> None:  # parsing 
    data = sys.stdin.read().strip().split()
    idx = 0
    out_lines = []

    while idx < len(data):
        if idx + 1 >= len(data):
            break
        
        C = int(data[idx])
        n = int(data[idx + 1])
        idx += 2
        
        if idx + 2*n > len(data):     
            break

        vals, wts = [], []
        for _ in range(n):
            vals.append(int(data[idx]))
            wts.append(int(data[idx + 1]))
            
            idx += 2

        k, items = solve_case(C, vals, wts)
        out_lines.append(str(k))
        out_lines.append(" ".join(map(str, items)))

    sys.stdout.write("\n".join(out_lines))
    
main()
