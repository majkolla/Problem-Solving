import math

def solve():
    N = int(input().strip())        # even number of trees
    L, W = map(int, input().split())
    positions = [int(input().strip()) for _ in range(N)]
    
    # Sort the original left-side drop positions
    positions.sort()
    
    # Compute the x-coordinates for the final pairs.
    # We have N/2 pairs, from x=0 to x=L, equally spaced.
    half = N // 2
    if half == 1:
        # sionce N \leq 4 the edge case N=2 wont be a problem 
        xcoords = [0]
    else:
        spacing = L / (half - 1)
        xcoords = [j * spacing for j in range(half)]
    
    # Set up the DP array: dp[i][l] = minimal total distance
    # after placing i trees, with l of them on the left.
    #  (N+1) x (half+1).
    INF = float('inf')
    dp = [[INF]*(half+1) for _ in range(N+1)]
    dp[0][0] = 0.0  # no trees placed, no distance
    
    for i in range(N):
        for l in range(half+1):
            if dp[i][l] == INF:
                continue  # not reachable
            # current cost so far
            cost_so_far = dp[i][l]
            # index of the next tree on the right side
            r = (i - l)  # how many have gone right so far
            
            # Option 1: put the i-th tree on the left side (if possible)
            if l < half:
                # new cost
                dx_left = positions[i] - xcoords[l]
                # distance from (positions[i], 0) to (xcoords[l], 0)
                dist_left = abs(dx_left)  
                cand = cost_so_far + dist_left
                if cand < dp[i+1][l+1]:
                    dp[i+1][l+1] = cand
            
            # Option 2: put the i-th tree on the right side (if possible)
            if r < half:
                # distance from (positions[i], 0) to (xcoords[r], W)
                dx_right = positions[i] - xcoords[r]
                dist_right = math.sqrt(dx_right*dx_right + W*W)
                cand = cost_so_far + dist_right
                if cand < dp[i+1][l]:
                    dp[i+1][l] = cand
    
    # The answer is dp[N][half], if we placed exactly half on the left.
    answer = dp[N][half]
    
    # Print with required precision error up to 1e-6.
    print(f"{answer:.9f}")
solve()