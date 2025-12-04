class Solution:
    def countCollisions(self, directions: str) -> int:
        i=0
        j=len(directions)-1
        while i<len(directions) and directions[i]=='L':
            i+=1
        while j >= 0 and directions[j]=='R':
            j-=1
        return sum(directions[k] != 'S' for k in range(i,j+1))
