def solution(A):
    ans = 100000000 # max possible sum computed based on the task description
    left_sum = 0
    right_sum = sum(A)

    for num in A[:-1]:
        left_sum += num
        right_sum -= num
        diff = abs(left_sum - right_sum)

        if diff < ans:
            ans = diff

    return ans