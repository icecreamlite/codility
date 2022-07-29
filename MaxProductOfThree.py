"""
Sort
Normally, the max product is product of last 3
But first 2 elem can be negative that when multiplied becomes positive
"""

def solution(A):
    A.sort()
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])