"""
Smallest average can be found only in 2 or 3-element slice
"""

def solution(A):
    start_pos = 0
    min_ave = 10000 # highest possible ave

    # for N = 2
    if len(A) == 2:
        return 0

    # for N > 2
    for i in range(len(A)-2):
        total = A[i] + A[i+1]
        ave1 = total / 2
        ave2 = (total + A[i+2]) / 3

        ave = min(ave1, ave2)

        if ave < min_ave:
            # lower ave of 2 or 3 elem slice from A[i] is less than current minimum
            min_ave = ave
            start_pos = i

    # check ave of the last 2 elements
    ave = (A[-2] + A[-1]) / 2
    if ave < min_ave:
        start_pos = len(A) - 2

    return start_pos