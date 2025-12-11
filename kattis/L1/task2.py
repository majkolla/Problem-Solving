"""
Michael Birtman — micbi949

0/1-Knapsack for Kattis with a 1d dp and pointers.


idea 
for each item i with weight w_i and value v_i
    for all c in C … w_i
        cand = val_at[c - w_i] + v_i
        if cand >  val_at[c]:
            val_at[c]  = cand
            item_at[c] = i
            prev_cap[c] = c - w_i

then we reconsrtuct: 

start at c = C; while item_at[c] is not -1 
    take item = item_at[c]
    c = prev_cap[c]


Complexities
------------
Time   O(n · C)   
Memory O(C)     


I solve this problem by doig an array dp and extra pointers. 
So for some capacity c we have val_at[c], which stores the max val of the subsets of the items 
that we have into the knapsack. We then do: 
for each item i with weight w and val v we loop c backwards from c to w. 

At capacity c we have two options, either choose item i or skip item i. if we skip then we keep 
the old val if we take we then we have previous items beign in the cap. c -w with val [c-w] and 
the new val is val_at[c-w] + v. 

So we just picj the better one. We run backwards loop, so we look at the solutions not contining
the item we're currently looking at.

the dp table will just update and build any solution that fits into the cap. So finally we get 
val_at[C] being the optimal val. 

Then we reconstruct which items we took, so 

    while c >= 0 and item_at[c] != -1:
        i = item_at[c]
        chosen.append(i)
        c = prev_cap[c]

we walk backwars in the optimal solution an collect the items in reverse order 
then we reverse chosen list and get the items in correct order. 
"""

import sys

def solve_case(cap: int, values: list[int], weights: list[int]) -> tuple[int, list[int]]:
    C = cap
    val_at   = [0]*(C + 1)        # best value for each capacity
    item_at  = [-1]*(C + 1)       # last item that gave that value (-1 = none)
    prev_cap = [-1]*(C + 1)       # previous capacity before adding the item

    for idx, (w, v) in enumerate(zip(weights, values)):
        # walk capacities backwards so each item is considered only once
        for c in range(C, w - 1, -1):
            cand = val_at[c - w] + v
            if cand > val_at[c]:          # strictly better then we wanna take this item
                val_at[c]  = cand
                item_at[c] = idx
                prev_cap[c] = c - w

    #  reconstruct the indicises 
    chosen: list[int] = []
    c = C
    while c >= 0 and item_at[c] != -1:
        i = item_at[c]
        chosen.append(i)
        c = prev_cap[c]
    chosen.reverse()
    return len(chosen), chosen


def ints() -> list[int]:
    return list(map(int, sys.stdin.buffer.read().split())) # https://stackoverflow.com/questions/55596557/os-read0-vs-sys-stdin-buffer-read-in-python

def main() -> None:
    data = ints()
    out_lines: list[str] = []
    idx = 0
    while idx + 1 < len(data):
        C, n = data[idx], data[idx + 1]
        idx += 2

        vals = data[idx     : idx + 2*n : 2]
        wts  = data[idx + 1 : idx + 2*n : 2]
        idx += 2*n

        k, items = solve_case(C, vals, wts)
        out_lines.append(str(k))
        out_lines.append(" ".join(map(str, items)))

    sys.stdout.write("\n".join(out_lines))

main()