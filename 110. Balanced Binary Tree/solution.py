# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.
        :param root: Tree node root
        :return: true if balanced, false otherwise
        """

        def update_dep(node: TreeNode):
            if not node:
                return 0
            node.dep = 1 + max(update_dep(node.left), update_dep(node.right))
            return node.dep

        def validate_depth(node: TreeNode) -> bool:
            if not node or not node.left and not node.right:
                return True
            if not node.left:
                return node.right.dep <= 1
            if not node.right:
                return node.left.dep <= 1
            return abs(node.left.dep - node.right.dep) <= 1 and validate_depth(node.left) and validate_depth(node.right)

        update_dep(root)
        return validate_depth(root)
