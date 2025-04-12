import sys

#
# Fenwick (Binary Indexed) Tree for point‐updates and prefix‐sum queries
#
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.data = [0]*(size+1)  # 1-based indexing
    
    def update(self, i, delta):
        # Add `delta` to position `i`
        while i <= self.size:
            self.data[i] += delta
            i += i & -i
    
    def query(self, i):
        # Returns sum from 1..i
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    
    def range_query(self, l, r):
        # sum in [l..r]
        return self.query(r) - self.query(l-1)

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])  # number of test cases
    ptr = 1
    
    out = []
    for _ in range(t):
        m = int(input_data[ptr]); ptr+=1
        r = int(input_data[ptr]); ptr+=1
        
        requests = list(map(int, input_data[ptr:ptr+r]))
        ptr += r
        
        # We only need FenwickTree up to m + r, because in the worst
        # case we will assign new "top" heights up to m+r.
        # Initialize Fenwicks with 0 counts
        F = FenwickTree(m + r)
        
        # 'pos[label]' will hold the current "height" of that DVD.
        pos = [0]*(m+1)
        
        # Assign initial heights: label i at height (m - i + 1) or similar,
        # so label 1 => m, label 2 => m-1, ..., label m => 1
        for dvd in range(1, m+1):
            p = m - dvd + 1
            pos[dvd] = p
            F.update(p, 1)
        
        # The highest "top" so far is m.
        # Next new top‐height we assign will be (m+1), then (m+2), etc.
        next_top = m
        
        result = []
        
        # Process each locate‐request
        for wanted in requests:
            curr_height = pos[wanted]
            # Number of movies above = total in [1..next_top] - total in [1..curr_height]
            above = F.query(next_top) - F.query(curr_height)
            result.append(str(above))
            
            # Remove from current height
            F.update(curr_height, -1)
            # Move it to a new top
            next_top += 1
            pos[wanted] = next_top
            F.update(next_top, 1)
        
        out.append(" ".join(result))
    
    print("\n".join(out))
