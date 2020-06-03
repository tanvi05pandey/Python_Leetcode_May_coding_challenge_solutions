# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
import collections


def canConstruct(ransomNote, magazine):
    # r = sorted(ransomNote)
    # m = sorted(magazine, reverse=True)
    # for c in r:
    #     if c in m:
    #         m.pop()
    #     else: return False
    # return True
    # for c in ransomNote:
    #     if c in magazine and ransomNote.count(c) <= magazine.count(c):
    #         continue
    #     else: return False
    # return True
    # ran_d = dict()
    # mag_d = dict()
    # for c in ransomNote:
    #     if c in ran_d:
    #         ran_d[c] += 1
    #     else: ran_d[c] = 1
    # for c in magazine:
    #     if c in mag_d:
    #         mag_d[c] += 1
    #     else: mag_d[c] = 1
    # for key in ran_d:
    #     if key in mag_d and ran_d[key] <= mag_d[key]:
    #         continue
    #     else: return False
    # return True

    freq_ransomNote = collections.Counter(ransomNote)
    freq_magzine = collections.Counter(magazine)
    return not(freq_ransomNote - freq_magzine)


print(canConstruct("fihjjei","hjibagacbhadfaefdjaeaebgi"))