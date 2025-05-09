#!/usr/bin/env python3
"""
White‑water rafting ride – maximum raft radius (bug‑fixed)
"""
import sys
import math

# ---------- geometry helpers -------------------------------------------------
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def seg_dist_sq(p, q, r, s):
    """Squared distance between segments PQ and RS (2‑D)."""
    u = sub(q, p)
    v = sub(s, r)
    w = sub(p, r)

    a = dot(u, u)
    b = dot(u, v)
    c = dot(v, v)
    d = dot(u, w)
    e = dot(v, w)
    D = a*c - b*b
    SMALL = 1e-12

    sN, tN = 0.0, 0.0
    sD, tD = D, D

    if D < SMALL:            # almost parallel
        sN, sD = 0.0, 1.0
        tN, tD = e, c
    else:
        sN = b*e - c*d
        tN = a*e - b*d
        if sN < 0.0:
            sN = 0.0
            tN, tD = e, c
        elif sN > sD:
            sN = sD
            tN, tD = e + b, c

    if tN < 0.0:
        tN = 0.0
        if -d < 0.0:
            sN = 0.0
        elif -d > a:
            sN = sD
        else:
            sN, sD = -d, a
    elif tN > tD:
        tN = tD
        if (-d + b) < 0.0:
            sN = 0.0
        elif (-d + b) > a:
            sN = sD
        else:
            sN, sD = -d + b, a

    sc = 0.0 if abs(sD) < SMALL else sN / sD
    tc = 0.0 if abs(tD) < SMALL else tN / tD

    dp = (w[0] + sc*u[0] - tc*v[0],
          w[1] + sc*u[1] - tc*v[1])
    return dot(dp, dp)

# ---------- main -------------------------------------------------------------
buf = sys.stdin.buffer.read().split()
if not buf:
    sys.exit(0)
it = iter(buf)
T = int(next(it))

for _ in range(T):
    ni = int(next(it))
    inner = [(int(next(it)), int(next(it))) for _ in range(ni)]
    no  = int(next(it))
    outer = [(int(next(it)), int(next(it))) for _ in range(no)]

    # edges: consecutive pairs, wrapping around with modulo
    inner_edges = [(inner[i], inner[(i+1) % ni]) for i in range(ni)]
    outer_edges = [(outer[i], outer[(i+1) % no]) for i in range(no)]

    mind2 = float('inf')
    for p, q in inner_edges:
        for r, s in outer_edges:
            d2 = seg_dist_sq(p, q, r, s)
            if d2 < mind2:
                mind2 = d2

    radius = math.sqrt(mind2) * 0.5
    print(f"{radius:.10f}")
