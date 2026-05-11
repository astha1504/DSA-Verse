class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            for d in str(x):
                ans.append(int(d))
        return ans
