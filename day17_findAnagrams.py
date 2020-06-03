# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
from collections import Counter


def findAnagrams(s, p):
    n = len(s)
    m = len(p)

    p = Counter(p)                    # Convert list of anagram letters to a Counter (hashtable)
    ans = []

    window = None
    for i in range(0,n-m+1):
        if i == 0:
            window = Counter(s[:m])   # Initialize window with beginning of s => length = length of anagram letters
        else:
            window[s[i-1]] -= 1       # Move window to right: 1. remove character on the left
            window[s[i+m-1]] += 1     #                       2. add character on the right
        if len(window - p) == 0:      # Check if window is anagram (direct comparison of counters does not work with 0 entries)
            ans.append(i)

    return ans


print(findAnagrams('cbaebabacd', 'abc'))
