def leader(A):
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

    val_cnt = A.count(value)
    if size > 0 and val_cnt > len(A) // 2:
        # if there is a candidate and its count is > half of elements
        return [val_cnt, value]
    else:
        # no leader
        return [0]

def solution(A):
    ldr = leader(A) # ldr[0] contains leader count, ldr[1] contains the leader
    equi_leader = 0

    if ldr[0]: # there's a leader
        ldr_count = 0

        for ind, elem in enumerate(A):
            if elem == ldr[1]:
                ldr_count += 1 # elem is leader, add to leader count
            if ldr_count > (ind + 1) // 2 and (ldr[0] - ldr_count) > (len(A) - (ind + 1)) // 2:
                # leader count is greater than half of elements in current position
                # and the remaining leader count (ldr[0] - ldr_count) is greater than half
                # of the remaining elements (len(A) - (ind + 1))
                equi_leader += 1
    
    return equi_leader