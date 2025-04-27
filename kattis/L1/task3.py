import sys
from bisect import bisect_left

"""
an implemetation of list indicies 
"""
# https://docs.python.org/3/library/bisect.html
# bisect_left(a, x, lo=0, hi=len(a), *, key=None) 
# 

#!/usr/bin/env python3
"""Longest increasing subsequence with earliest indices (O(n log n))."""

import sys
from bisect import bisect_left

def lis_indices(seq):
    """Return 0-based indices of ONE LIS, choosing the left-most one if many."""
    if not seq:
        return []

    tails, tails_idx = [], []          # minimum tail value / its index for each length
    parent = [-1] * len(seq)           # link to predecessor in the LIS

    for i, x in enumerate(seq):
        pos = bisect_left(tails, x)    # where would x go?
        if pos == len(tails):          # longer subsequence found
            tails.append(x)
            tails_idx.append(i)
            parent[i] = tails_idx[pos-1] if pos else -1
        elif x < tails[pos]:           # strictly better (smaller) tail → update
            tails[pos] = x
            tails_idx[pos] = i
            parent[i] = tails_idx[pos-1] if pos else -1
        # else: x == tails[pos]  → keep the earlier index already stored

    # reconstruct one LIS by backtracking
    k = tails_idx[-1]
    out = []
    while k != -1:
        out.append(k)
        k = parent[k]
    return out[::-1]                   # earliest indices, strictly increasing order


def main() -> None:
    """Friendlier line-by-line I/O until EOF."""
    out_lines = []
    for line in sys.stdin:             # read first line of every test case
        line = line.strip()
        if not line:
            continue                   # skip blank lines just in case
        n = int(line)
        nums = list(map(int, sys.stdin.readline().split()))
        idx = lis_indices(nums)
        out_lines.append(str(len(idx)))
        out_lines.append(" ".join(map(str, idx)))

    sys.stdout.write("\n".join(out_lines))


main()
