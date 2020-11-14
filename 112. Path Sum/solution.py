# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        Given a binary tree and a sum,
         determine if the tree has a root-to-leaf path
         such that adding up all the values along the path equals the given sum.
        :param root: root of a tree
        :param sum: target sum
        :return: true if there is a path, false otherwise
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        else:
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
