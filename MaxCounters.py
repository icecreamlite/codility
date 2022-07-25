def solution(N, A):
    counters = [0] * (N + 1) # N + 1 elements so numbers can match index
    maximum = 0
    minimum = 0

    for num in A:
        try:
            # should be atleast minimum
            if counters[num] < minimum:
                counters[num] = minimum

            counters[num] += 1

            # track maximum
            if counters[num] > maximum:
                maximum = counters[num]

        except:
            # current num is N + 1
            minimum = maximum

    for ind, elem in enumerate(counters):
        # counters should be atleast minimum
        if elem < minimum:
            counters[ind] = minimum

    return counters[1:] # remove first extra element