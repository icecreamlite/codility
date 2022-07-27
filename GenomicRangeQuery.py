"""
Create an array consisting of total encountered nucleotides for each type.
Given P[K] and Q[K], you will know if a nucleotide is encountered if the difference
of the count at the given positions are greater than 0.
Start with A as that has the lowest impact.
"""

def solution(S, P, Q):
    ans = []
    dic = {'A':0, 'C':1, 'G':2, 'T':3} # for index not impact factor

    countA, countC, countG, countT = [0], [0], [0], [0]
    sums = [0] * 4 # used to track total encounterd nucleotides at each position

    for nuc in S:
        sums[dic[nuc]] += 1
        for ind, cnt in enumerate((countA, countC, countG, countT)):
            cnt.append(sums[ind])

    for p, q in zip(P, Q):
        if countA[q+1] - countA[p]:
            ans.append(1)
        elif countC[q+1] - countC[p]:
            ans.append(2)
        elif countG[q+1] - countG[p]:
            ans.append(3)
        elif countT[q+1] - countT[p]:
            ans.append(4)

    return ans