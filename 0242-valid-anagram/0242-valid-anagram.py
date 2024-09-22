class Solution(object):
    def isAnagram(self, s, t):
        ''' Anagram: A word or phrase formed by rearranging the 
        letters of a different word or phrase, typically using 
        all the original letters exactly once.'''

        ''' use sorted function to sort the two strings and 
        return if they are anagram or not.'''
        return sorted(s) == sorted(t)

        ''' use Counter function to Creates a dictionary-like 
        object where keys are the items being counted and values 
        are their counts.
        Automatically initializes new items with a count of 0.
        Provides convenient methods for counting and manipulating 
        counted data'''
        return Counter(s) == Counter(t)

        ''' use hashmaps and then compare them with eachother, 
        first by the length and then by the characters'''
        if len(s) != len(t): 
            return False
        countS, countT = {}, {}

        for i in range(len(s)): 
            countS[s[i]] = countS.get(s[i], 0)
            countT[t[i]] = countS.get(t[i], 0)
        for c in countS: 
            if countS[c] != countT.get(c, 0): 
                return False
        return True
        
        