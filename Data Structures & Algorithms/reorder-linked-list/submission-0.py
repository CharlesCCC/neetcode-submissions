# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle point by use fast/slow pointer 
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next #second half head 
        prev = slow.next = None 
        # reverse second half 
        while second:
            tmp = second.next  #save pointer to tmp 
            second.next = prev  #reverse 
            prev = second 
            second = tmp   #move pointer 
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2 