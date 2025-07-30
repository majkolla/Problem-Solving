"""
Michael Birtman - micbi949

Floyd warshall gives us the shortest paths in O(n^3), then we do another O(n^3) loop to mark every pair 
that's affected by the neg cycles. 
So we compute the shortest paths beftween all pairs of nodes and then we return according to kattis. 

First i create a nxn distance matrix init to inf and set the diag to 0 becuase dist is 0 there 
then i put in the direct edge weights and i keep the smallest if there are mutlple. 

I uypdate the dist between i and j using different paths (intermediate nodes),
if dist between k and k is less than 0 i know i have negative cyucle and i mark all the nodes that can be affected 

then i just print 
"""

import sys
import math 
INF = math.inf
 

def shortest_path_all_pairs(n, edge_list):

    # initialize the distnace of the matrix with inf 
    dist = [[INF] * n for _ in range(n)]
    for v in range(n):
        dist[v][v] = 0
    for u, v, w in edge_list:
        dist[u][v] = min(dist[u][v], w)     # keep smallest parallel edge

    # Floyd-Warshall loops  https://www.geeksforgeeks.org/dsa/floyd-warshall-algorithm-in-python/
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            if dist[i][k] == INF:
                continue
            
            dik = dist[i][k]
            di = dist[i]
            
            for j in range(n):
                if dk[j] == INF:
                    continue
                
                
                if di[j] > dik + dk[j]:
                    di[j] = dik + dk[j]

    # now we mark the  pairs affected by a neg. cycle 
    neg = [[False] * n for _ in range(n)]
    for k in range(n):
        if dist[k][k] < 0:                    # vertex k is in / reachable from a neg-cycle
            
            for i in range(n):
                if dist[i][k] == INF:
                    continue                # k not reachable from i
                
                for j in range(n):
                    if dist[k][j] == INF:
                        continue            # j not reachable from k
                    
                    neg[i][j] = True        # the chain can go around the cycle and get - inf 
    return dist, neg


def main():
    it = sys.stdin
    out_lines = []

    while True:
        line = it.readline().split()
        if not line:
            break
        n, m, q = map(int, line)
        if n == m == q == 0:                # sentinel
            break

        edges = []
        for _ in range(m):
            line = it.readline().split()
            node1, node2, weight = map(int, line)
            edges.append((node1, node2, weight))

        dist, neg = shortest_path_all_pairs(n, edges)

        for _ in range(q):
            line = it.readline().split()
            u, v = map(int, line)
            
            if neg[u][v]:
                out_lines.append("-Infinity")
                
            elif dist[u][v] == INF:
                out_lines.append("Impossible")
                
            else:
                out_lines.append(str(dist[u][v]))
        out_lines.append("")       

    sys.stdout.write("\n".join(out_lines))

main()
