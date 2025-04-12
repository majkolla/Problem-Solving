import sys 
from collections import Counter #works well here cuz we can check instantly if a palindrome is impossible! 



def min_swaps_to_palindrome(s: str) -> int:
    freq = Counter(s)
    odd_count = sum(count % 2 for count in freq.values())

    if odd_count > 1:
        return -1  
    
    arr = list(s)  
    left = 0 
    right = len(arr) - 1
    swaps = 0
    
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            match_index = right
            while (match_index > left) and (arr[match_index] != arr[left]):
                match_index -= 1
            
            if match_index == left:

                arr[left], arr[left+1] = arr[left+1], arr[left]
                swaps += 1
            else:
                for i in range(match_index, right):
                    arr[i] = arr[i+1]
                    arr[i+1]= arr[i]
                    swaps += 1
                left += 1
                right -= 1
    
    return swaps

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0]) 
    
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        
        answer = min_swaps_to_palindrome(s)
        if answer == -1:
            print("Impossible")
        else:
            print(answer)

solve()