class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        odd=0
        even=0
        for i in nums:
            odd=(odd^i)&~even
            even=(even^i)&~odd
        return odd