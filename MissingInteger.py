def solution(A):
    dic = {}
    for num in A:
        if num > 0: # only create key-value pair for positive integer
            dic[num] = True
        
    len_dic_add_1 = len(dic) + 1
    for i in range(1, len_dic_add_1):
        try:
            dic[i] # try to access item with current positive integer i as key
        except:
            return i # if key does not exist, it is the smallest positive integer that does not occur in A

    return len_dic_add_1 # the smallest is the highest number + 1