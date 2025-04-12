def solve():
    import sys
    import heapq
    
    data = sys.stdin.read().strip().split()
    c = int(data[0])  # cache capacity
    n = int(data[1])  # number of different objects
    a = int(data[2])  # number of accesses
    
    accesses = list(map(int, data[3:]))

    if c == 0:
        print(a)
        return

    from collections import defaultdict, deque
    future_positions = defaultdict(deque)
    
    for idx, obj in enumerate(accesses):
        future_positions[obj].append(idx)
    
    cache = set()
    heap = []
    
    misses = 0

    for i, obj in enumerate(accesses):

        future_positions[obj].popleft()

        if obj in cache:
            pass
        else:
            misses += 1
            if len(cache) == c:

                while True:
                    neg_next_use, evict_candidate = heapq.heappop(heap)
                    if evict_candidate in cache:
                        if future_positions[evict_candidate]:
                            actual_next_use = future_positions[evict_candidate][0]
                        else:
                            actual_next_use = a  
                        
                        if actual_next_use == -neg_next_use:
                            cache.remove(evict_candidate)
                            break

            
            cache.add(obj)
        
        if future_positions[obj]:
            next_use = future_positions[obj][0]
        else:
            next_use = a
        
        heapq.heappush(heap, (-next_use, obj))

    print(misses)
solve()
