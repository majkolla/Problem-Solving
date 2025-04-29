"""
we want to have a fair distribution of candy but one kid always loses it so we need 
K * X + 1

we can only get candies in C amount 
we want to find B number of bags such that 

B C = K X + 1

so we want B X "tripple equal"  1 mod K

so if gcd(K,C) =! 1 there is no multiplicative inverse 

we also need to make sure that every kid gets more than 1 candy 
so  X = (BC-1)/K so for X to be greater or equal to one we need: 
BC >= K + 1
"""

import sys 
import math 

# implementing the extended euclidian alg
def modinv(a, m): 
    r0 = a
    r1 = m 
    s0 = 1
    s1 = 0
    while r1 != 0:
        q = r0 // r1

        temp_r = r0
        r0 = r1
        r1 = temp_r - q * r1

        temp_s = s0
        s0 = s1
        s1 = temp_s - q * s1
    # r0 is gcd,  s0 is the inverse
    return s0 % m

def solve(K, C): #solve one testcase 

    if K == 1: 
        if C > 1:
            return 1 
        else:
            return 2
    # congruence BC === 1 mode K needs to have gcd = 1 
    if math.gcd(K,C) != 1: 
        return None 
    
    B = modinv(C, K) ##  1 ≤ B ≤ K−1  and  CB === 1 (mod K)
    #the other constrient BC ≥ K + 1

    if B * C <= K: ## not enough candies, continue with next sol
        # since the sol is basically B = B_0 + nK
        # we just wanna find the smallest n such that the ineq is true 
        n = (K + 1 - B * C + K * C - 1) // (K * C)    # round up 
        B += n * K
    if B <= 1000000000: 
        return B 
    else: 
        return None 

def main() -> None:
    data = sys.stdin.read().strip().splitlines()
    t = int(data[0])
    output = []
    for i in range(1, t + 1):
        K_str, C_str = data[i].split()
        K = int(K_str)
        C = int(C_str)
        ans = solve(K, C)
        if ans is not None: 
            output.append(str(ans))
        else: 
            output.append("IMPOSSIBLE")
    sys.stdout.write("\n".join(output))
 
main()