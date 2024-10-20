class Solution(object):
    def getRow(self, rowIndex):
        # Initialize first row of Pascal's Triangle with [1]
        res = [1]
        
        # Generate each row up to the desired rowIndex
        for i in range(rowIndex):
            # Create new row with size = previous_row_length + 1, initialize with zeros
            next_row = [0] * (len(res) + 1)
            
            # Build the next row using values from current row
            for j in range(len(res)):
                # Each element contributes to two positions in the next row:
                # Current position (j) and next position (j+1)
                next_row[j] += res[j]      # Add to current position
                next_row[j + 1] += res[j]  # Add to next position
            
            # Update res to the newly created row
            res = next_row
            
        return res