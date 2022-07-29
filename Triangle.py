def solution(A):
    # remove 0 and negative and sort in descending order
    A = sorted([x for x in A if x > 0], reverse=True)

    # check all 3 consecutive elements
    for i in range(len(A) - 2):
        if A[i + 2] + A[i + 1] > A[i]:
            return 1 # sum of 2 smaller legs > longest leg is triangle

    return 0