"""
Michael birtman micbi949 

Disjoint Set Union (Union-Find)

We are given N elements:  0 ... N-1 and must do Q operations:

- "= a b"   merge the sets containing a and b
- "? a b"   print "yes" if a and b are in the same set, otherwise "no"


we are going to be using union find 

- union-by-size   (attach the smaller tree under the larger one)
- path compression (flattens paths during find)

data structure:

we represent each set as a rooted tree so: 

parant[x] = paraent of x in the tree
a root r satisfies parent[r] = r and is representing the complete set
size[r] is the number of elements in the ree rooted at r 

first the find(x) follows parents until it gets to the root of the tree of x. That root 
is the id of the set of x. 

we do this by: 
union by size: 
here we can just connect the smaller tree under the larger one. Therefore, 
we have it so taht the larger trees root is the root of the combined tree. 

path compression: 
during find(x) we make the path shorter from x to the root by making 
every node on the path point directly to the node. Then we get a posisbly flat tree or almost flat

Complexities
- time : O((N + Q) · (N))  here o is the ackerman function that grows very slowly so we are basically dealing with a constant 
so we get: - O(N + Q)
- memory : O(N) integers (parent, size)


"""


import sys


class DisjointSetUnion:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # path halving/compression 
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        # Union by size! ra is root of the larger tree
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)



def solve() -> None:
    data = sys.stdin.read().split()


    n = int(data[0])
    q = int(data[1])

    dsu = DisjointSetUnion(n)
    out_lines = []

    idx = 2
    for _ in range(q):
        op = data[idx]
        a = int(data[idx + 1])
        b = int(data[idx + 2])
        idx += 3

        if op == '=':
            dsu.union(a, b)
        elif op == '?':
            if dsu.same(a,b):
                out_lines.append("yes")
            else:
                out_lines.append("no")

    sys.stdout.write("\n".join(out_lines))

solve()

