class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, self.next)

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


l1 = ListNode(0)
l1.next = ListNode(3)
# l1.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(2)

# l1 = ListNode([1,3,4])
# l2 = ListNode([0,2,3])

print(Solution().mergeTwoLists(l1, l2))