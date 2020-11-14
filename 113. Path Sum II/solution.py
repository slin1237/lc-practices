from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# noinspection PyTypeChecker
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
        :param root: Tree root
        :param sum: target sum
        :return: list of paths that combines to target sum
        """

        def build_paths(node: TreeNode, path: List[int], path_list: List[List[int]], sums: int):
            if not node:
                return
            path.append(node.val)
            sums -= node.val
            if not node.left and not node.right and sums == 0:
                path_list.append(list(path))
            else:
                build_paths(node.right, path, path_list, sums)
                build_paths(node.left, path, path_list, sums)
            path.pop()

        paths = []
        build_paths(root, [], paths, sum)
        return paths
