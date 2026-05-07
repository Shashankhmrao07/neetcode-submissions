"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def inBetweenPointer(self, head):
        temp = head
        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next.next

    def getRandomPointer(self, head):
        temp = head
        while temp:
            copy_node = temp.next
            if temp.random:
                copy_node.random = temp.random.next
            else:
                copy_node.random = None
            temp = temp.next.next

    def getCopyList(self, head):
        temp = head
        current = dummy = Node(temp.val)
        while temp:
            current.next = temp.next
            temp.next = temp.next.next
            current = current.next
            temp = temp.next
        return dummy.next


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        self.inBetweenPointer(head)
        self.getRandomPointer(head)
        return self.getCopyList(head)
        