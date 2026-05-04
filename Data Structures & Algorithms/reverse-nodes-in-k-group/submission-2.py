# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, temp):
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return prev

    def findKthNode(self, temp, k):
        k -= 1
        while temp and k > 0:
            k -= 1
            temp = temp.next
        return temp
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode = None
        while temp:
            kth_node = self.findKthNode(temp, k)
            if kth_node == None:
                if prevNode:
                    prevNode.next = temp
                    break
            nextNode = kth_node.next
            kth_node.next = None
            self.reverseLinkedList(temp)
            if head == temp:
                head = kth_node
            else:
                prevNode.next = kth_node
            prevNode = temp
            temp = nextNode
        return head