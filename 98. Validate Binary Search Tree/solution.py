# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """Given a binary tree, determine if it is a valid binary search tree
            The left subtree of a node contains only nodes with keys less than the node's key.
            The right subtree of a node contains only nodes with keys greater than the node's key.
            Both the left and right subtrees must also be binary search trees.
        :param root: binary tree
        :return: true if tree is binary search tree, false o.w.
        """
        def validate_binary_tree(node: TreeNode,
                                 left_bound=float("-inf"),
                                 right_bound=float("inf")) -> bool:
            """
            Given a tree node, validate if the tree node and leaves formed a binary search tree
            :param left_bound: left bound for node value
            :param right_bound: right bound for node value
            :param node: tree node
            :return: true or false
            """
            if not node:
                return True
            if node.val <= left_bound or node.val >= right_bound:
                return False
            else:
                return validate_binary_tree(node.left, left_bound, node.val) \
                       and validate_binary_tree(node.right, node.val, right_bound)
        return validate_binary_tree(root)
