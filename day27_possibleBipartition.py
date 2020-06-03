# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group.
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
# Example 1:
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#
# Example 2:
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
import collections


def possibleBipartition(N, dislikes):
    NOT_COLORED, GREEN, BLUE = 0, -1, 1

    def helper(person_id, color):
        colored_table[person_id] = color

        for other_person in dislike_table[person_id]:
            if colored_table[other_person] == color:
                return False
            if colored_table[other_person] == NOT_COLORED and (not(helper(other_person, -color))):
                return False
        return True

    # create a dislike table and colored table
    dislike_table = collections.defaultdict(list)
    colored_table = [NOT_COLORED for _ in range(N+1)]

    for p1, p2 in dislikes:
        # p1 and p2 dislike each other
        dislike_table[p1].append(p2)
        dislike_table[p2].append(p1)

    for person_id in range(1, N+1):
        if colored_table[person_id] == NOT_COLORED and (not helper(person_id, BLUE)):
            return False
    return True



print(possibleBipartition(4, [[1,2],[1,3],[2,4]]))