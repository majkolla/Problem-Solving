"""
Michael Birtman micbi949

Polynomial Multiplication 2 

We are given test case containing two polynomials: p, q 
    we wanna compute r(x) = p(x)q(x)  and we're going to do it using fft 
https://www.geeksforgeeks.org/dsa/fast-fourier-transformation-poynomial-multiplication/
complexity 

we use a divide and conquer method with fft which is a cooley tukey implementation we såöot omtp pdd amd evem omdoecoes amd then we combine 
we do a point wise mult in freq domain and inverse, also we round. 
time:  O(n log n) 
memory: O(K)
"""
from sys import stdin, stdout
import math, cmath


def fft(a: list[complex], invert: bool = False) -> list[complex]:
    n = len(a)
    if n == 1:   # base case
        return a

    even = fft(a[0::2], invert)      # FFT of even-indexed elements
    odd = fft(a[1::2], invert)   # FFT of odd-indexed elements

    ang = 2 * math.pi / n * (-1 if not invert else 1)
    w_n = cmath.exp(1j * ang) # primitive root of unity
    w = 1 + 0j

    y = [0j] * n
    half = n // 2
    for k in range(half):
        t = w * odd[k]
        y[k] =  even[k] + t
        y[k + half]  =  even[k] - t
        w *= w_n

    if invert:   # normalise after inverse FFT
        return [z / 2 for z in y]
    return y

def convolve_int(a: list[int], b: list[int]) -> list[int]:
    need = len(a) + len(b) - 1
    n = 1
    while n < need:   # next power-of-two
        n *= 2 

    fa = list(map(complex, a)) + [0j] * (n - len(a))
    fb = list(map(complex, b)) + [0j] * (n - len(b))

    fa = fft(fa, False)
    fb = fft(fb, False)
    fc = [fa[i] * fb[i] for i in range(n)]
    fc = fft(fc, True)    # inverse FFT

    conv = [int(round(fc[i].real)) for i in range(need)]
    return conv 

def main() -> None:
    data = list(map(int, stdin.buffer.read().split()))
    if not data:
        return
    pos = 0
    t = data[pos]
    pos += 1          # T == 1 by the statement
    
    out = []
    
    for _ in range(t):
        n = data[pos]
        pos += 1
        
        a = data[pos: pos + n + 1]
        pos += n + 1
        
        m = data[pos]
        pos += 1
        
        b = data[pos: pos + m + 1]
        pos += m + 1
        
        res = convolve_int(a, b)
        
        out.append(str(n + m))
        out.append(" ".join(map(str, res)))
    stdout.write("\n".join(out))

main()