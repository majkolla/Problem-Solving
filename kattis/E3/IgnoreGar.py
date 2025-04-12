def solve():
    import sys
    
    valid_digits = ['0','1','2','5','6','8','9']
    first_digits = ['1','2','5','6','8','9']
    flip_map = {'0':'0','1':'1','2':'2','5':'5','6':'9','8':'8','9':'6'}
    

    
    max_len = 20 
    counts = [0]*(max_len+1)
    

    def count_d_digit(d):
        if d == 1:
            return len(first_digits)
        else:
            return len(first_digits) * (len(valid_digits)**(d-1))
    
    running_sum = 0
    for d in range(1,max_len+1):
        amt = count_d_digit(d)
        running_sum += amt
        counts[d] = running_sum
    
    def find_kth_valid_number(k):
        d = 1
        while d <= max_len and counts[d] < k:
            d += 1
        
        if d == 1:
            offset = k - 1  
        else:
            offset = k - counts[d-1] - 1
        

        
        # First digit:
        if d == 1:
            first = first_digits[offset]  # offset < 6 guaranteed
            return first
        else:
            block_size_for_remaining = (len(valid_digits)**(d-1))
            first_index = offset // (block_size_for_remaining)
            remainder = offset % (block_size_for_remaining)
            
            s = [first_digits[first_index]]
            
            for i in range(d-1):
                block_size_for_next = len(valid_digits)**(d-2 - i)
                digit_index = remainder // block_size_for_next
                remainder = remainder % block_size_for_next
                s.append(valid_digits[digit_index])
            
            return "".join(s)
    
    def flip_number(num_str):
        return "".join(flip_map[d] for d in reversed(num_str))
    
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue
        K = int(line)
        normal_num_str = find_kth_valid_number(K)
        flipped = flip_number(normal_num_str)
        print(flipped)
solve()