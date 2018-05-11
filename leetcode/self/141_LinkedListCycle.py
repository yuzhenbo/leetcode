class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head
        slow = head

        while fast.next is not None and slow.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False