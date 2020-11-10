# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Given the root of a binary search tree (BST),
         where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
        :param root: BST tree node
        :return: None
        """
        stack = []
        x = y = pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val < pre.val:
                y = root
                if not x:
                    x = pre
                else:
                    break
            pre = root
            root = root.right
        x.val, y.val = y.val, x.val
