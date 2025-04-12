import math

def solve():
    while True:
        line = input().strip()
        if line == '0':
            break
        
     
        digits = line[2:-3]
        
        best_num = None
        best_den = None
        
        for r in range(1, len(digits) + 1):
            nr = len(digits) - r  
            X = int(digits)                   
            Y = int(digits[:nr]) if nr > 0 else 0  
            
            numerator = X - Y
            denominator = (10**nr) * (10**r - 1)
            
            g = math.gcd(numerator, denominator)
            numerator //= g
            denominator //= g
            
            if best_den is None or denominator < best_den:
                best_den = denominator
                best_num = numerator
        
        print(f"{best_num}/{best_den}")
solve()