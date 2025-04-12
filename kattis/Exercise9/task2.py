def normalize_line(line: str) -> str:

    line = line.strip()
    if not line:
        return ''

    parts = line.split()
    return ' '.join(parts)

def read_fragment():

    lines = []
    while True:
        line = input().rstrip('\n')
        if line == "***END***":
            break
        norm = normalize_line(line)
        if norm:
            lines.append(norm)
    return lines

def longest_consecutive_match(linesA, linesB):

    lenA, lenB = len(linesA), len(linesB)
    dp = [0] * (lenB + 1)
    max_len = 0
    for i in range(1, lenA + 1):
        new_dp = [0] * (lenB + 1)
        for j in range(1, lenB + 1):
            if linesA[i - 1] == linesB[j - 1]:
                new_dp[j] = dp[j - 1] + 1
                if new_dp[j] > max_len:
                    max_len = new_dp[j]
        dp = new_dp
    return max_len

def solve():
    import sys
    
    n = int(sys.stdin.readline().strip())
    
    fragments = []
    for _ in range(n):
        filename = sys.stdin.readline().rstrip('\n')
        fragment_lines = []
        while True:
            line = sys.stdin.readline().rstrip('\n')
            if line == "***END***":
                break
            norm = normalize_line(line)
            if norm:
                fragment_lines.append(norm)
        fragments.append((filename, fragment_lines))
    
    snippet_lines = []
    while True:
        line = sys.stdin.readline().rstrip('\n')
        if line == "***END***":
            break
        norm = normalize_line(line)
        if norm:
            snippet_lines.append(norm)
    
    if not snippet_lines:
        print(0)
        return
    
    global_max = 0
    winners = []  
    
    for i, (fname, frag_lines) in enumerate(fragments):
        match_len = longest_consecutive_match(frag_lines, snippet_lines)
        if match_len > global_max:
            global_max = match_len
            winners = [fname]
        elif match_len == global_max and match_len > 0:
            winners.append(fname)
    
    if global_max == 0:
        print(0)
    else:
        print(global_max, *winners)

solve()