def solve():
    # Read N
    N = int(input())
    
    # Read the array A
    A = [int(input()) for _ in range(N)]
    
    # pos[x] = 1-based position of number x in A
    pos = [0]*(N+1)
    for i in range(N):
        pos[A[i]] = i+1  # store where each value is located
    
    # Fenwick (BIT) array for positions 1..N
    fenw = [0]*(N+1)
    
    # Fenwick helpers
    def fenw_add(i, val):
        while i <= N:
            fenw[i] += val
            i += i & -i
    
    def fenw_sum(i):
        # Returns sum in range 1..i
        s = 0
        while i > 0:
            s += fenw[i]
            i -= i & -i
        return s
    
    # Initialize Fenwick tree so that each position has value 1
    # (meaning "active")
    for i in range(1, N+1):
        fenw_add(i, 1)
    
    # We'll remove numbers in "turbosort" order over N phases:
    #   Phase i odd  => move the smallest unused (i.e. (i+1)//2),
    #                   cost is rank(pos[x]) - 1
    #   Phase i even => move the largest unused (N - i//2 + 1),
    #                   cost is (total_active - rank(pos[x]))
    # Then we fenw_add(pos[x], -1) to mark that position inactive.
    
    total_active = N
    answers = []
    for i in range(1, N+1):
        if i % 2 == 1:
            # Odd phase -> next smallest number
            x = (i + 1) // 2
            r = fenw_sum(pos[x])      # rank of pos[x] among active
            cost = r - 1
        else:
            # Even phase -> next largest number
            x = N - (i // 2) + 1
            r = fenw_sum(pos[x])
            cost = total_active - r
        
        # Deactivate this position
        fenw_add(pos[x], -1)
        total_active -= 1
        
        answers.append(str(cost))
    
    # Output the results
    print("\n".join(answers))
solve()