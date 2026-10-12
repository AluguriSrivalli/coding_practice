def appendAndDelete(s, t, k):
    common_length = 0
    max_prefix_limit = min(len(s), len(t))
    
    while common_length < max_prefix_limit and s[common_length] == t[common_length]:
        common_length += 1
        
    min_ops = (len(s) - common_length) + (len(t) - common_length)
    
    # 3. Check the valid conditions
    if k >= len(s) + len(t):
        return "Yes"
    elif k >= min_ops and (k - min_ops) % 2 == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input().strip())
    print(appendAndDelete(s, t, k))

