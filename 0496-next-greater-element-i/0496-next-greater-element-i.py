class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        nextgreater={}
        for num in nums2:
            while s and s[-1] < num:
                nextgreater[s.pop()] = num
            s.append(num)      
        for num in s:
            nextgreater[num]=-1
        ans=[]    
        for num in nums1:
            ans.append(nextgreater[num])
        return ans



