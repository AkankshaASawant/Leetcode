# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # Initialize two pointers, one for each linked list
        l1, l2 = headA, headB
        
        # Continue until l1 and l2 meet at the same node
        while l1 != l2:
            # If l1 reaches end of list A, point it to head of list B
            # Otherwise, move to next node in list A
            l1 = l1.next if l1 else headB
            
            # If l2 reaches end of list B, point it to head of list A
            # Otherwise, move to next node in list B
            l2 = l2.next if l2 else headA
            
        return l1