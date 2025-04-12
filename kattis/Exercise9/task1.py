import sys


def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])              
    
    idx = 1                            
    out = []                           
    
    for _ in range(t):
        l = int(input_data[idx]); idx += 1   
        s = int(input_data[idx]); idx += 1   
        final_string = [None] * l
        impossible = False
        
        for _suf in range(s):
            p = int(input_data[idx]); idx += 1
            suffix = input_data[idx]; idx += 1
            
            start_index = p - 1 
            
            star_pos = suffix.find('*')
            if star_pos == -1:
                if start_index + len(suffix) != l:
                    impossible = True
                else:
                    for i, ch in enumerate(suffix):
                        pos = start_index + i
                        if final_string[pos] is None:
                            final_string[pos] = ch
                        elif final_string[pos] != ch:
                            impossible = True
                if impossible:
                    pass
            else:
                left = suffix[:star_pos]
                right = suffix[star_pos+1:]
                
                L = len(left)
                R = len(right)
                total_len = l - start_index
                star_len = total_len - (L + R)
                
                if star_len < 0:
                    impossible = True
                else:
                    for i, ch in enumerate(left):
                        pos = start_index + i
                        if pos >= l:
                            impossible = True
                            break
                        if final_string[pos] is None:
                            final_string[pos] = ch
                        elif final_string[pos] != ch:
                            impossible = True
                            break
                    for i in range(R):
                        ch = right[-1 - i]
                        pos = l - 1 - i
                        if pos < start_index:
                            impossible = True
                            break
                        if final_string[pos] is None:
                            final_string[pos] = ch
                        elif final_string[pos] != ch:
                            impossible = True
                            break
                if impossible:
                    pass
        
        if not impossible and None not in final_string:
            out.append("".join(final_string))
        else:
            out.append("IMPOSSIBLE")
    
    print("\n".join(out))
solve()