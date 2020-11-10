# Definition for a binary tree node.
from typing import List


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

        def inorder(node: TreeNode) -> List[int]:
            """
            Construct inorder array of binary search tree
            :param node:
            :return: array of int
            """
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        def find_swaps(nums: List[int]) -> (int, int):
            """
            Given a sorted array, return the two values that's swapped
            :param nums: list of sorted array
            :return: tuples
            """
            val1 = val2 = -1
            for i in range(len(nums) - 1):
                if nums[i+1] < nums[i]:
                    val2 = nums[i + 1]
                    if val1 == -1:
                        val1 = nums[i]
                    else:
                        break
            return val1, val2

        def recover(node: TreeNode, count: int) -> None:
            """
            Swaps two nodes value in order to recover the tree
            :param node: Tree node
            :param count: number of swaps
            :return: None
            """
            if node:
                if node.val == y or node.val == x:
                    node.val = y if node.val == x else x
                    count += 1
                    if count == 0:
                        return
                recover(node.left, count)
                recover(node.right, count)

        inorder = inorder(root)
        x, y = find_swaps(inorder)
        recover(root, 2)


