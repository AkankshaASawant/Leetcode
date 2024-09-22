class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {} # value: index

        '''Use enumerate function to To get both the index and 
        value of elements in a loop without manually incrementing 
        a counter.'''
        for i, n in enumerate(nums): 
            diff = target - n
            if diff in hashmap: 
                return [hashmap[diff], i]
            hashmap[n] = i
        return True
        