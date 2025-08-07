"""
Michael Birtman - micbi949

Chinese remeinaer theorem 
 
for each case we get some ints 

    x tripple equal a (mod n)  
    x tripple equal b (mod m), with gcd(n, m) = 1

and we ouput 

    x, K = nm, where  0 ≤ x < K.

Alg: idea https://cp-algorithms.com/algebra/chinese-remainder-theorem.html
---------
With co-prime moduli the solution is unique modulo K.  Let  

    n^-1 = modular inverse of n (mod m).

then we just set
    t  =  ( (b - a) mod m) * n^-1  mod m      ( 0 <= t < m )  
    x  =  a + n · t                         ( 0 <= x < nm )

Proof:  
x tripple equal a (mod n) by construction.  
then we know that
x tripple equal a + nt tripple equal a + (b - a) tripple equal b (mod m)

Complexities
------------
* Extended-gcd for the inverse O(log min(n,m))  
* All other ops are O(1).  
* Works comfortably for up to 1000 cases (given limit).

Implementation notes
--------------------
* Python’s `int` is unbounded, but a helper `mul_mod` is shown to mimic
  overflow-safe multiplication if the same code is ported to 64-bit
  languages (hint from the assignment).
"""

import sys
from typing import Tuple


# Extended Euclidean algorithm  => (g, x, y) with  g = ax + by
def egcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def mod_inv(a: int, mod: int) -> int:
    """Return a⁻¹  (mod mod),  assuming gcd(a, mod)=1."""
    g, x, _ = egcd(a, mod)
    if g != 1:
        raise ValueError("Inverse does not exist")
    return x % mod


# Optional overflow-safe (a * b) % mod  via Russian peasant method
def mul_mod(a: int, b: int, mod: int) -> int:
    res = 0
    a %= mod
    while b:
        if b & 1:
            res = (res + a) % mod
        a = (a + a) % mod
        b >>= 1
    return res


# Solve one test case
def crt_two(a: int, n: int, b: int, m: int) -> Tuple[int, int]:
    """Return (x, K) for the system with co-prime n, m."""
    n_inv = mod_inv(n, m)                 # n⁻¹  (mod m)
    diff  = (b - a) % m                   # (b − a) mod m
    t     = (diff * n_inv) % m            # may use mul_mod if porting
    # t = mul_mod(diff, n_inv, m)         # <– safe version
    x     = a + n * t
    K     = n * m
    return x, K


def main() -> None:
    it = sys.stdin
    T = int(it.readline())
    out = []

    for _ in range(T):
        a, n, b, m = map(int, it.readline().split())
        x, K = crt_two(a, n, b, m)
        out.append(f"{x} {K}")

    sys.stdout.write("\n".join(out))


main()
