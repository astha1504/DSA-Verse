class Solution:
    def largestInteger(self, num: int) -> int:
        arr=list(str(num))
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if (int(arr[i])%2==int(arr[j])%2) and arr[j]>arr[i]:
                            arr[i], arr[j] = arr[j], arr[i]
        return int("".join(arr))
        