# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.'
#    ' Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a"
# is considered a different type of stone from "A".

# Input: J = "z", S = "ZZ"
# Output: 0

def numJewelsInStones(J, S) -> int:
    count=0
    for stone in S:
        if stone in J:
            count += 1
    return count

print(numJewelsInStones('aA', 'aAAbbbb'))