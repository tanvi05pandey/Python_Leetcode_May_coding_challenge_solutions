# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
import collections


def firstUniqChar(s):
    # d = dict()
    # for c in s:
    #     if c in d:
    #         d[c] += 1
    #     else: d[c] = 1
    # for k, v in d.items():
    #     if v == 1:
    #         return s.index(k)
    # return -1

    c = collections.Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("loveleetcode"))