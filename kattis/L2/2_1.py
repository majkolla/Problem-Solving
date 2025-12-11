"""
michael Birtman - micbi949


We have a a list of adjacencies that contains paris for each outgoing edge, then we use dijkastra with min heap (the heap q module)
so parent stores the pre that achieved the best distance, so we can rebuild the path. THen we got the normal pasrsing. 

Let  n = # vertices 
     m = # directed edges 
     
each vertex is popped once => n heappops 
every edge can maximum triggerf one improvement => m heappush 
heap1 operations costs log n  https://docs.python.org/3/library/heapq.html

thus we get O((n+m)log n)
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
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]: # if the cost improve nd on dist v then we record it and store the pre 
                dist[v]   = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v)) # push it into heap 
    return dist, parent

def reconstruct_path(parent, start, target):
    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]

    path.reverse()
    return path


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
            u, v, w = map(int, it.readline().split())
            G[u].append((v, w))

        dist, parent = shortest_path(G, s) # run dijstras 

        for _ in range(q):
            t = int(it.readline())
            if dist[t] != INF: 
                out_lines.append(str(dist[t]))
                # print the path here if we want to 
            else: 
                out_lines.append("Impossible")
        out_lines.append("")   # blank line between test cases

    sys.stdout.write("\n".join(out_lines))
    
    
main()