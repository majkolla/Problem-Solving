import sys

def largest_pth_power(x):
    absx = abs(x) 
    def is_power(x, base, p):
        return pow(base, p) == x
    
    for p in range(31, 1, -1):
        if x > 0:
            base = int(round(absx ** (1.0/p)))
            for candidate in [base-1, base, base+1]:
                if candidate > 1 and is_power(x, candidate, p):
                    return p
        else:
            if p % 2 == 1:
                base = int(round(absx ** (1.0/p)))
                for candidate in [base-1, base, base+1]:
                    if candidate > 0 and is_power(x, -candidate, p):
                        return p
    
    return 1

def main():
    for line in sys.stdin:
        x_str = line.strip()
        if x_str == '0':
            break
        x = int(x_str)
        print(largest_pth_power(x))

if __name__ == "__main__":
    main()
