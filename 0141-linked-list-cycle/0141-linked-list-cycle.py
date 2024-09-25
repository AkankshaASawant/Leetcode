# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # Initialize two pointers, starting at the head
        slow, fast = head, head

        # Continue as long as fast pointer and its next node exist
        while fast and fast.next:
            slow = slow.next       # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
            
            if slow == fast:       # If slow and fast pointers meet, 
                return True        # then a cycle exists

        return False               # If the loop completes without finding a cycle
        