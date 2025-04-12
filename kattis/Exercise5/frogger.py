def solve():
    import sys
    from collections import deque
    
    input_data = sys.stdin.read().strip().split()
    scenarios = int(input_data[0])
    idx = 1  # pointer to current position in input_data
    
    for _ in range(scenarios):
        x = int(input_data[idx]); idx+=1  # max number of rounds allowed
        n = int(input_data[idx]); idx+=1  # number of lanes
        m = int(input_data[idx]); idx+=1  # length of each lane
        
        lines = input_data[idx:idx + (n+2)]
        idx += (n+2)
        
        top_curb = lines[0]
        bottom_curb = lines[n+1]
        
        g_col = top_curb.index('G')
        f_col = bottom_curb.index('F')
        
        lane_strings = lines[1:n+1]
        lane_strings.reverse()

        carPos = [[[False]*m for _ in range(m)] for _ in range(n)]
        
        # Fill carPos for t=0 from input, then shift left/right for t=1..m-1
        for i in range(n):
            row_str = lane_strings[i]
            for c in range(m):
                if row_str[c] == 'X':
                    carPos[i][0][c] = True
            

            direction = 1 if (i % 2 == 0) else -1
            
            for t in range(1, m):
                for c in range(m):
                    old_col = (c - direction) % m
                    carPos[i][t][c] = carPos[i][t-1][old_col]
        
        visited = [[[False]*m for _ in range(m+2)] for _ in range(n+2)]
        
        queue = deque()
        
        queue.append((n+1, f_col, 0, 0))
        visited[n+1][f_col][0] = True
        
        def safe_move(r, c, nr, nc, t):

            if not (0 <= nr <= n+1):
                return False
            if not (0 <= nc < m):
                return False
            
            if nr == 0 or nr == n+1:
                return True
            
            lane_i = nr - 1  # lane index 0..n-1
            next_t = (t + 1) % m
            if carPos[lane_i][next_t][nc]:
                return False
            

            if r == nr and c != nc:
                direction_frog = nc - c   # +1 => frog moves right, -1 => left
                lane_direction = 1 if (lane_i % 2 == 0) else -1

                if carPos[lane_i][t][nc]:
                    if direction_frog * lane_direction != -1:
                        return False
            
            return True
        
        answer = None
        
        while queue:
            r, c, t_mod, steps = queue.popleft()
            
            if r == 0 and c == g_col:
                answer = steps
                break
            
            if steps == x:
                continue
            
            for dr, dc in [(0,0), (-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= (n+1) and 0 <= nc < m:
                    if safe_move(r, c, nr, nc, t_mod):
                        nt = (t_mod + 1) % m
                        if not visited[nr][nc][nt]:
                            visited[nr][nc][nt] = True
                            queue.append((nr, nc, nt, steps + 1))
        
        if answer is not None:
            print(f"The minimum number of turns is {answer}.")
        else:
            print("The problem has no solution.")
solve()