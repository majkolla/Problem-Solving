import sys

def zeros_upto(x: int) -> int:
    if x < 0:
        return 0

    total = 1          
    p = 1              

    while p <= x:
        high   = x // (p * 10)
        cur    = (x // p) % 10
        low    = x % p

        if cur == 0:
            total += (high - 1) * p + (low + 1)
        else:
            total += high * p

        p *= 10

    return total


def main() -> None:
    for line in sys.stdin:
        m, n = map(int, line.split())
        if m < 0:                       
            break
        print(zeros_upto(n) - zeros_upto(m - 1))
main()