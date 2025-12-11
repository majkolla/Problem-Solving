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


updates: 

Question: 
We get a Directed graph with n nodesm m edges and weights and up to q queires. Each query ask for
the min distance from nodu u to v. We can have negative weights. 

We use Floyd-Warshall alg. to compute all the pairs of shortest paths. So: 
dist[i][j] = min dist. from i to j (if no neg. cycle are on that path)

Flloyd warshall, is a dp alg. so we consider a set of nodes as possible inbetween nodes in 
the path. Then after processing a node k we get the best distance from only having the 
inbetween nodes being from 0, ..., k. 

So basically, either we have a path from i to j that doesnt goes through k 
or it goes through k (once or more) and then we split the path at k and use the shortest path
from i to k and shortest path from k to j. 

Negative cycles: 
FFlod warshall gives everything correct if there is no negative cycle. For example if 
we have i ->k and k ->j. and k is on a neg cycle we can just loop around in infity 
to get as "short" (weird word to use here maybe) path as possible 

So after the main Floyd warshall we do another tripple forloop: 
for each k with dist[k][k] < 0
    for every i that can reach k
        for every j htat is reachbel from k 
            mark pair (i,j) as affected by negative cycle 

So we store this in a bool matrix adn if it's true then we just answer - infinity otherwise
otheriwse if dist[u][v] is still infinite there is no path and we just answer impossible. 
otherwise we just return the normal (finite) val dist[u][v]

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
