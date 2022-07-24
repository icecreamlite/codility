def solution(N):
    a = str(bin(N))
    ans = 0
    counter = 0
    try:
        # start counting after the first '1'
        # used try-except since 'after' does not exist if first '1' is at the end of the binary string (e.g 0b1)
        for ch in a[a.index('1') + 1:]:
            # if current ch is 1, replace ans with counter if counter is greater than ans, reset counter
            if ch == '1':
                if counter > ans:
                    ans = counter
                counter = 0
            else:
                # add 1 to zero count
                counter += 1
    except:
        pass
    
    return ans