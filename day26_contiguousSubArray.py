# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.


def findMaxLength(nums):
    count = 0
    d = {0:-1}
    m = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count+=1
        else:
            count-=1
        if count in d:
            print("if:", d)
            m = max(m, i-d[count])
            print("m is: ", m)
        else:

            d[count] = i
            print("else", d)
    return m


#print(findMaxLength([0,1,1,0,1,1,1,0]))
#print(findMaxLength([0,1,0]))
print(findMaxLength([0,0,1,0,0,0,1,1]))