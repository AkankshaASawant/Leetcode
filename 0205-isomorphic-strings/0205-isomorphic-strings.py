class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create two hash maps to track character mappings
        mapST, mapTS = {}, {}
        
        # Iterate through both strings simultaneously
        for i in range(len(s)): 
            c1, c2 = s[i], t[i]
            
            # Check for inconsistent mappings
            if ((c1 in mapST and mapST[c1] != c2) or 
               (c2 in mapTS and mapTS[c2] != c1)): 
                # If characters are already mapped to different characters, return False
                return False
            
            # Create bidirectional mappings between characters
            mapST[c1] = c2
            mapTS[c2] = c1
            
        # If all characters can be mapped consistently, return True
        return True