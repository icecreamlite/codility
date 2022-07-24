def solution(A):
    dic = {}

    # save integers count in a dictionary in one pass
    for num in A:
        try:
            dic[num] += 1
        except:
            dic[num] = 1

    for k, v in dic.items():
        # if value is odd, that key has an unpaired entry
        if v % 2:
            return k