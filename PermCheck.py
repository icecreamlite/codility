def solution(A):
    # create a container list with # of elem = len(A) with default value False
    container = [False] * len(A)

    for num in A:
        # if it accessed an index > len(A) - 1, current num exceeds len of A
        # and that would mean a missing value in between
        try:
            if container[num-1]: # if True, num is already encountered
                return 0
            else:
                container[num-1] = True
        except:
            return 0

    return 1