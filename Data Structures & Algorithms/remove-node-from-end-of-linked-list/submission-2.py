# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        removeIndex = length - n
        i = 0
        curr = head
        if removeIndex == 0:
            return head.next
        while curr:
            i += 1
            if i == removeIndex:
                curr.next = curr.next.next
            curr = curr.next
        return head
