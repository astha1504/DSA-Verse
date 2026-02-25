class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sorting(x):
            count=bin(x).count('1')
            return (count,x)
        arr.sort(key=sorting)
        return arr
