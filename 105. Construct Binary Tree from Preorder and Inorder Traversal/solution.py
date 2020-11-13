# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Given preorder and inorder traversal of a tree, construct the binary tree.
        :param preorder: preorder traversal of a tree
        :param inorder: inorder traversal of a tree
        :return: root of binary tree
        """

        def helper(left: int = 0, right: int = len(preorder)) -> TreeNode:
            """
            helper function to construction a tree
            :param left: left bound
            :param right: right bound
            :return: tree node
            """
            nonlocal preorder_index
            if left == right:
                return None
            node_val = preorder[preorder_index]
            node_index = index_map[node_val]
            preorder_index += 1
            node = TreeNode(node_val)
            node.left = helper(left, node_index)
            node.right = helper(node_index+1, right)
            return node

        index_map = {val: index for index, val in enumerate(inorder)}
        preorder_index = 0
        return helper()
