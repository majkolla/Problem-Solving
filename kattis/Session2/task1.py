"""
Idea: 

So assume we have a function largest_prime_fac(x) 
then we have some number of segemts, where the score is the largest_prime_fac(gcd(segment)) 

This means that we get either an decrease or constant gcd(segmet)

lets look at this 
n = 5,  k = 3  
a = [10, 5, 4, 8, 3]

gcd(10,5) = 5 so LPF(5) = 5 which is larger than 3 so we can extend the segment 
gcd(5,4) = 1 LPF(1) = 0 less than 3 so we must cut before 4

So now next segment: 
gcd(4,8) = 4 LPF(4) = 2 less than three so we cannot extend 

last segment is just 3 

"""

import sys
import math 

max_values = 1000000

# first we compute the largest prime factor for all numbers less then the max: 

def lpf() -> list[int]: 
    lpf = [0] * (max_values +1) ## initialize the list, we get constant look up time, 
                                ## by using the index 
    for p in range(2, max_values + 1):
        if lpf[p] == 0: 
            multiple = p 
            while multiple <= max_values: 
                lpf[multiple] = p 
                multiple += p
    return lpf
 
LPF = lpf()

def feasibility(s, lst, k) -> bool: 
    """
    return true if the array can be cut into k segments or less such that
    every segmet gcd has a largest prime factor bigger than s
    """
    segments = 0 
    g = 0 #the gcd of the open segment 

    for x in lst: 
        if g == 0: # start a new seg 
            g = x
        else: 
            new_g = math.gcd(g,x)
            if LPF[new_g] >= s:  #if true we can extend the seg
                g = new_g
            else: 
                segments += 1 
                g = x 
        if LPF[g] < s: 
            return False
    if g: 
        segments += 1
    return segments <= k

def solve_case(lst, k): 
    high = max(LPF[v] for v in lst) #upper bound 
    low = 0 

    while low < high: #do a binary search
        mid = (low + high + 1) // 2 
        if feasibility(mid, lst, k): 
            low = mid 
        else: 
            high = mid - 1
    if low <= 2: 
        return low 
    else:  # we score 0 if no prime larger than 2 is ok
        return 0 

def main():

    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    out_lines = []
    
    while idx < len(data):
        n = int(data[idx]) 
        idx += 1 
        k = int(data[idx + 1]) 
        idx += 1
        lst = list(map(int, data[idx: idx + n]))
        idx += n
        out_lines.append(str(solve_case(lst, k)))
    sys.stdout.write("\n".join(out_lines))
main()
