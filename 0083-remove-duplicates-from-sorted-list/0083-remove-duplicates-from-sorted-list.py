# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # Initialize current pointer to the head of the list
        cur = head
        
        while cur: 
            
            # While next node and its value = current node
            while cur.next and cur.next.val == cur.val: 
                # Skip the next node
                cur.next = cur.next.next
            # Move to the next distinct node
            cur = cur.next
            
        # Return the head of the modified list
        return head