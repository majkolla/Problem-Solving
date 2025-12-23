import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n = data[p]
    p += 1
    masks = (4, 2, 1)
    out = []

    for _ in range(n):
        m = data[p]
        p += 1
        prefs = []
        for _ in range(m):
            prefs.append(data[p:p+8])
            p += 8

        dp_next = list(range(8))
        for i in range(m - 1, -1, -1):
            ranks = prefs[i]
            dp_curr = [0] * 8
            for state in range(8):
                best = dp_next[state ^ masks[0]]
                best_rank = ranks[best]
                t = dp_next[state ^ masks[1]]
                r = ranks[t]
                if r < best_rank:
                    best_rank = r
                    best = t
                t = dp_next[state ^ masks[2]]
                r = ranks[t]
                if r < best_rank:
                    best = t
                dp_curr[state] = best
            dp_next = dp_curr

        final = dp_next[0]
        out.append(
            ("Y" if final & 4 else "N") +
            ("Y" if final & 2 else "N") +
            ("Y" if final & 1 else "N")
        )

    sys.stdout.write("\n".join(out))

main()
