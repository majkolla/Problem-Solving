import sys 
"""
- we do a prime factorise m 
- use legendre's formula 

edge cases: 
- m = 0 undivisieble 
- m = 1 always divides 
n = 0 only divides 0!

we look at the factorial function 
"""
def primes(x: int) -> dict[int, int]: 
    f : dict = {}
    d : int = 2

    while d * d <= x:
        while x % d == 0: 
            f[d] = f.get(d, 0) + 1
            x = x // d
        if d == 2: 
            d +=1
        else: 
            d = 2
    if x > 1: 
        f[x] = f.get(x,0) + 1
    return f


def divides_fact(n: int, m: int) -> bool:
    if m == 0:
        return False
    if m ==  1:        
        return True
    if n == 0:
        return m == 1

    for p, e in primes(m).items():
        exp = 0 
        power = p
        while power <= n:
            exp += n // power
            power *= p
        if exp < e:
            return False
    return True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n, m = map(int, line.split())
    if divides_fact(n, m):
        print(f"{m} divides {n}!")
    else:
        print(f"{m} does not divide {n}!")