class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre=0
        minpre=0
        for num in nums:
            pre+=num
            minpre=min(pre,minpre)
        return 1-minpre

        