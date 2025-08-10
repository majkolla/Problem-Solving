"""
Michael Birtman - micbi949

Chinese remeinaer theorem 
 
for each case we get some ints 

    x tripple equal a (mod n)  
    x tripple equal b (mod m), with gcd(n, m) = 1

and we wanna ouput 

    x, K = nm, where  0 <= x < K.
Alg: idea https://cp-algorithms.com/algebra/chinese-remainder-theorem.html
---------
With prime moduli the solution is unique modulo K.  Let  

    n^-1 = modular inverse of n (mod m).

then we just set
    t  =  ( (b - a) mod m) * n^-1  mod m      ( 0 <= t < m )  
    x  =  a + n * t      ( 0 <= x < nm )

proof idea:  
x tripple equal a (mod n) by construction.  
then we know that
x tripple equal a + nt tripple equal a + (b - a) tripple equal b (mod m)

Complexities
------------
- gcd for  inverse O(log m)  
-  rest of the operations are O(1) 

note that python ints cannot overflow 
"""

import sys


# Extended Euclidean algorithm => g,x, y where g = a*x + b*y
def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def mod_inv(a: int, mod: int) -> int:
    """Return a^{-1} mod 'mod', assume that gcd(a, mod) = 1."""
    g, x, _ = egcd(a, mod)
    if g != 1:
        print("test (we shouldnt be here)")
    return x % mod


def crt_two(a: int, n: int, b: int, m: int) -> tuple[int, int]:
    """Return (x, k) for the system with co prime n and m."""
    n_inv = mod_inv(n, m)          # inverse of n modulo m
    t = ((b - a) % m) * n_inv % m
    x = a + n * t
    K = n * m
    return x, K


def main():
    it = sys.stdin
    T = int(it.readline())
    out = []
    for _ in range(T):
        a, n, b, m = map(int, it.readline().split())
        x, K = crt_two(a, n, b, m)
        out.append(f"{x} {K}")
    sys.stdout.write("\n".join(out))


main()