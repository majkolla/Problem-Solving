import math

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        elif rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootB] = rootA
            rank[rootA] += 1
        return True
    return False

def solve():
    t = int(input().strip())  # number of test cases
    for _ in range(t):
        m = int(input().strip())  # number of islands
        coords = [tuple(map(float, input().split())) for _ in range(m)]

        edges = []
        for i in range(m):
            x1, y1 = coords[i]
            for j in range(i+1, m):
                x2, y2 = coords[j]
                dist = math.hypot(x2 - x1, y2 - y1)
                edges.append((dist, i, j))

        edges.sort(key=lambda e: e[0])

        parent = list(range(m))
        rank = [0]*m
        mst_length = 0.0
        edges_used = 0

        for dist, a, b in edges:
            if union(parent, rank, a, b):
                mst_length += dist
                edges_used += 1
                if edges_used == m - 1:
                    break

        print(f"{mst_length:.6f}")
