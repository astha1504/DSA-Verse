class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        
        return min(digit_sum(x) for x in nums)
