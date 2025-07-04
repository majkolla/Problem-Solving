"""
Longest Increasing Subsequence 

Given one or more integer sequences we are supposed to 
compute an increasing subsequence of maximum possible
length and then we output

- the length of that subsequence
- the indices of its elements, in the increasing order


Michael Birtman micbi949

"""
import bisect # a module that does binary search (https://docs.python.org/es/3.13/library/bisect.html)
import sys



def lis(seq: list[int]) -> list[int]:
    """
    Return **one** longest increasing subsequence of seq,
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


if __name__ == "__main__":
    solve()
