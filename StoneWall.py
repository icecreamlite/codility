def solution(H):
    stack = []
    blocks = 0

    for height in H:
        # remove blocks that are higher than the current height
        while stack and height < stack[-1]:
            stack.pop()

        if stack:
            if height > stack[-1]:
                # higher block from last in stack means new block
                # also add current height to stack
                blocks += 1
                stack.append(height)

        else:
            # found new lowest height
            blocks += 1
            stack.append(height)
    
    return blocks