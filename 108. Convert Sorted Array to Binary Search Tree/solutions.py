from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
        :param nums: inorder traversal or a bst
        :return: root node
        """
        def helper(left: int = 0, right: int = len(nums)) -> TreeNode:
            if left == right:
                return None
            node_index = left + (right - left) // 2
            node_val = nums[node_index]
            node = TreeNode(node_val)
            node.left = helper(left, node_index)
            node.right = helper(node_index+1, right)
            return node

        return helper()
