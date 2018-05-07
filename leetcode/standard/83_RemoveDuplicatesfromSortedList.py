
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
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            while nextNode:
                # keep traversing till current node and next node's value are unequal
                if nextNode.val == currentNode.val:
                    nextNode = nextNode.next
                else:
                    break
            currentNode.next = nextNode
            currentNode = nextNode
        return head
