"""
Michael Birtman - micbi949

SuffixArray

the inspo https://cp-algorithms.com/string/suffix-array.html


first we have the constructor  O(s log s)
then we have the query that has a linear time  O(1)    
        which returns the start index of the i lexicographicaly smallest suffix


first we build a suffix array using the cyclic shift or doubling alg. but
we use counting sorts. Thus we have that every round
costs O(s), i.e. we get  O(s log s)

Internal fields

self.sa = list of suffix start positions in the sorted order  
self.rank = current ranks  

-------------------------------------------- Added stuff
Problem is basically: input: non empty string then a line 
outoput: for each qi we print the starting idx of qith lexicographically
smallest suffiex of s. 

Suffix array: 
- s[i:] for 0 <= i < n 
- the suffix arr sa is a permuation such that 
    s[sa[0]:] < s[sa[1]:] < ... < s[sa[n-1]:] 

this way we can make any query q1 and itll be answered in constant time 
by retuning sa[qi]!

We construct this arr by using prefix doubling: 
- sort suffixes by increasingly long prefixes of len 1,2,4, etc 
- let rank[i] be an int class that describe us L first chars of suffic s[i:]
- init L = 1 so rank[i] is just the chars code of ord(s[i])


doubling step: 
- let rank[i] be the correct repr. of fist L chars of s[i:]
- then the first 2L chars of s[i:] are determined by the pair: 
    rank[i], rank[i+l] since: 
    - rank[i] represents s[i : i+L]
    - rank[i+L] represents s[i+L : i+2L]

Sorting the suffixes by these pairs therefore sorts the first 2L chars
and after sorting we "compress" equal paris into same new rank
therefore producing ranks for len 2L prefixes. 

More about each round and complexity: 

- The pair keys are integer ranks in [0..n-1, so we cna do it in linear time 
- We do a radix sort
    - stable counting sort by second key rank[i+L]
    - stable counting sort by first key rank[i]
- if we have out of range stuff, it's just treated as -1, thus no chars left 
so shorter suffixes comes before longer ones when one is the prefix of the other 


each round doubles L so get get at most log_2n rounds (rounded up)


Complexity: 
building the suffix arr O(nlogn) bc. time per round O(n) and O(logn) rounds 
each query is constant time. 

"""

import sys


class SuffixArray:
    def __init__(self, s: str) -> None:
        self._s = s
        self.sa: list[int] = self._build_sa(s)      # O(n log n)

    def getSuffix(self, i: int) -> int:
        """Return the start pos of the ith smallest suffix"""
        return self.sa[i]                           # O(1)

    # construction of the suffix array O(s log s)
    def _build_sa(self, s: str) -> list[int]:
        n = len(s)
        sa = list(range(n))    # initial order 
        rank = [ord(c) for c in s]    # rank by single char https://www.w3schools.com/python/ref_func_ord.asp 
        tmp = [0] * n                     # helper array
        k = 1          # current 2^k prefix len

        # heklp function:  counting sort by key
        def counting_sort(indices: list[int],
                          key_fn,
                          max_val: int) -> list[int]:
            cnt = [0] * (max_val + 2)               # +2
            for i in indices:
                cnt[key_fn(i) + 1] += 1     # shift by +1
            
            for i in range(1, len(cnt)):
                cnt[i] += cnt[i - 1]  # prefix sums
            out = [0] * len(indices)
            
            for i in reversed(indices):
                k = key_fn(i) + 1
                cnt[k] -= 1
                out[cnt[k]] = i
            
            
            return out

        while k < n:
            max_rank = max(rank)

            # sort by second key rank[i + k], then first key rank[i]
            sa = counting_sort(sa, lambda i: rank[i + k] if i + k < n else -1    , max_rank)
            
            sa = counting_sort(sa, lambda i: rank[i], max_rank)

            # re-rank
            tmp[sa[0]] = 0
            r = 0
            for i in range(1, n):
                prev, cur = sa[i - 1], sa[i]
                
                cur_rank = rank[cur]
                cur_next_rank = rank[cur + k] if cur + k < n else -1

                # pull out previous ranks
                prev_rank      = rank[prev]
                prev_next_rank = rank[prev + k] if prev + k < n else -1

                if (cur_rank, cur_next_rank) != (prev_rank, prev_next_rank):
                    r += 1
                tmp[cur] = r
            rank, tmp = tmp, rank    # swap buffers
            if r == n - 1:    # all ranks unique
                break
            k *= 2
        return sa



def main():
    it = sys.stdin
    out_lines = []

    while True:
        
        
        s = it.readline().rstrip('\n')
        if not s:
            break
        line = it.readline()

        parts = list(map(int, line.split()))
        _, *queries = parts # the star makes it so that we can read the _ the first and 
                            # then queiries get the be rest of the elemtns in the container

        # build suffix array and answer all queries
        SA = SuffixArray(s)
        #for q in queries: 
        out_lines.append(" ".join(str(SA.getSuffix(q)) for q in queries))

    sys.stdout.write("\n".join(out_lines))


main()
