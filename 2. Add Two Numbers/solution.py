from lst.list_node import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :param l1: ListNode of a number
        :param l2: ListNode of a number
        :return: sum of two ListNode
        """
        dummy_node = ListNode(0)
        head = dummy_node
        carry = 0
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            head.next = ListNode(sum % 10)
            head = head.next
            carry = int(sum / 10)
        if carry == 1:
            head.next = ListNode(1)
        return dummy_node.next