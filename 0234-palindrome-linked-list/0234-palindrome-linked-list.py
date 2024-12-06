# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 
        nums = []                  # Initialize an empty list to store linked list values
        
        while head:                # Traverse the entire linked list
            nums.append(head.val)  # Add each node's value to the list
            head = head.next       # Move to the next node
    
        l, r = 0, len(nums) - 1    # Set two pointers at the start and end of the list
    
        while l <= r:              # Compare elements from both ends moving inwards
            if nums[l] != nums[r]: # If any pair of elements don't match
                return False       # It's not a palindrome
            l += 1                 # Move left pointer right
            r -= 1                 # Move right pointer left
        return True  