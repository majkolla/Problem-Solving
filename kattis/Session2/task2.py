def count_repeated_substrings(s: str) -> int:
    """
    """
    trans, link, length, occ = [], [], [], []

    def new_state():
        trans.append({})
        link.append(-1)
        length.append(0)
        occ.append(0)
        return len(trans) - 1

    root = new_state()
    last = root

    for ch in s:
        cur = new_state()
        length[cur] = length[last] + 1
        occ[cur] = 1                              # new end-position
        p = last
        while p != -1 and ch not in trans[p]:
            trans[p][ch] = cur
            p = link[p]
        if p == -1:
            link[cur] = root
        else:
            q = trans[p][ch]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:                                # need a *clone* state
                clone = new_state()
                trans[clone] = trans[q].copy()
                length[clone] = length[p] + 1
                link[clone] = link[q]
                # occ[clone] starts at 0; its end-positions get inherited later
                while p != -1 and trans[p].get(ch) == q:
                    trans[p][ch] = clone
                    p = link[p]
                link[q] = link[cur] = clone
        last = cur

    # ─────────── propagate frequencies (endpos sizes) upwards ────────────
    for v in sorted(range(len(length)), key=lambda v: length[v], reverse=True):
        if link[v] != -1:
            occ[link[v]] += occ[v]

    # ────────────────────────── final tally ──────────────────────────────
    total = 0
    for v in range(1, len(length)):               # skip the root (0)
        if occ[v] >= 2:
            total += length[v] - length[link[v]]
    return total


def solve_io(src: str) -> str:
    """tiny wrapper matching the problem's multi-case I/O format"""
    lines = src.strip().splitlines()
    t = int(lines[0])
    out = []
    for i in range(1, t + 1):
        out.append(str(count_repeated_substrings(lines[i].rstrip("\n"))))
    return "\n".join(out)


# ─── quick run on the sample ───
if __name__ == "__main__":
    SAMPLE = """\
3
aabaab
aaaaa
AaAaA
"""
    print(solve_io(SAMPLE))
"""
find total number of repeated substrings in a string 


"""

