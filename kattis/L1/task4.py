"""
Michael birtman micbi949 

Disjoint Set Union (Union-Find)

We are given N elements:  0 ... N-1 and must do Q operations:

- "= a b"   merge the sets containing a and b
- "? a b"   print "yes" if a and b are in the same set, otherwise "no"


we are going to be using union find 

- union-by-size   (attach the smaller tree under the larger one)
- path compression (flattens paths during find)


Complexities
- time : O((N + Q) · (N))  here o is the ackerman function that grows very slowly so we are basically dealing with a constant 
so we get: - O(N + Q)
- memory : O(N) integers (parent, size)


"""
import sys

def find(x: int, parent : list[int]) -> int:
    """Return the root of the set containing x"""
    
    while parent[x] != x:
    
        parent[x] = parent[parent[x]]     
        x = parent[x]
    
    return x


def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    q = int(data[1])

    # union find init 
    parent: list[int] = list(range(n))
    size:list[int] = [1] * n          # valid at roots


    out_lines: list[str] = []
    idx = 2  # current reading position in data

    for _ in range(q):
        op = data[idx]          
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        idx += 3

        if op == '=':          # union
            ra = find(a, parent)
            rb = find(b, parent)
            if ra != rb:        # merge smaller under larger
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]
        else:
            if find(a, parent) == find(b, parent):
                out_lines.append("yes")
            else: 
                out_lines.append("no")
                
    sys.stdout.write("\n".join(out_lines))


solve()
