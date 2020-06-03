# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3

import collections

def majorityElement(nums):
    nums_count = collections.Counter(nums)
    n = len(nums)
    for item in nums_count.items():
        if item[1] > n//2:
            return item[0]


print(majorityElement([6,5,5]))