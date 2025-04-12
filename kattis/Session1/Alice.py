import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])  # number of test cases
    idx = 1
    
    answers = []
    for _ in range(t):
        n = int(input_data[idx]); idx+=1
        m = int(input_data[idx]); idx+=1
        A = list(map(int, input_data[idx:idx+n]))
        idx += n
        print(A)

        p = [0]*(n+1)
        for i in range(n):
            p[i+1] = p[i] + A[i]
        
        max_sum = 0
        
        # We'll split the array into segments separated by values < m.
        start = 0
        while start < n:
            # Skip over elements < m
            if A[start] < m:
                start += 1
                continue
            
            # Now A[start] >= m, so find the end of this segment
            seg_start = start
            while start < n and A[start] >= m:
                start += 1
            seg_end = start - 1  # inclusive
            
            # Gather positions of m in this segment
            # (we only consider [seg_start..seg_end])
            positions_of_m = []
            for i in range(seg_start, seg_end+1):
                if A[i] == m:
                    positions_of_m.append(i)
            
            # If there are no m's, we can't form a valid subarray here
            if not positions_of_m:
                continue
        
            positions_of_m = [seg_start-1] + positions_of_m + [seg_end+1]
            
            # For each *actual* m inside, compute the best subarray that includes that m
            for j in range(1, len(positions_of_m)-1):
                left_bound = positions_of_m[j-1] + 1
                right_bound = positions_of_m[j+1] - 1
                # subarray sum = p[right_bound+1] - p[left_bound]
                sub_sum = p[right_bound+1] - p[left_bound]
                if sub_sum > max_sum:
                    max_sum = sub_sum
        
        answers.append(str(max_sum))
    
    # Print all results
    print("\n".join(answers))
solve()