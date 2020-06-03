# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once. Find this single element that appears only once.
#
#
#
# Example 1:
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

from collections import Counter

def singleNonDuplicate(nums):
    # arr = Counter(nums)
    # for k in arr.keys():
    #     if arr[k] == 1:
    #         return k

    #-----better way using Binary search--------#

    left = 0
    right = len(nums)-1
    while left < right:
        mid = (right + left) // 2
        #middle is even
        if mid % 2 == 0:
            if nums[mid] != nums[mid+1]:
                right = mid
            else:
                left = mid + 2
        #middle is odd
        else:
            if nums[mid] != nums[mid-1]:
                right = mid -1
            else:
                left = mid + 1
    #left == right
    return nums[left]


print(singleNonDuplicate([3,3,7,7,10,11,11]))