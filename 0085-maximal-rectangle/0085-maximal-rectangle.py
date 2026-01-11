class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        max_area = 0
        
        for row in matrix:
            # Step 1: Update heights
            for j in range(m):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Step 2: Largest Rectangle in Histogram
            stack = []
            for i in range(m + 1):
                h = heights[i] if i < m else 0
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        
        return max_area
        