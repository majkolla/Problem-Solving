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
        sa = list(range(n))                         # initial order 
        rank = [ord(c) for c in s]                  # rank by single char https://www.w3schools.com/python/ref_func_ord.asp 
        tmp = [0] * n                               # helper array
        k = 1                                       # current 2^k prefix len

        # heklp function:  counting sort by key
        def counting_sort(indices: list[int],
                          key_fn,
                          max_val: int) -> list[int]:
            cnt = [0] * (max_val + 2)               # +2
            for i in indices:
                cnt[key_fn(i) + 1] += 1             # shift by +1
            
            for i in range(1, len(cnt)):
                cnt[i] += cnt[i - 1]                # prefix sums
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
            rank, tmp = tmp, rank                   # swap buffers
            if r == n - 1:                          # all ranks are unique
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
