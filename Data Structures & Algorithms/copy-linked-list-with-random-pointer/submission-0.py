"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        iterator = head
        while iterator:
            copy = Node(iterator.val)
            oldToCopy[iterator] = copy
            iterator = iterator.next
        iterator = head
        while iterator:
            copy = oldToCopy[iterator]
            copy.next = oldToCopy[iterator.next]
            copy.random = oldToCopy[iterator.random]
            iterator = iterator.next
        return oldToCopy[head]
