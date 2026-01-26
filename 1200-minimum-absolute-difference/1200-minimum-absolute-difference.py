class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        md=min(arr[i+1] - arr[i] for i in range(len(arr)-1))
        return [[arr[i], arr[i+1]] for i in range(len(arr)-1) if arr[i+1] - arr[i] == md]
