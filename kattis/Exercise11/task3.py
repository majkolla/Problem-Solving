import sys
import math
from itertools import tee

# ---------- geometry helpers -------------------------------------------------
def dot(a, b):          # 2‑D dot product
    return a[0] * b[0] + a[1] * b[1]

def sub(a, b):          # vector difference
    return (a[0] - b[0], a[1] - b[1])

def seg_dist_sq(p, q, r, s):
    """
    Squared distance between segments PQ and RS (2‑D).
    Algorithm: closest points on two segments (same as 3‑D case).
    """
    u = sub(q, p)
    v = sub(s, r)
    w = sub(p, r)

    a = dot(u, u)
    b = dot(u, v)
    c = dot(v, v)
    d = dot(u, w)
    e = dot(v, w)
    D = a * c - b * b          # always ≥ 0

    SMALL = 1e-12
    sc, sN, sD = 0.0, D, D     # sc = sN / sD
    tc, tN, tD = 0.0, D, D

    if D < SMALL:              # segments almost parallel
        sN = 0.0
        sD = 1.0
        tN = e
        tD = c
    else:
        sN = (b * e - c * d)
        tN = (a * e - b * d)
        if sN < 0.0:
            sN = 0.0
            tN = e
            tD = c
        elif sN > sD:
            sN = sD
            tN = e + b
            tD = c

    if tN < 0.0:
        tN = 0.0
        if -d < 0.0:
            sN = 0.0
        elif -d > a:
            sN = sD
        else:
            sN = -d
            sD = a
    elif tN > tD:
        tN = tD
        if (-d + b) < 0.0:
            sN = 0.0
        elif (-d + b) > a:
            sN = sD
        else:
            sN = (-d + b)
            sD = a

    sc = 0.0 if abs(sN) < SMALL else sN / sD
    tc = 0.0 if abs(tN) < SMALL else tN / tD

    dp = (w[0] + sc * u[0] - tc * v[0],
          w[1] + sc * u[1] - tc * v[1])
    return dot(dp, dp)

def pairwise(iterable, wrap=False):
    """(p0,p1,p2,…) → (p0,p1), (p1,p2), …  (+ last,first if wrap=True)."""
    a, b = tee(iterable)
    next(b, None)
    pairs = zip(a, b)
    if wrap:
        first = next(iterable)
        last = None
        for last in iterable:   # iterate to last element
            pass
        if last is not None:
            pairs = list(pairs) + [(last, first)]
    return pairs

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit(0)
it = iter(data)
T = int(next(it))

for _ in range(T):
    ni = int(next(it))
    inner = [(int(next(it)), int(next(it))) for _ in range(ni)]
    no = int(next(it))
    outer = [(int(next(it)), int(next(it))) for _ in range(no)]

    # build edge lists (as segment endpoint pairs)
    inner_edges = list(pairwise(inner, wrap=True))
    outer_edges = list(pairwise(outer, wrap=True))

    # minimum distance between any edge pair
    mind2 = float('inf')
    for (p, q) in inner_edges:
        for (r, s) in outer_edges:
            d2 = seg_dist_sq(p, q, r, s)
            if d2 < mind2:
                mind2 = d2

    radius = math.sqrt(mind2) * 0.5
    # print with enough digits – 10 is plenty for 1e‑5 tolerance
    print(f"{radius:.10f}")