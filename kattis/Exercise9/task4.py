import sys
import collections

def solve():
    
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        n = line.strip()
        if not n:
            continue  
        n = int(n)
        if n == 0:
            break  

        sequences = []
        for _ in range(n):
            sequences.append(sys.stdin.readline().strip())
        
        needed = (n // 2) + 1
        
        min_len = 1
        max_len = min(len(s) for s in sequences)  
        best_len = 0
        best_substrings = []

        while min_len <= max_len:
            mid = (min_len + max_len) // 2
            
            freq = collections.Counter()
            

            for s in sequences:
                seen_in_this_string = set()
                for start in range(len(s) - mid + 1):
                    sub = s[start:start+mid]
                    seen_in_this_string.add(sub)
                for sub in seen_in_this_string:
                    freq[sub] += 1
            
            candidates = [sub for (sub, count) in freq.items() if count >= needed]
            
            if candidates:
                best_len = mid
                best_substrings = candidates
                min_len = mid + 1
            else:
                max_len = mid - 1

        if best_len == 0:
            print("?")
        else:
            best_substrings = sorted(set(best_substrings))
            for sub in best_substrings:
                print(sub)
        
        print()  
solve()