import sys
from bisect import bisect_left


# https://docs.python.org/3/library/bisect.html
# bisect_left(a, x, lo=0, hi=len(a), *, key=None) 
# 

def lis_indices(seq): #longest increasing subsequence with indicies 
    """Return indices of one longest strictly-increasing subsequence"""
    
    if not seq:
        return []

    tails = []              # tails[v]  is the value of last element of a LIS of length v+1
    tails_idx = []          # tails_idx[v] is the  index in seq of that tail
    parent = [-1]*len(seq)  # parent[i] is the previous index in the LIS that ends at i

    for i, x in enumerate(seq):
        # position where x would go in the current tails array
        
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[pos]  = x
            tails_idx[pos] = i

        # link to predecessor if it exists
        parent[i] = tails_idx[pos-1] if pos > 0 else -1

    # now we reconstruct LIS by following parent links from last tail
    k = tails_idx[-1]
    lis = []
    while k != -1:
        lis.append(k)
        k = parent[k]
    lis.reverse()
    return lis            # list of indices

def solve() -> None:
    out_lines = []
    # iterate over each stdin line
    for line in sys.stdin:
        line = line.strip()
        if not line:            # skip blank lines (rare in Kattis, but harmless)
            continue
        n = int(line)           # first line of test case
        # second line: n integers (we assume they are on a single line)
        seq = list(map(int, sys.stdin.readline().split()))
        idx = lis_indices(seq)
        out_lines.append(str(len(idx)))
        out_lines.append(" ".join(map(str, idx)))

    sys.stdout.write("\n".join(out_lines))


solve()
