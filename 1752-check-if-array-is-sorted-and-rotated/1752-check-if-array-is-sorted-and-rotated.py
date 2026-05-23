class Solution:
    def check(self, nums: List[int]) -> bool:
        a = sorted(nums)
        for _ in range(len(nums)):
            if nums==a:
                return True
            nums = nums[1:] + [nums[0]]

        return False