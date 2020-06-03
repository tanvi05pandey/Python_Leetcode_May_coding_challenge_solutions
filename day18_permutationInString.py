# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# # In other words, one of the first string's permutations is the substring of the second string.
# #
# # Example 1:
# #
# # Input: s1 = "ab" s2 = "eidbaooo"
# # Output: True
# # Explanation: s2 contains one permutation of s1 ("ba").
# # Example 2:
# #
# # Input:s1= "ab" s2 = "eidboaoo"
# # Output: False

from collections import Counter


def checkInclusion(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    s1 = Counter(s1)

    window = None

    for i in range(s2_len-s1_len+1):
        if i == 0:
            window = Counter(s2[:s1_len])
        else:
            window[s2[i-1]] -= 1
            window[s2[i+s1_len-1]] += 1
        if len(window - s1) == 0:
            return True
    return False

print(checkInclusion('ab', 'eidbaooo'))

