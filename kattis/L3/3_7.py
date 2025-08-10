"""
Michael Birtman - micbi949

General Chinese Remainder Theorem (non-coprime moduli)
=====================================================
Solve, for each test case:
    x tripple equal a (mod n)
    x tripple equal b (mod m)

basic alg: 

we let g = gcd(n, m) then  a solution exists iff (a - b) % g == 0.

then we know that if there is no solution we just print no solution

Otherwise we reduce to it to the co prime modulo
    n' = n / g,  m' = m / g
Let inv = (n')^{-1} mod m' (must exist bc of assumption  gcd(n', m') = 1)

Then we compute 
    t = ((b - a) / g) * inv  mod m'
    x = a + n * t
    K = lcm(n, m) = n / g * m
return x % K, K


From previous stuf we knot that the extended gcd / inverse is 
O(log m) per case.

and just like before ints are unbounded in python so no need to think baout overflow
"""

import sys


# Extended Euclidean algorithm → (g, x, y) with g = a*x + b*y
def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def mod_inv(a: int, mod: int) -> int:
    """Return a^{-1} (mod mod); assumes gcd(a, mod) = 1."""
    g, x, _ = egcd(a, mod)
    if g != 1:
        print("inverse does not exist")
    return x % mod


def crt_general(a: int, n: int, b: int, m: int) -> tuple[int, int] | None:
    """Return (x, K) with K = lcm(n, m), 0 <= x < K, or None if no solution exist!"""
    g, _, _ = egcd(n, m)
    if (a - b) % g != 0:
        return None

    n_g, m_g = n // g, m // g                     # reduced coprime moduli
    # combine using modular inverse of n' modulo m'
    inv = mod_inv(n_g, m_g)
    t = ((b - a) // g) * inv % m_g
    x = a + n * t
    K = n_g * m                                    # lcm(n, m)
    return x % K, K


def main() -> None:
    it = sys.stdin
    T = int(it.readline())
    out_lines = []
    for _ in range(T):
        a, n, b, m = map(int, it.readline().split())
        res = crt_general(a, n, b, m)
        if res is None:
            out_lines.append("no solution")
        else:
            x, K = res
            out_lines.append(f"{x} {K}")
    sys.stdout.write("\n".join(out_lines))


main()
