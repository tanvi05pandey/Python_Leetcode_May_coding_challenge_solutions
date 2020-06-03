# Given a non-negative integer num represented as a string, remove k digits from the number
# so that the new number is the smallest possible.
#
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

def removeKdigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and len(stack) > 0 and int(stack[-1]) > int(digit):
            stack.pop()
            k -= 1
        stack.append(digit)
    # while k > 0:
    #     stack.pop()
    #     k -= 1
    if k > 0:
        stack = stack[:-k]
    return "".join(stack).lstrip("0") or "0"


print(removeKdigits("112", 1))