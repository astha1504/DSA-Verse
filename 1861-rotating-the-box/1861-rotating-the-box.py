class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        box=boxGrid
        m, n = len(box), len(box[0])
        for r in range(m):
            fall = n - 1
            for c in range(n-1, -1, -1):
                if box[r][c] == '*':
                    fall = c - 1
                elif box[r][c] == '#':
                    box[r][c], box[r][fall] = '.', '#'
                    fall -= 1
        res = [[None]*m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m-1-r] = box[r][c]
        return res
