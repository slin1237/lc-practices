# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Given a binary tree
        Populate each next pointer to point to its next right node.
        If there is no next right node, the next pointer should be set to NULL.
        :param root: Binary tree root node
        :return: binary root node
        """
        if not root:
            return None
        cur_dep = 0
        que = [(root, 0)]
        pre = None

        for node, dep in que:
            if cur_dep != dep:
                cur_dep = dep
                pre = None
            if pre:
                pre.next = node
                pre = node
            else:
                pre = node
            if node.left:
                que.append((node.left, dep + 1))
            if node.right:
                que.append((node.right, dep + 1))
        return root
