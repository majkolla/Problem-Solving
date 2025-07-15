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