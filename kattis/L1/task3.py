"""
Longest Increasing Subsequence 

Given one or more integer sequences we are supposed to 
compute an increasing subsequence of maximum possible
length and then we output

- the length of that subsequence
- the indices of its elements, in the increasing order


Michael Birtman micbi949

----- improvements: 

the idea is to go through the seq. and keep the info of the best increasing seq we seen
up to that point. 

tails_val[k] - smallest possible end val of any increasing subseq. of len k+1
tails_index  - index of the orginal array where the end val is 
pred[i] - idx of the prev. elemetn in the subseq. that ends at pos i. 


For each element x at i we do: 
find bisect left, the first position in tails val where cx could be placed 
while keeping tails_val sorted 

if pos = current length of tails_value, we extend the
subseq. by one => append x

if pos > 0 the previous element of i is the index stored in tail_index[pos-1] 
bc. the idx ends at an optimal subseq. with len pos that x extends to len pos +1. 

finally:
the len of tails_val is the len of a LIS 
the laöst idx of that LIS is tail_index[-1] 
and then we reconstruct the LIS idxs by doing pred[] backwards from last idx and 
reversing the indxs we got.  
"""
import bisect # a module that does binary search (https://docs.python.org/es/3.13/library/bisect.html)
import sys



def lis(seq: list[int]) -> list[int]:
    """
    Returns one of the longest increasing subsequence of seq,
    represented as the list of based indices pointing into seq.

    time complexity  : O(n log n)
    memory : O(n)
    """
    n = len(seq)

    tails_value: list[int] = []
    tails_index: list[int] = []

    pred = [-1] * n # index of the elelemnt before i in the best current seq 

    for i, x in enumerate(seq):
        pos = bisect.bisect_left(tails_value, x)
        if pos == len(tails_value):
            tails_value.append(x)
            tails_index.append(i)
        else:
            tails_value[pos] = x
            tails_index[pos] = i

        if pos:                        
            pred[i] = tails_index[pos - 1]

    # Reconstruct lis using backtracking
    if tails_index: 
        k = tails_index[-1]
    else: 
        -1
    result: list[int] = []
    
    
    while k != -1:
        result.append(k)
        k = pred[k]
    
    
    result.reverse()
    return result


def solve():
    """
    Solve with sys library for the 
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return

    out_lines: list[str] = []
    ptr = 0
    while ptr < len(data): 
        n = int(data[ptr])
        ptr += 1
        seq = list(map(int, data[ptr: ptr + n]))
        ptr += n

        idxs = lis(seq)
        out_lines.append(str(len(idxs)))
        out_lines.append(" ".join(map(str, idxs)))

    sys.stdout.write("\n".join(out_lines))

solve()