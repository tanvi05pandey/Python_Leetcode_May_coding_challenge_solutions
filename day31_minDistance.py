# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# ---------- Explanation ------------ #

# Case 1:-
# w1 = ab,  w2 = ""
# result = 2.
# we can convert w1 to w2 by
# deleting all the characters in w1.
# So, result is 2.

# Case 2:-
# w1 = "", w2 = ab
# we can convert w1 to w2,
# by inserting a and b it w1.
# So, result is 2.

# Case 3:-
# w1 = a,  w2 = a
# w1 and w2 are equal.
# So, result is 0.
#
# Case 4:-
# w1 = a,  w2 = b
# Here, w1 and w2 are not equal.
# So, What to do now.
# We have three operations
# 1. insert
# 2. delete
# 3. replace
# perform three operations on w1.
# and take minimum result.
#
# w1 = a,  w2 = b.
# index1 = 0
# index2 = 0
# operations = 0
#
# 1.insert
#
# insert b to w1.
# So, w1 = ba, w2 = b
# operations is increased by since we have inserted a character.
# operations = 1
# Now, w1[index1] == w2[index2],
# So, ignore those characters and check remaining characters.
# So, w1 = a, w2 = "" (after ignoring first characters as they are same)
# This is same as case 1.
# we can w2 from w1 by deleting 'a'.
# So, delete 'a'
# - >  operations = 2.
#
# 2. Delete:-
#
# w1 = a, w2 = b, operations = 0
# delete a character from w1
# So, operations = 1
# w1 = "", w2 = b
# this is same as case 2.
# we can w2 from w1 by inserting 'b' to w1.
# So, insert 'b'.
# - > operations = 2.
#
# 3. replace:
#
# w1 = a, w2 = b, operations = 0
# replace a with b.
#     operations = 1.
# w1 = w2
# So, operations = 1.
#
# Now, choose minimum of (insert, delete, replace) = min(2, 2, 1)
#
# So, result = 1 to convert a to b.

def minDistance(word1, word2):
    M, N = len(word1), len(word2)
    if M * N == 0:
        return M + N
    dp = [[0] * (N + 1) for i in range(M + 1)]

    for i in range(M + 1):
        dp[i][0] = i
    for i in range(N + 1):
        dp[0][i] = i
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]))
    return dp[M][N]

print(minDistance('intention', 'execution'))