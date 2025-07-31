"""
Michael Birtman - micbi949

We are going to use KMP pattern matching to solve this question. 

Finds **all** (possibly overlapping) occurrences of `pattern` in `text`
in linear time, O(len(text) + len(pattern)), and prints their 0-based
indices for each test case.

Input format (until EOF):
    pattern\n
    text\n

Output for each case:
    space-separated list of indices on one line
    (print an empty line if there are no matches)
"""

import sys


# ---------- KMP helper: build longest-prefix-suffix (LPS) table ----------
def build_lps(pat: str) -> list[int]:
    """Return the LPS array where lps[i] = length of the longest proper
    prefix of pat[0:i+1] that is also a suffix of pat[0:i+1]."""
    lps = [0] * len(pat)
    length = 0                       # length of current candidate prefix

    for i in range(1, len(pat)):
        while length and pat[i] != pat[length]:
            length = lps[length - 1] # fallback in the table
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
    return lps


# ---------- KMP search ----------
def find_all_occurrences(pattern: str, text: str) -> list[int]:
    """Return a list of all start indices (0-based) where pattern occurs."""
    if not pattern or not text or len(pattern) > len(text):
        return []

    lps = build_lps(pattern)
    matches = []
    j = 0                            # current length of matched prefix

    for i, ch in enumerate(text):
        while j and ch != pattern[j]:
            j = lps[j - 1]           # fallback using LPS
        if ch == pattern[j]:
            j += 1                   # extend current match
            if j == len(pattern):    # full match found
                matches.append(i - j + 1)
                j = lps[j - 1]       # prepare for next (overlapping) match
    return matches


def main():
    it = sys.stdin
    out_lines = []

    while True:
        pattern = it.readline()
        if not pattern:              # EOF
            break
        pattern = pattern.rstrip('\n')

        text = it.readline().rstrip("\n")

        positions = find_all_occurrences(pattern, text)
        out_lines.append(" ".join(map(str, positions)))  # blank line if none

    sys.stdout.write("\n".join(out_lines))


main()
