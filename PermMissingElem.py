def solution(A):
    N = len(A)
    if N == 0:
        return 1
    
    return int((N+1) * (N / 2 + 1) - sum(A))