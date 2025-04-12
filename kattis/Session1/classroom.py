import sys
import heapq

input_data = sys.stdin.read().strip().split()
n, k = map(int, input_data[:2])
intervals = []
idx = 2
for _ in range(n):
    s, f = map(int, input_data[idx:idx+2])
    idx += 2
    intervals.append((s, f))

# Sort actiivies by starting time 
intervals.sort(key=lambda x: x[0])

# Min-heap of finish times for the activities currently using a classroom
ongoing = []
scheduled_count = 0

for s, f in intervals:
    # Pop all rooms that finished strictly before this start time
    while ongoing and ongoing[0] < s:
        heapq.heappop(ongoing)
    
    # If we still have space for this activity
    if len(ongoing) < k:
        heapq.heappush(ongoing, f)
        scheduled_count += 1
    # else, we skip this activity (cannot schedule)

print(scheduled_count)

#solve()