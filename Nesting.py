def solution(S):
    if len(S) % 2:
        return 0

    open_count = 0 # stack not, track open parenthesis count
    for ind, ch in enumerate(S):
        if ch == '(':
            open_count += 1
            if open_count > len(S) - ind - 1:
                # count of open parenthesis is greater than remaining chars to check
                return 0
        
        else:
            if open_count:
                open_count -= 1
            else:
                # encountered closing parenthesis but no current open parenthesis
                return 0

    # all parenthesis are closed
    return 1