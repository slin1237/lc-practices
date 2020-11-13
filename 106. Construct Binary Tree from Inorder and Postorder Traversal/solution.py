from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Given inorder and postorder traversal of a tree, construct the binary tree.
        :param inorder: inorder traversal of a binary tree
        :param postorder: postorder traversal of a binary tree
        :return: binary tree root node
        """
        def helper(left: int = 0, right: int = len(postorder)) -> TreeNode:
            nonlocal postorder_index
            if left == right:
                return None
            node_val = postorder[postorder_index]
            node_index = index_map[node_val]
            node = TreeNode(node_val)
            postorder_index -= 1
            node.right = helper(node_index+1, right)
            node.left = helper(left, node_index)
            return node

        index_map = {val: index for index, val in enumerate(inorder)}
        postorder_index = len(postorder) - 1
        return helper()