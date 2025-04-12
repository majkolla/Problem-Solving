def solve():
    n = int(input())
    V = [int(input()) for _ in range(n)]

    freq = [0] * (n + 2)
    for v in V:
        if v < 1 or v > n + 1:
            print("Error")
            return
        freq[v] += 1


    heap = []
    heap_size = 0

    def heap_push(x):
        nonlocal heap_size
        heap.append(x)
        heap_size += 1
        i = heap_size - 1
        while i > 0:
            p = (i - 1) // 2
            if heap[p] > heap[i]:
                heap[p], heap[i] = heap[i], heap[p]
                i = p
            else:
                break

    def heap_pop():
        nonlocal heap_size
        if heap_size == 0:
            return None
        ret = heap[0]
        heap_size -= 1
        if heap_size > 0:
            heap[0] = heap[heap_size]
            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                if left >= heap_size:
                    break
                smallest = left
                if right < heap_size and heap[right] < heap[left]:
                    smallest = right
                if heap[smallest] < heap[i]:
                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest
                else:
                    break
        heap.pop()  
        return ret

    for i in range(1, n + 1):
        if freq[i] == 0:
            heap_push(i)

    U = []  
    for v in V:
        u = heap_pop()
        if u is None:
            print("Error")
            return
        U.append(u)
        if freq[v] < 1:
            print("Error")
            return
        freq[v] -= 1
        if v <= n and freq[v] == 0:
            heap_push(v)

    for x in freq:
        if x != 0:
            print("Error")
            return

    for leaf in U:
        print(leaf)
solve()