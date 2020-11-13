# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Given the head of a singly linked list where elements are sorted in ascending order,
        convert it to a height balanced BST.
        :param head: Head of a sorted linked list
        :return: balanced bst
        """

        def convert_lst_to_arr(node: ListNode) -> List[int]:
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        def convert_arr_to_bst(nums: List[int],
                               left: int,
                               right: int) -> TreeNode:
            if left == right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = convert_arr_to_bst(nums, left, mid)
            node.right = convert_arr_to_bst(nums, mid + 1, right)
            return node

        nums = convert_lst_to_arr(head)
        return convert_arr_to_bst(nums, 0, len(nums))
