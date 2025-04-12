def solve():
    T = int(input().strip())
    
    def find_set(x, parent):
        if parent[x] != x:
            parent[x] = find_set(parent[x], parent)
        return parent[x]

    def union(x, y, parent, forced_word):
        rx, ry = find_set(x, parent), find_set(y, parent)
        if rx != ry:
            if forced_word[rx] is not None and forced_word[ry] is not None:
                if forced_word[rx] != forced_word[ry]:
                    return False
            if forced_word[rx] is None:
                forced_word[rx] = forced_word[ry]
            parent[ry] = rx
        return True

    def force(var_id, w, parent, forced_word):
        r = find_set(var_id, parent)
        if forced_word[r] is None:
            forced_word[r] = w
        else:
            if forced_word[r] != w:
                return False
        return True

    for _ in range(T):
        pattern1 = input().split()
        pattern2 = input().split()

        if len(pattern1) != len(pattern2):
            print("-")
            continue

        placeholder_map_1 = {}
        placeholder_map_2 = {}

        parent = []
        forced_word = []  
        next_id = 0

        def make_var():
            nonlocal next_id
            var_id = next_id
            next_id += 1
            parent.append(var_id)
            forced_word.append(None)
            return var_id

        def get_var_id_1(name):
            if name not in placeholder_map_1:
                placeholder_map_1[name] = make_var()
            return placeholder_map_1[name]

        def get_var_id_2(name):
            if name not in placeholder_map_2:
                placeholder_map_2[name] = make_var()
            return placeholder_map_2[name]

        conflict = False
        n = len(pattern1)

        for i in range(n):
            t1 = pattern1[i]
            t2 = pattern2[i]
            
            is_placeholder_1 = (len(t1) >= 2 and t1[0] == '<' and t1[-1] == '>')
            is_placeholder_2 = (len(t2) >= 2 and t2[0] == '<' and t2[-1] == '>')

            if not is_placeholder_1 and not is_placeholder_2:
                if t1 != t2:
                    conflict = True
                    break
            elif is_placeholder_1 and not is_placeholder_2:
                var_id = get_var_id_1(t1[1:-1])
                if not force(var_id, t2, parent, forced_word):
                    conflict = True
                    break
            elif not is_placeholder_1 and is_placeholder_2:
                var_id = get_var_id_2(t2[1:-1])
                if not force(var_id, t1, parent, forced_word):
                    conflict = True
                    break
            else:
                var1 = get_var_id_1(t1[1:-1])
                var2 = get_var_id_2(t2[1:-1])
                if not union(var1, var2, parent, forced_word):
                    conflict = True
                    break
        
        if conflict:
            print("-")
            continue


        def final_word_for_placeholder_1(name):
            var_id = placeholder_map_1[name]
            r = find_set(var_id, parent)
            if forced_word[r] is None:
                forced_word[r] = "a"
            return forced_word[r]

        result = []
        for token in pattern1:
            if len(token) >= 2 and token[0] == '<' and token[-1] == '>':
                placeholder_name = token[1:-1]
                result.append(final_word_for_placeholder_1(placeholder_name))
            else:
                result.append(token)

        print(" ".join(result))
solve()