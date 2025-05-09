import sys, math

EPS = 1e-12                    

def sub(a, b): return (a[0]-b[0], a[1]-b[1])
def dot(a, b): return a[0]*b[0] + a[1]*b[1]
def cross(a, b): return a[0]*b[1] - a[1]*b[0]
def dist(a, b): return math.hypot(a[0]-b[0], a[1]-b[1])

def leash_len(stack, spot):
    """sum of segment lengths post‑…‑pivot‑spot"""
    l, prev = 0.0, stack[0]
    for p in stack[1:]:
        l += dist(prev, p);  prev = p
    return l + dist(prev, spot)

def collinear(a, b, c):
    return abs(cross(sub(b, a), sub(c, a))) < EPS

def max_leash(toys, trees):
    origin = (0.0, 0.0)
    stack  = [origin]        
    spot   = origin
    best   = 0.0

    for toy in toys:           
        start, target = spot, toy
        d = sub(target, start)  

        while True:
            P_last = stack[-1]
            P_prev = stack[-2] if len(stack) >= 2 else None

            best_t, ev_kind, ev_arg = 2.0, None, None  
            for Z in trees:
                if Z == P_last:          
                    continue
                ZB   = sub(Z, P_last)
                num  = cross(ZB, sub(start, P_last))
                den  = -cross(ZB, d)
                if abs(den) < EPS:       
                    continue
                t = num / den
                if t <= EPS or t > 1.0+EPS:
                    continue
                vec = (start[0]+t*d[0]-P_last[0],
                       start[1]+t*d[1]-P_last[1])
                if dot(ZB, vec) < -EPS:               
                    continue
                if dist(P_last, Z) - dist(P_last, (start[0]+t*d[0], start[1]+t*d[1])) > EPS:
                    continue
                if t < best_t - EPS:
                    best_t, ev_kind, ev_arg = t, "wrap", Z

            if P_prev is not None:
                BA  = sub(P_last, P_prev)
                num = cross(BA, sub(start, P_last))
                den = -cross(BA, d)
                if abs(den) > EPS:
                    t = num / den
                    if -EPS <= t <= 1.0+EPS:          
                        if t < best_t - EPS:
                            best_t, ev_kind = t, "unwrap"

            if best_t > 1.0 - EPS:
                best_t, ev_kind = 1.0, None

            spot = (start[0] + best_t*d[0],
                    start[1] + best_t*d[1])
            best = max(best, leash_len(stack, spot))

            if ev_kind is None:      
                break

            if ev_kind == "wrap":
                stack.append(ev_arg)
            else:                   
                stack.pop()

                while len(stack) >= 2 and collinear(stack[-2], stack[-1], spot):
                    stack.pop()

            start = spot
            d = sub(target, start)

    return best

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    toys  = [(float(next(it)), float(next(it))) for _ in range(n)]
    trees = [(float(next(it)), float(next(it))) for _ in range(m)]

    print(f"{max_leash(toys, trees):.2f}")

main()