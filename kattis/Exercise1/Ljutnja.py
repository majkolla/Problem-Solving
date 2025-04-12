def solve():
    import bisect
    
    # Read input the usual way
    M, N = map(int, input().split())
    demands = [int(input()) for _ in range(N)]
    
    total_demand = sum(demands)
    R = total_demand - M  # total shortage
    
    # If there's no shortage, nobody is angry
    if R <= 0:
        print(0)
        return
    
    # Sort demands to help with prefix sums and binary search
    demands.sort()
    
    # Build prefix sums of x_i and x_i^2
    prefix = [0] * (N + 1)
    prefix_sq = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + demands[i]
        prefix_sq[i+1] = prefix_sq[i] + demands[i]*demands[i]
    
    # S(k) = sum of min(demands[i], k) for i=1..N
    def S(k):
        idx = bisect.bisect_left(demands, k)
        # All elements before idx are < k, so sum is prefix[idx]
        # All elements from idx..N-1 contribute exactly k each
        return prefix[idx] + k * (N - idx)
    
    # 1) Binary-search the smallest k where S(k) >= R
    left, right = 0, demands[-1]
    while left < right:
        mid = (left + right) // 2
        if S(mid) >= R:
            right = mid
        else:
            left = mid + 1
    k = left
    
    # 2) leftover = how many times we can reduce a child's shortfall 
    #    from k down to (k-1)
    actual_sum = S(k)
    leftover = actual_sum - R
    
    # 3) Compute sum of squares of shortfalls
    #    First, all children with demand < k shortfall their entire demand
    idx = bisect.bisect_left(demands, k)
    sum_squares = prefix_sq[idx]  # those shortfall = demands[i]
    
    # Children with demand >= k shortfall = k each, except 'leftover' 
    # get (k-1) shortfall
    sum_squares += (N - idx) * (k**2)
    sum_squares -= leftover * (2*k - 1)
    
    print(sum_squares)
solve()