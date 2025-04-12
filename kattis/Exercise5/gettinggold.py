def solve():
    import sys
    from collections import deque
    
    data = sys.stdin.read().strip().splitlines()
    W, H = map(int, data[0].split())
    grid = data[1:]
    
    start_r = start_c = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 'P':
                start_r, start_c = r, c
                break
        if start_r is not None:
            break
    
    def adjacent_to_trap(r, c):
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            rr, cc = r + dr, c + dc
            if grid[rr][cc] == 'T':
                return True
        return False
    
    visited = set()
    queue = deque()
    visited.add((start_r, start_c))
    queue.append((start_r, start_c))
    
    while queue:
        r, c = queue.popleft()

        if adjacent_to_trap(r, c):
            continue
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            rr, cc = r + dr, c + dc
            if grid[rr][cc] != '#' and (rr, cc) not in visited:
                visited.add((rr, cc))
                queue.append((rr, cc))
    
    gold_count = sum(grid[r][c] == 'G' for (r, c) in visited)
    print(gold_count)
solve()