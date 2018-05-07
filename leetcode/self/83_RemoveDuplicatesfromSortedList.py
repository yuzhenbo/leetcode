class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Recursively
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next else head

    # iteratively
    def deleteDuplicates1(self, head):
        cur = head
        while cur:
            # skip all the duplcated nodes of cur
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            # No duplicated nodes, move cur to next node
            cur = cur.next
        return head