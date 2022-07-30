def solution(S):
    # if length is odd, atleast one bracket will not be closed
    if len(S) % 2:
        return 0

    opening = "({["
    closing = ")}]"

    stack = [] # stack for all opening brackets found
    for ind, ch in enumerate(S): 
        if opening.find(ch) == -1: # if not opening
            try:
                if stack.pop() != opening[closing.find(ch)]:
                    # closing bracket does not correspond to last opening bracket
                    return 0
            except:
                # if stack is empty and found closing bracket
                return 0
        else:
            stack.append(ch) # add opening to stack

            if len(stack) > len(S) - ind - 1:
                # number of brackets in stack is greater than remaining brackets to check
                return 0

    # all brackets are closed
    return 1