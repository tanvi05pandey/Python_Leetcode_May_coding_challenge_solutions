# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
#
# Here, a circular array means the end of the array connects to the beginning of the array.
# (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
#
# Also, a subarray may only include each element of the fixed buffer A at most once.
# (Formally, for a subarray C[i], C[i+1], ..., C[j],
# there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
# Example 1:
#
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
#
# Example 2:
#
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
#


# EXPLANATION:-
# EX 1:-
# A = [1, -2, 3, -2]
# max = 3   (This means max subarray sum for normal array)
# min = -2  (This means min subarray sum for normal array)
# sum = 0   (total array sum)
# Maximum Sum = 3 (max)
#
# EX2:-
# A = [5, -3, 5]
# max = 7
# min  = -3
# sum = 7
# maximum subarray sum = 7 - (-3) = 10
#
# EX3:-
# A = [3, -1, 2, -1]
# max = 4
# min = -1
# sum = 3
# maximum subarray sum  = sum - min = 3 - (-1) = 4
#
# EX4:-
# A = [-2, -3, -1]
# max = -1
# min = -6
# sum = -6
# In this example, if we do (sum - min) then result is 0. but there is no subarray with sum 0.
# So, in this case we return max value. that is -1.
#
# From above examples,
# we can understand that
# maximum sum is either max (we get using kadane's algo) or (sum - min).
# There is a special case, if sum == min,
# then maximum sum is max.
#
# Let's develop an algorithm to solve this problem.
# 1. Find maximum subarray sum using kadane's algorithm (max)
# 2. Find minimum subarray sum using kadane's algorithm (min)
# 3. Find total sum of the array (sum)
# 4. Now, if sum == min return max
# 5. Otherwise, return maximum ( max, sum - min )
#
# IF YOU HAVE ANY DOUBTS, FEEL FREE TO ASK
# IF YOU UNDERSTAND, DON'T FORGET TO UPVOTE.
#
# Time :- O(N)
# Space :- O(1)


def maxSubarraySumCircular(A):
    if len(A) == 0:
        return 0
    maxTotal,maxSoFar,minSoFar,minTotal,s = A[0], A[0], A[0], A[0],A[0]
    for i in range(1, len(A)):
        maxSoFar = max(A[i], maxSoFar + A[i])
        maxTotal = max(maxTotal, maxSoFar)

        minSoFar = min(A[i], minSoFar + A[i])
        minTotal = min(minTotal, minSoFar)
        s += A[i]

    if s == minSoFar:
        return maxTotal

    return max(s - minTotal, maxTotal)

print(maxSubarraySumCircular([5,-3,5]))
