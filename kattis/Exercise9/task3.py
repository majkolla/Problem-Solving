import sys

def main():
    # Read the dictionary
    dictionary = set()
    possible_lengths = set()
    while True:
        line = sys.stdin.readline().strip()
        if line == '#':
            break
        if line:
            dictionary.add(line)
            possible_lengths.add(len(line))
    possible_lengths = sorted(possible_lengths, reverse=True)  # Check longer lengths first
    
    # Read all remaining lines for messages
    buffer = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        buffer.append(line.rstrip('\n'))
    
    # Process buffer into messages
    all_chars = []
    for line in buffer:
        all_chars.extend(list(line))
    messages = []
    current = []
    for c in all_chars:
        if c == '#':
            break
        if c == '!':
            messages.append(''.join(current))
            current = []
        else:
            current.append(c)
    
    # Process each message using dynamic programming
    for msg in messages:
        n = len(msg)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # Initialize with previous value
            # Check all possible lengths from the dictionary
            for l in possible_lengths:
                if l > i:
                    continue
                start = i - l
                substring = msg[start:i]
                if substring in dictionary:
                    if dp[start] + 1 > dp[i]:
                        dp[i] = dp[start] + 1
        print(dp[n])

main()