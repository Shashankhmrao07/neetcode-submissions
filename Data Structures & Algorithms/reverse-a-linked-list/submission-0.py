# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            while current != None:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            return previous
        
        