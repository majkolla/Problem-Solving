import sys
from sys import stdin
from collections import defaultdict

sys.setrecursionlimit(1000000)

def tarjan(u):
    global index, indices, low, S, in_stack, sccs
    indices[u] = index
    low[u] = index
    index += 1
    S.append(u)
    in_stack.add(u)
    for v in adj[u]:
        if indices[v] == -1:
            tarjan(v)
            low[u] = min(low[u], low[v])
        elif v in in_stack:
            low[u] = min(low[u], indices[v])
    if low[u] == indices[u]:
        scc = []
        while True:
            v = S.pop()
            in_stack.remove(v)
            scc.append(v)
            if v == u:
                break
        sccs.append(scc)

def solve():
    input = stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        global adj, indices, low, in_stack, sccs, index, S
        adj = [[] for _ in range(n+1)]
        for __ in range(m):
            s1 = int(input[ptr])
            s2 = int(input[ptr+1])
            ptr += 2
            adj[s1].append(s2)
        indices = [-1]*(n+1)
        low = [-1]*(n+1)
        in_stack = set()
        sccs = []
        index = 0
        S = []
        for u in range(1, n+1):
            if indices[u] == -1:
                tarjan(u)
        k = len(sccs)
        if k == 1:
            print(0)
            continue
        component = [0]*(n+1)
        for i, scc in enumerate(sccs):
            for node in scc:
                component[node] = i
        in_degree = [0]*k
        out_degree = [0]*k
        added = defaultdict(set)
        for u in range(1, n+1):
            for v in adj[u]:
                if component[u] != component[v]:
                    if component[v] not in added[component[u]]:
                        added[component[u]].add(component[v])
                        out_degree[component[u]] += 1
                        in_degree[component[v]] += 1
        S = sum(1 for i in range(k) if in_degree[i] == 0)
        T = sum(1 for i in range(k) if out_degree[i] == 0)
        print(max(S, T))

if __name__ == "__main__":
    solve()