# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # Initialize three pointers: prev -> curr -> nxt
        prev, curr = None, head
        
        # Traverse the linked list
        while curr: 
            nxt = curr.next     # Store the next node in nxt
            curr.next = prev    # Reverse link between curr. and prev nodes
            prev = curr         # Move the prev pointer to the current node
            curr = nxt          # Move the curr pointer to the next node

        # After the loop, prev will point to new head of reversed list    
        return prev    
        