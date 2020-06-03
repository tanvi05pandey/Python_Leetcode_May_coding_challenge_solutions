# In a town, there are N people labelled from 1 to N.
# There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing
# that the person labelled a trusts the person labelled b.
#
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
#
# Example 1:
#
# Input: N = 2, trust = [[1,2]]
# Output: 2
# Example 2:
#
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
#
# Example 3:
#
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

def findJudge(N, trust):
    # d = dict()
    # if not trust and N==1:
    #     return 1
    # for p in trust:
    #     if p[0] in d:
    #         d[p[0]] -= 1
    #     else:
    #         d[p[0]] = -1
    #     if p[1] in d:
    #         d[p[1]] += 1
    #     else: d[p[1]] = 1
    # for k in d.keys():
    #     if d[k] == N-1:
    #         return k
    # return -1

    if not N:
        return -1
    mapper = {}
    for i in range(1, N+1):
        mapper[i] = 0
    for trusts, trustee in trust:
        mapper[trustee] += 1
        mapper[trusts] -= 1

    for key, val in mapper.items():
        if val == N-1:
            return key
    return -1


print(findJudge(3, [[1,3],[2,3]]))