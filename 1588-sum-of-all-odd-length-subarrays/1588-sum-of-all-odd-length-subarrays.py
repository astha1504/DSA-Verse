class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        total=0
        for i in range(n):
            for j in range(0,n):
                subarray=arr[i:j+1] 
                if len(subarray)%2==1:
                    total+=sum(subarray)
        return total               
        