def solution(A):
    ans = 0
    to_east = 0
    for car in A:
        if car:
            ans += to_east
            if ans > 1000000000:
                return -1
        else:
            to_east += 1
    
    return ans