import sys
from collections import deque

def solve():
    input_stream = sys.stdin
    T = int(input_stream.readline())
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def bfs(start_r, start_c, maze, rows, cols):

        dist = [[-1]*cols for _ in range(rows)]
        dist[start_r][start_c] = 0
        q = deque()
        q.append((start_r, start_c))
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if maze[nr][nc] != '#' and dist[nr][nc] == -1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))
        return dist
    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0]*n
            self.components = n
        
        def find(self, a):
            if self.parent[a] != a:
                self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
        
        def union(self, a, b):
            rootA = self.find(a)
            rootB = self.find(b)
            if rootA != rootB:
                if self.rank[rootA] < self.rank[rootB]:
                    rootA, rootB = rootB, rootA
                self.parent[rootB] = rootA
                if self.rank[rootA] == self.rank[rootB]:
                    self.rank[rootA] += 1
                self.components -= 1
                return True
            return False
    
    outputs = []
    for _ in range(T):
        line = input_stream.readline().strip()
        x, y = map(int, line.split())
        
        maze = []
        for _row in range(y):
            row_str = input_stream.readline().rstrip('\n')
            if len(row_str) < x:
                row_str += ' '*(x - len(row_str))
            row_str = row_str[:x]
            maze.append(row_str)
        
        points = []
        
        for r in range(y):
            for c in range(x):
                if maze[r][c] == 'S':
                    points.append((r,c))
        
        for r in range(y):
            for c in range(x):
                if maze[r][c] == 'A':
                    points.append((r,c))
        
        k = len(points)
        bfs_results = []
        for i in range(k):
            (sr, sc) = points[i]
            bfs_results.append(bfs(sr, sc, maze, y, x))
        
        edges = []
        for i in range(k):
            for j in range(i+1, k):
                (rj, cj) = points[j]
                dist_ij = bfs_results[i][rj][cj]
                edges.append((dist_ij, i, j))
        
        edges.sort(key=lambda e: e[0])
        
        uf = UnionFind(k)
        mst_cost = 0
        for w, i, j in edges:
            if uf.union(i, j):
                mst_cost += w
            if uf.components == 1:
                break
        
        outputs.append(str(mst_cost))
    
    print("\n".join(outputs))

solve()
