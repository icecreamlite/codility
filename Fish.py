def solution(A, B):
    alive = len(A)
    down_stack = []

    for ind, fish in enumerate(A):
        if B[ind]: # if fish downstream, add to stack
            down_stack.append(fish)
        else: 
            while down_stack: # if found upstream and there are fish downstream
                alive -= 1 # one will be eaten
                if fish > down_stack[-1]:
                    # if downstream fish is eaten, pop it from stack and check next in stack
                    down_stack.pop()
                else:
                    # else, upstream is eaten and check next fish
                    break

    return alive