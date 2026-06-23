class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       list2=[]
       for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if nums[i]+nums[j]==target:
                    list2.append(i)
                    list2.append(j)
                j=j+1
       return list2

       

        