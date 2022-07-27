"""
Count the number of multiples of K, that are within A and B, inclusive, by subtracting
the quotient (when divided to K) of the highest multiple of K to the quotient of the
lowest multiple of K
"""

import math

def solution(A, B, K):
    return (B // K) - math.ceil(A/K) + 1