"""
michael Birtman - micbi949


Before we had v,w that gives the weight and we could always use w. 
Now we have v, t0, P, d and we can leave u and v at t0 + k · P. 

https://www.geeksforgeeks.org/dsa/minimum-time-required-to-visit-each-disappearing-nodes/

earlist departyre on this edge is given by:
t <= 0 leave t0,
elif ¨P==0 edge 
else k = ceil((t - t0)/P) aka (t-t0) // P 

we just added some O(1) operations so the time complexity stays the same as for the previous exercise O((n+m)log n) 
"""



import sys
import heapq
import math 
 
INF = math.inf # or just a large number like 10^10

def shortest_path(graph, start):
    n = len(graph)
    dist   = [INF] * n
    parent = [-1]  * n

    dist[start] = 0 # init 
    pq = [(0, start)]            # (distance so far, vertex)

    while pq:
        d, u = heapq.heappop(pq) # pop the vertex with the smallest dist 
        if d != dist[u]:         # stale entry we discard stuff that becomes outdated when we find better path 
            continue
        
        # for every outgoing edge try the route that reaches u with cost d then pays w. 
        for v, t0, P, d in graph[u]:
            t = dist[u]                         # time we reach u
            if t <= t0:
                leave = t0
            elif P == 0:
                continue                        # missed a one-off edge
            else:
                # round up (t − t0)/P 
                k = (t - t0 + P - 1) // P
                leave = t0 + k * P
            arr = leave + d                     # arrival time at v
            if arr < dist[v]:
                dist[v] = arr
                parent[v] = u
                heapq.heappush(pq, (arr, v))
    return dist, parent

def main():
    it = sys.stdin
    out_lines = []

    while True:
        line = it.readline()
        n, m, q, s = map(int, line.split())
        if n == m == q == s == 0: # read til 0000
            break

        # build graph
        G = [[] for _ in range(n)]
        for _ in range(m):
            #u, v, w = map(int, it.readline().split())
            u, v, t0, P, d = map(int, it.readline().split())
            #G[u].append((v, w))
            G[u].append((v, t0, P, d))

        dist, _ = shortest_path(G, s) # run dijstras 

        for _ in range(q):
            t = int(it.readline())
            if dist[t] != INF: 
                out_lines.append(str(dist[t]))
            else: 
                out_lines.append("Impossible")
        out_lines.append("")   # blank line between test cases

    sys.stdout.write("\n".join(out_lines))
    
    
main()