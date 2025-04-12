def solve():
    import sys
    input_data = sys.stdin.read().strip()
    n = int(input_data)
    Z = 0
    power_of_5 = 5
    while power_of_5 <= n:
        Z += n // power_of_5
        power_of_5 *= 5

    e2 = 0
    power_of_2 = 2
    while power_of_2 <= n:
        e2 += n // power_of_2
        power_of_2 *= 2
    e2 -= Z
    M = 10**6
    product_mod = 1
    for i in range(1, n + 1):
        x = i
        while x % 5 == 0:
            x //= 5
        product_mod = (product_mod * (x % M)) % M

    if e2 > 0:
        twos_part = pow(2, e2, M)
        product_mod = (product_mod * twos_part) % M

    bigX = product_mod
    above_thousand = (bigX // 1000)  
    last_three = bigX % 1000

    if above_thousand == 0:

        print(last_three)  
    else:
        print(f"{last_three:03d}")

n = int(input())

a = 1
twos = 0  
fives = 0  

for i in range(2, n + 1):
    num = i

    while num % 2 == 0:
        num //= 2
        twos += 1
    while num % 5 == 0:
        num //= 5
        fives += 1

    a = (a * num) % 1000

for _ in range(twos - fives):
    a = (a * 2) % 1000

print(a)