# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]

# see the explanation of this solution at https://www.youtube.com/watch?v=awxaRgUB4Kw
def countBits(num):
    arr = [None]*(num+1)
    arr[0] = 0
    for i in range(num+1):
        arr[i] = arr[i//2] + i%2
    return arr

print(countBits(6))
