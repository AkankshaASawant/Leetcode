class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize a pointer to the last position of the merged array
        last = m + n - 1
        
        # Compare elements from the end of both arrays
        while m > 0 and n > 0: 
            if nums1[m - 1] > nums2[n - 1]: 
                # If element from nums1 is larger, place it at the end
                nums1[last] = nums1[m - 1]
                m -= 1
            else: 
                # If element from nums2 is larger or equal, place it at the end
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        while n > 0: 
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1