"""
Michael Birtman - micbi949

We are going to use KMP pattern matching to solve this question. first we build an lps table 

we want to find all the occurrences of the pattern in text 
in linear time, O(len(text) + len(pattern)), and prints their
indices for each test case.

https://www.geeksforgeeks.org/dsa/kmp-algorithm-for-pattern-searching/
"""

import sys


# first we build an lps table 
def build_lps(pat: str) -> list[int]:
    """Return the LPS array where lps[i] = length of the longest proper prefix of pat[0:i+1]"""
    lps = [0] * len(pat)
    length = 0                       # length of current prefix

    for i in range(1, len(pat)):
        while length and pat[i] != pat[length]:
            length = lps[length - 1] 
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
    return lps


# now we do the kmp serch
def find_all_occurrences(pattern: str, text: str) -> list[int]:
    """Return a list of all start indices (0-based) where pattern occurs."""
    if not pattern or not text or len(pattern) > len(text):
        return []

    lps = build_lps(pattern)
    matches = []
    j = 0                            # current length of matched prefix

    for i, ch in enumerate(text):
        while j and ch != pattern[j]:
            j = lps[j - 1]           # fallback with lps
        if ch == pattern[j]:
            j += 1                   # extend the match
            if j == len(pattern):    # full match found
                matches.append(i - j + 1)
                j = lps[j - 1]       # prepare for next match
    return matches


def main():
    it = sys.stdin
    out_lines = []

    while True:
        pattern = it.readline()
        if not pattern:             
            break
        pattern = pattern.rstrip('\n')

        text = it.readline().rstrip("\n")

        positions = find_all_occurrences(pattern, text)
        out_lines.append(" ".join(map(str, positions))) 

    sys.stdout.write("\n".join(out_lines))


main()
