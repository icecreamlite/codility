def solution(X, A):
    leaves = {}

    # mark if leaf is already in position and stop if all positions are filled
    for sec, pos in enumerate(A):
        leaves[pos] = True
        if len(leaves) == X:
            return sec

    return -1