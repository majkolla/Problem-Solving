""" 
Jack & Jill has CD
They only sell one of each of the CD they both own
Jack and Jill only owns at most one copy of each CD

Q] How many can they sell? 

Essentialy does jack and jill own the same CD if yes they can sell if no they cannot 

INPUT: 

N and M, where N, M \leq 1 000 000
where N is the number of CDs owned by Jack 
and M is the number of CDs owned by Jill 
then: 
N lines listing catalog numbers of CDs owned by Jack (in increasing order)
M lines listing catalog number of CDs owned by Jill  (in increasing order)

The input is terminated by a line containing two zeros
"""

while True:
    line = input().strip()
    
    N, M = map(int, line.split())
    A, B = N, M
    # Check for termination condition
    if N == 0 and M == 0:
        break
    
    # Read N catalog numbers for Jack
    jack_cds = [int(input().strip()) for _ in range(N)]
    # Read M catalog numbers for Jill
    jill_cds = [int(input().strip()) for _ in range(M)]
    

i = 0
j = 0 
count = 0

while i < len(jack_cds) and j < len(jill_cds):
    if jack_cds[i] == jill_cds[j]:
        count += 1
        i += 1
        j += 1
    elif jack_cds[i] < jill_cds[j]:
        i += 1
    else:
        j += 1

print(count)
