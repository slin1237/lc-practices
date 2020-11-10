# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.
        :param l1:  linked-list representation of a number
        :param l2: linked-list representation of a number
        :return: linked-list representation of a number of sum of l1 and l2
        """
        result = ListNode(0)
        sum, carry = 0, 0
        dummy = result

        while l1 or l2:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            dummy.next = ListNode(sum % 10)
            dummy = dummy.next
            carry = int(sum / 10)
            sum = 0
        if carry != 0:
            dummy.next = ListNode(1)
        return result.next
