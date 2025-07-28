"""
Michael Birtman micbi949 

https://www.geeksforgeeks.org/dsa/detect-negative-cycle-graph-bellman-ford/

first we relax it n-1 times (worst case is O(n m ) if no edges change). because bell ford gives a guarentee if there are no
negative cycles reachable from the source 

then we make a cycle detection pass, because edges can still be relaxed means that we have head vertex that is 
reachable through a negative cycle. just go through so O(m)

we then


"""

import sys
from collections import deque
import math 
INF = math.inf


def shortest_path(graph, n, start):

    dist   = [INF] * n
    parent = [-1]  * n
    dist[start] = 0

    # Relax edges up to (n-1) times 
    for _ in range(n - 1):
        changed = False
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v]   = dist[u] + w
                parent[v] = u
                changed = True
        if not changed:                    # early stop
            break

    # Find vertices that we still can improve on  after neg-cycle 
    in_neg = [False] * n
    for u, v, w in graph:
        if dist[u] != INF and (dist[u] + w < dist[v]):
            in_neg[v] = True               # edge relaxes means negative cycle

    # now we go through that mark with BFS/DFS over outgoing edges 
    # and then we build adjency lists
    adj = [[] for _ in range(n)]
    
    for u, v, _ in graph:
        adj[u].append(v)
    q = deque()
    
    for v, bad in enumerate(in_neg):
        if bad:
            q.append(v)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not in_neg[v]:
                in_neg[v] = True
                q.append(v)

    return dist, parent, in_neg



def main():
    it = sys.stdin
    out_lines = []

    while True:
        line = it.readline()
        if not line:
            break
        n, m, q, s = map(int, line.split())
        if n == m == q == s == 0:
            break

        edges = []
        for _ in range(m):
            line = it.readline().split()
            u, v, w = map(int, line)
            edges.append((u, v, w))


        dist, parent, in_neg = shortest_path(edges, n, s)

        for _ in range(q):
            t = int(it.readline())
            if in_neg[t]:
                out_lines.append("-Infinity")
            elif dist[t] == INF:
                out_lines.append("Impossible")
            else:
                out_lines.append(str(dist[t]))
        out_lines.append("")          # blank line between cases

    sys.stdout.write("\n".join(out_lines))


main()
