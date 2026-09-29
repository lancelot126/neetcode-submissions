# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        curr = l1
        num1 = 0
        i = 1
        while curr:
            num1 += i * curr.val
            i *= 10
            curr = curr.next
        curr = l2
        num2 = 0
        i = 1
        while curr:
            num2 += i * curr.val
            i *= 10
            curr = curr.next
        res = str(num1 + num2)
        res = "".join(reversed(res))
        for num in res:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next
        
        

