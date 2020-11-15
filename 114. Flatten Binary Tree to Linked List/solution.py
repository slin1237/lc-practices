# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Given a binary tree, flatten it to a linked list in-place.
        :param root: root of a bst
        :return: None
        """
        if not root:
            return
        que = [root]
        pre = None
        while que:
            node = que.pop()
            if pre:
                pre.left = None
                pre.right = node
            if node.right:
                que.append(node.right)
            if node.left:
                que.append(node.left)
            pre = node
