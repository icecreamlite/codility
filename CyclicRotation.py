def solution(A, K):
    if A:
        # execute only if A is non-empty list
        for i in range(K):
            A.insert(0, A.pop())
    return A