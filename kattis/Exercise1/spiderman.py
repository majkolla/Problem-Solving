def solve():
    import math
    
    N = int(input().strip())  # Number of test scenarios
    
    for _ in range(N):
        M = int(input().strip())
        distances = list(map(int, input().split()))
        
        # Sum of distances is the maximum possible height
        sum_d = sum(distances)
        
        # dp[i][h] = minimum max height achievable reaching height h after i steps
        # If impossible, dp[i][h] = None
        dp = [[None]*(sum_d+1) for _ in range(M+1)]
        
        # direction[i][h] = 'U' or 'D' indicating whether we arrived at (i,h) by going up or down.
        direction = [[None]*(sum_d+1) for _ in range(M+1)]
        
        # Start at step=0, height=0 with max height 0
        dp[0][0] = 0
        
        for i in range(M):
            d = distances[i]
            for h in range(sum_d+1):
                if dp[i][h] is None:
                    continue  # can't be at height h at step i
                
                current_max = dp[i][h]
                
                # Option 1: Go up (U) -> new height = h + d
                up_h = h + d
                if up_h <= sum_d:
                    new_max = max(current_max, up_h)
                    if dp[i+1][up_h] is None or new_max < dp[i+1][up_h]:
                        dp[i+1][up_h] = new_max
                        direction[i+1][up_h] = 'U'
                
                # Option 2: Go down (D) -> new height = h - d (must not go below 0)
                down_h = h - d
                if down_h >= 0:
                    # Going down does not exceed the previous max any further than h already did
                    # but we must ensure we consider the fact that the current height h might 
                    # already be part of the "max so far".
                    new_max = max(current_max, h)
                    if dp[i+1][down_h] is None or new_max < dp[i+1][down_h]:
                        dp[i+1][down_h] = new_max
                        direction[i+1][down_h] = 'D'
        
        # Check the minimal maximum height if we end at height 0 after M steps
        if dp[M][0] is None:
            print("IMPOSSIBLE")
            continue
        
        # Reconstruct the path of U/D by backtracking from (M, 0)
        path = []
        h = 0  # final height
        for i in range(M, 0, -1):
            move = direction[i][h]
            path.append(move)
            d = distances[i-1]
            if move == 'U':
                # we came to h from (h - d)
                h = h - d
            else:
                # we came to h from (h + d)
                h = h + d
        
        # path is reversed, so reverse it back
        path.reverse()
        
        print("".join(path))
solve()