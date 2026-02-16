class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower=[]
        for i in range(query_row+1):
            row=[0.0]*(i+1)
            tower.append(row)

        tower[0][0]=poured

        for i in range(query_row):
            for j in range(len(tower[i])):
                if tower[i][j]>1:
                    excess=(tower[i][j]-1)/2.0
                    tower[i+1][j]+=excess
                    tower[i+1][j+1]+=excess

        ans=tower[query_row][query_glass]
        if ans>1:
            return 1.0
        return ans
