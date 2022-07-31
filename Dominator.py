"""
As long as there are different elements, remove 2 different elements from the list
The remaining will be the candidate for leader element
"""

def solution(A):
    size = 0 # tracks size of same number that gets reduced when found 2 different number
    for ind, num in enumerate(A):
        if size == 0:
            value = num
            size += 1
            ans = ind
        else:
            if value != num:
                # found 2 different number
                size -= 1
            else:
                # found same number as current value
                size += 1

    if size > 0 and A.count(value) > len(A) // 2:
        # if there is a candidate and its count is > half of elements
        return ans
    else:
        # no leader
        return -1