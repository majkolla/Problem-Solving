def solve():
    import sys
    
    sys.setrecursionlimit(10**7)
    
    lines = sys.stdin.read().strip().split('\n')
    N = int(lines[0])
    
    dictionary_words = lines[1:N+1]
    candidates = lines[N+1:]
    dict_set = set(dictionary_words)
    MAX_DEPTH = 3
    digits = "0123456789"
    
    def neighbors(word, target):
        n = len(word)
        for i in range(n-1):
            if word[i] != word[i+1]:
                wlist = list(word)
                wlist[i], wlist[i+1] = wlist[i+1], wlist[i]
                yield "".join(wlist)
            else:
                pass
        for i in range(n):
            if target[i] in digits and word[i] != target[i]:
                if word[i] not in digits:  
                    wlist = list(word)
                    wlist[i] = target[i]
                    yield "".join(wlist)

    def can_transform_in_3_or_less(dict_word, candidate):
        if len(dict_word) != len(candidate):
            return False
        
        if dict_word == candidate:
            return True
        
        from collections import deque
        
        visited = set([dict_word])
        queue = deque()
        queue.append((dict_word, 0))
        
        while queue:
            cur, d = queue.popleft()
            if d == MAX_DEPTH:
                continue
            for nxt in neighbors(cur, candidate):
                if nxt == candidate:
                    return True
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, d+1))
        
        return False
    for cand in candidates:
        unacceptable = False        
        for w in dictionary_words:
            if can_transform_in_3_or_less(w, cand):
                unacceptable = True
                break
        
        if not unacceptable:
            print(cand)
solve()