# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Given two binary trees, this function checks if they are the same or not.
        :param p: binary tree
        :param q: binary tree
        :return: true if both trees are the same, false o.w.
        """
        if not p and not q:
            return True
        if not q or not p or p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
