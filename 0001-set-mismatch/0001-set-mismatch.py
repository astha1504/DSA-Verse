class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        duplicate = -1
        total = len(nums)
        
        for x in nums:
            if x in s:
                duplicate = x
            s.add(x)
        
        # Missing number = the one NOT in the set
        for i in range(1, total + 1):
            if i not in s:
                return [duplicate, i]
