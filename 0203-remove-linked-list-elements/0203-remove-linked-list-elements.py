# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(next = head)
        
        # Use two pointers to traverse and modify the list
        prev, cur = dummy, head
        
        while cur: 
            # Store the next node before potential modification
            nxt = cur.next
            
            # If current node's value matches target, skip it
            if cur.val == val: 
                prev.next = nxt
            else: 
                # Move previous pointer if node is not removed
                prev = cur
                
            # Move to next node
            cur = nxt
        
        # Return modified list, skipping dummy node
        return dummy.next