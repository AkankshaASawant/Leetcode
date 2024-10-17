class Solution(object):
    def generate(self, numRows):
        # Initialize result with first row [1]
        res = [[1]]
        
        # Loop (numRows-1) times to generate remaining rows
        for i in range(numRows - 1): 
            # Add 0s at the beginning and end of the previous row
            # e.g., if previous row is [1,2,1], temp becomes [0,1,2,1,0]
            temp = [0] + res[-1] + [0]
            row = []
            
            # Generate current row by adding adjacent numbers from temp
            # e.g., for [0,1,2,1,0]: 0+1=1, 1+2=3, 2+1=3, 1+0=1
            # resulting in [1,3,3,1]
            for j in range(len(res[-1]) + 1): 
                row.append(temp[j] + temp[j + 1])
            # Add the new row to result
            res.append(row)
        return res