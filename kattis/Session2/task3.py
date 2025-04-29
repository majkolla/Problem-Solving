"""
we get independetn test cases and for each case: 
we read n unique phone numbers 
and for every number is a sequence of 10 digits  


so we want to return yes if the data is consistent,
i.e. no number is a prefix of another



idea: 
we sort it, so that we get that if we have prefix number situation we know that theyre
going to be next to eachother, thus 

for an inconstient list there must be an i such that 
sorted[i +1] starts with sorted[i]
"""

import sys


def consistent(phone_numbers):
    """Return True iff the list has no prefix conflicts."""
    phone_numbers.sort()                   
    for a, b in zip(phone_numbers, phone_numbers[1:]): # we combine the adjancent numbers 
        if b.startswith(a):  # this string method returns true if b starts with a,
            return False
    return True

def main(): 
    data = sys.stdin.read().split()
    test_cases = int(data[0])
    idx = 1 
    output = []

    for _ in range(test_cases): 
        n = int(data[idx])
        idx += 1 
        prob = data[idx : idx + n]
        idx += n
        if consistent(prob): 
            output.append("YES")
        else: 
            output.append("NO")
    
    sys.stdout.write("\n".join(output))
main()
