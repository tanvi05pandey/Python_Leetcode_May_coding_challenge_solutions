# Given a positive integer, output its complement number. The complement strategy is
# to flip the bits of its binary representation.
#
# Example 1:
#
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
# So you need to output 2.

def findComplement(num):
    importantBits = 0
    temp = num
    while temp != 0:
        temp >>= 1
        importantBits += 1
    mask = (1 << importantBits) - 1
    return (~num) & mask


print(findComplement(5))
