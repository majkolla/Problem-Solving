import sys
from math import isclose

def squared_length(p, q):
    """Return squared distance between points p and q."""
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def triangle_type(p1, p2, p3):
    """Classify the triangle or return None if it is degenerate."""
    # reject duplicate points
    if p1 == p2 or p1 == p3 or p2 == p3:
        return None

    # check collinearity via twice the signed area
    area2 = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    if area2 == 0:
        return None

    # squared side lengths
    a2 = squared_length(p2, p3)
    b2 = squared_length(p1, p3)
    c2 = squared_length(p1, p2)
    sides2 = sorted([a2, b2, c2])      # s0 ≤ s1 ≤ s2
    s0, s1, s2 = sides2

    # side‑based classification
    if s0 == s1 or s1 == s2:           # equilateral cannot occur per statement
        side_cls = "isosceles"
    else:
        side_cls = "scalene"

    # angle‑based classification using the converse of Pythagoras
    if s2 == s0 + s1:
        angle_cls = "right"
    elif s2 > s0 + s1:
        angle_cls = "obtuse"
    else:
        angle_cls = "acute"

    return f"{side_cls} {angle_cls} triangle"

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    for case in range(1, n + 1):
        coords = [int(next(it)) for _ in range(6)]
        p1, p2, p3 = coords[0:2], coords[2:4], coords[4:6]
        ttype = triangle_type(tuple(p1), tuple(p2), tuple(p3))
        if ttype is None:
            ttype = "not a triangle"
        print(f"Case #{case}: {ttype}")
main()