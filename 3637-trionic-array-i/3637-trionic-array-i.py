class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == 0 or i == n-1:
            return False
        j = i
        while j+1 < n and nums[j] > nums[j+1]:
            j += 1
        if j == i or j == n-1:
            return False
        while j+1 < n and nums[j] < nums[j+1]:
            j += 1
        return j == n-1
