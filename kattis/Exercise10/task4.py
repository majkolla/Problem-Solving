"""
i did the proof by hand: ill update later but its intersting! 

"""

import sys, random, math
from functools import reduce

def mod_mul(a: int, b: int, m: int) -> int:
    return (a * b) % m

def mod_pow(a: int, d: int, m: int) -> int:
    res = 1
    while d:
        if d & 1:
            res = mod_mul(res, a, m)
        a = mod_mul(a, a, m)
        d >>= 1
    return res

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d & 1 == 0:
        d >>= 1
        s += 1
    for a in (2, 3, 5, 7, 11, 13):
        if a % n == 0:
            continue
        x = mod_pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = mod_mul(x, x, n)
            if x == n - 1:
                break
        else:
            return False
    return True

rand = random.SystemRandom()

def rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    while True:
        c = rand.randrange(1, n)
        f = lambda x: (mod_mul(x, x, n) + c) % n
        x = rand.randrange(0, n)
        y, d = x, 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d

def factor(n: int, fac: list) -> None:
    """append prime factors (not necessarily unique) of n to fac"""
    if n == 1:
        return
    if is_prime(n):
        fac.append(n)
        return
    d = rho(n)
    factor(d, fac)
    factor(n // d, fac)

def phi(n: int) -> int:
    if n == 1:
        return 1
    fac = []
    factor(n, fac)
    fac = set(fac)           
    res = n
    for p in fac:
        res = res // p * (p - 1)
    return res

def divisors(n: int):
    fac = []
    factor(n, fac)
    primes = {}
    for p in fac:
        primes[p] = primes.get(p, 0) + 1
    divs = [1]
    for p, k in primes.items():
        mults = [p ** e for e in range(1, k + 1)]
        divs = [d * m for d in divs for m in ([1] + mults)]
    return divs

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    results = []
    for _ in range(T):
        N = int(next(it))
        ans = sum(phi(d + 1) for d in divisors(N))
        results.append(str(ans))
    print('\n'.join(results))
