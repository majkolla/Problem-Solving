"""
Disjoint Set Union (Union‑Find)
===============================

Problem
-------
Maintain *N* disjoint sets of elements **0 … N‑1** while processing **Q**
operations:

* "`= a b`" – merge the sets that contain *a* and *b*  
* "`? a b`" – answer whether *a* and *b* are in the same set, output
  `"yes"` or `"no"`

Constraints: 1 ≤ N ≤ 1 000 000,  0 ≤ Q ≤ 1 000 000.

Solution overview
-----------------
Use the classic **Union‑Find / Disjoint Set Union** structure with

* **union‑by‑size** – attach the smaller tree under the larger one  
* **path compression** – flattens trees during `find`

Both heuristics together give an **amortised** time complexity of
O(α(N)) per operation, where α is the inverse Ackermann function –
effectively *constant* for any realistic input.

Implementation details
----------------------
* `parent[i]` – immediate parent of node *i* (or *i* itself if root)  
* `size[i]`   – size of tree rooted at *i* (valid only at roots)
* An **iterative** `find` avoids deep recursion.
* All output is buffered in a list and written once at the end to keep
  I/O fast.

Complexities
------------
* **Time:** O((N + Q) · α(N))   (~ O(N + Q) in practice)  
* **Memory:** O(N) integers  (`parent`, `size`)

Author
------
Your Name <your.email@example.com>
"""

import sys


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    q = int(data[1])
 
    # Initialise Union‑Find structures
    parent: list[int] = list(range(n))
    size:   list[int] = [1] * n          # valid only at roots

    def find(x: int) -> int:
        """Return root of the set containing x (with path compression)."""
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path‑halve
            x = parent[x]
        return x

    out_lines: list[str] = []
    idx = 2  # current position in the token list

    for _ in range(q):
        op = data[idx]          # raw byte literal: b'=' or b'?'
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        idx += 3

        if op == b'=':          # union operation
            ra = find(a)
            rb = find(b)
            if ra != rb:        # merge smaller tree into larger
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]
        else:                   # op == b'?': query
            out_lines.append("yes" if find(a) == find(b) else "no")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
