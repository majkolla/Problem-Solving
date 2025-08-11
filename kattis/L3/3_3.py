"""
Michael Birtman – micbi949

we're going to reuse the same stuff from the previous exercise see this link for more stuff about it 
https://cp-algorithms.com/string/suffix-array.html).  


After the suffix array is built in O(n log n) (as we discussed in previous exercise)
we compute an lcp array. We do this using kaisais alg which is O(n) https://www.geeksforgeeks.org/dsa/kasais-algorithm-for-construction-of-lcp-array-from-suffix-array/
that constructs lcp from suffix array. 
then we output max(lcp),
i.e. len of longest substring occuring at least twice

Complexities
------------
-  Constructo -  O(n log n)  
-  lcp using kaisais - O(n)  
-  ans lookup O(1)

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

# Kasais lcp 
def build_lcp(s: str, sa: list[int]) -> list[int]:
    n = len(s)
    rank = [0] * n
    for i, pos in enumerate(sa):
        rank[pos] = i

    lcp = [0] * n
    h = 0
    for i in range(n):
        r = rank[i]
        if r == 0:
            continue
        j = sa[r - 1]
        while (i + h < n) and (j + h < n) and (s[i + h] == s[j + h]):
            h += 1
        lcp[r] = h
        if h:
            h -= 1
    return lcp


def main() -> None:
    it = sys.stdin
    answers = []

    while True:
        L_line = it.readline()
        if not L_line:
            break  # EOF
        L = int(L_line.strip())
        s = it.readline().rstrip('\n')

        sa = SuffixArray(s).sa
        lcp = build_lcp(s, sa)
        answers.append(str(max(lcp)))  # longest repeated substring length

    sys.stdout.write("\n".join(answers))


main()
