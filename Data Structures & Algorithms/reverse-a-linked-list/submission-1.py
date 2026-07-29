# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head

        if head.next:
            # "reverse the rest, then fix the pointer for the current node."
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None 

        return newHead 

        