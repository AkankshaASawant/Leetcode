# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode() 
        # tail pointer to keep track of last node in merged list
        tail = dummy
        
        # When both lists have elements
        while list1 and list2: 
            
            if list1.val < list2.val:   # If List1's value is smaller,          
                tail.next = list1       # add it to the merged list.
                list1 = list1.next      # Move list1 pointer to the next node
            else: 
                tail.next = list2      # Same for List2
                list2 = list2.next 
            tail = tail.next           # Move tail pointer to newly added node
            
        if list1:                           
            tail.next = list1          # If any elements remain in list1 or in list2,
        elif list2:                    # append them to the merged list
            tail.next = list2

        return dummy.next              # Return the head of the merged list
        