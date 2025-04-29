"""
forest is a graph 
2 nodes connceted if if b = a + 1
or theyre both multple of some integer K 

we want to find the shortest path 

note that if we take the legit path, ie all the nodes it's the worst path 
so if we find a multiple it can only improve the time 

however, because this "or theyre both multple of some integer K", we note that 
we have another connected path that is connected for all. So we can just do the biggest jump 
So we basically know the optimal solution is going to be the normal rule 
+ 1 use of the other connection rule 


we get the min run if we take the biggest step, we do that by lettin 
k = a and b be the biggest possible number 

b = [(n-1)/k] * k rounded down  


"""

import sys
import math

def shortest_path(n: int, K: int) -> int:
    if n == 1:                 # already at home
        return 0

    base = n - 1               # running through all nodes

    if K > n - 1:              # if no multiples exist we only one oke path
        return base

    b = ((n-1)//K) *K   
    r = (n-1) - b          # remainder to reach n-1 after using the multiple
    teleport_path = K + 1 + r # walk to K,, walk remainder

    return min(base, teleport_path)

def main() -> None:
    n_str, k_str = sys.stdin.readline().split()
    n = int(n_str)
    K = int(k_str)
    print(shortest_path(n, K))
main()