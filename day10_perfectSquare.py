# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Output: true

def isPerfectSquare(num):
    # i = 1
    # while i * i <= num:
    #
    #     # If (i * i = n)
    #     if (num % i == 0) and (num / i == i):
    #         return True
    #
    #     i = i + 1
    # return False

   # much better solution:

    # a = num**0.5
    # if a == int(a):
    #     return True
    # else:
    #     return False

    # another better approach than above using binary search algo:

    l = 1
    r = num
    while r >= l:
        mid = int((l + r) / 2)
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            r = mid - 1
        else:
            l = mid + 1
    return False


print(isPerfectSquare(175325))