# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
# Example 1:
#
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
# Example 2:
#
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        treequeue = deque()
        treedict = dict()
        treequeue.append((root, 0, 0))
        while treequeue:
            node, parent, depth = treequeue.popleft()
            if node is not None:
                treedict[node.val] = (parent, depth)
                treequeue.append((node.left, node.val, depth+1))
                treequeue.append((node.right, node.val, depth+1))
        return treedict[x][1] == treedict[y][1] and treedict[x][0] != treedict[y][0]


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(4)
t.right.right = TreeNode(5)

s = Solution()
print(s.isCousins(t, 5, 4))


