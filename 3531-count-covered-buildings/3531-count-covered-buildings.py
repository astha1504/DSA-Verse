from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        b = set(map(tuple, buildings))
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        
        # Build row and column maps
        for x, y in buildings:
            row_map[x].append(y)
            col_map[y].append(x)
        
        # Sort coordinates for binary search
        for r in row_map:
            row_map[r].sort()
        for c in col_map:
            col_map[c].sort()
        
        count = 0
        for x, y in buildings:
            # Check row (left/right)
            row = row_map[x]
            pos_y = bisect_left(row, y)
            has_left  = pos_y > 0
            has_right = pos_y < len(row) - 1
            
            # Check column (above/below)
            col = col_map[y]
            pos_x = bisect_left(col, x)
            has_above = pos_x > 0
            has_below = pos_x < len(col) - 1
            
            if has_above and has_below and has_left and has_right:
                count += 1
        
        return count
