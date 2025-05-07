import sys, math

def rotated_corners(cx, cy, w, h, deg):
    alpha = -math.radians(deg)
    ca, sa = math.cos(alpha), math.sin(alpha)
    for dx in (-w / 2, w / 2):
        for dy in (-h / 2, h / 2):
            yield (
                cx + dx * ca - dy * sa,
                cy + dx * sa + dy * ca,
            )

def convex_hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 1:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower, upper = [], []
    for p in pts:                                # build lower hull
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):                      # build upper hull
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(poly):
    if len(poly) < 3:
        return 0.0
    s = 0.0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0

it = iter(sys.stdin.read().strip().split())
try:
    T = int(next(it))
except StopIteration:
    sys.exit(0)

for _ in range(T):
    n = int(next(it))
    hull_points = []
    boards_area = 0.0

    for _ in range(n):
        x, y, w, h, v = map(float, (next(it), next(it), next(it), next(it), next(it)))
        boards_area += w * h
        hull_points.extend(rotated_corners(x, y, w, h, v))

    mould_area = polygon_area(convex_hull(hull_points))
    pct = 100.0 * boards_area / mould_area if mould_area else 0.0
    print(f"{pct:.1f} %")