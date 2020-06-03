# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#         3
#         / \
#         1   4
#         \
#         2
# Output: 1

# Definition for a binary tree node.

# The below solution is based on the fact that Inorder traversal of a BST results in a sorted array.
# We keep a count variable to keep track of kth value so that as soon as count becomes equal to k, we exit from the loop
# and do not continue with the traversal of the complete tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.ans = 0
        self.count = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.inorder(root, k)
        return self.ans

    def inorder(self, root, k):
        if not root: return

        self.inorder(root.left, k)
        self.count += 1
        if self.count == k:
            self.ans = root.val
            return self.ans
        self.inorder(root.right, k)
