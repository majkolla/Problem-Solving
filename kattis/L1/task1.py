"""
 If we implement a simply greedy alg. here we can do it by: 
 (let S be the set of all intervals [a_i, b_i] and [A,B] is the set we want to cover)
 start with the set that starts at (or before) A and cover the most ground. 

 We first sort the smallest a then the second priority is the biggest b if they have the same a (or the biggest abs(a-b))




"""

import sys 


def cover_interval(A: float, B: float, intervals : list[tuple]) -> list:
    # The tuples are going to have three elements, a_i, b_i and a fix index (from the input)

    intervals = [(a,b,i) for i, (a,b) in enumerate(intervals)]

    # we sort by a if a_i = a_j and i != j we sort by b

    intervals.sort(key = lambda x: (x[0], -x[1])) # sort has a time complexity of O(n log(n)) (it uses Timsort https://en.wikipedia.org/wiki/Timsort)
    result : list = []
    i : int = 0 
    current_point : float = A
    n : int = len(intervals)

    if current_point == B: # in cases where A = B we simply want to find an interval that has that part
        for interval in intervals: 
            if (interval[0] <= B) and (interval[1] >= B): 
                result.append(interval[2])

    while current_point < B:
        best_b : float = -float("inf") #Starting value 
        best_index : int = -1 
        
        while i < n and intervals[i][0] <= current_point: 
            if intervals[i][1] >= best_b: 
                best_b = intervals[i][1]
                best_index = intervals[i][2]
            i += 1 

        if best_b < current_point: 
            return []
        
        result.append(best_index)
        current_point = best_b


    return result

def solve():
    lines = sys.stdin.read().strip().split()
    idx = 0

    while idx < len(lines):
        # Read A, B
        A = float(lines[idx])
        B = float(lines[idx+1])
        idx += 2
        
        # Read n
        n = int(lines[idx])
        idx += 1
        
        intervals = []
        for _ in range(n):
            a = float(lines[idx]) 
            b = float(lines[idx+1])
            
            idx += 2
            intervals.append((a,b))
            
        result = cover_interval(A, B, intervals)
        
        if not result: # reult is empty 
            print("impossible")
        else: 
            print(len(result))
            print(" ".join(map(str, result))) 

solve()


""" 
1) we sort the intervals 
2) The Greedy alg. 

1) this step uses sort() which uses the Timsort alg and is O(nlogn)

2) 
We have an outer loop that continues until the current is equal or larger than (to) B.

Then we have an inner loop:
i starts at 0 and increases, it's never reset thus we get max number of iterationsof inner loop to be nn. 
Thus the inner loop is O(n)

we get O(nlogn) + O(n) = O(nlogn)
"""