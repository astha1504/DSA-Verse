class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def helper(ds, s1):
            if len(s1)==0:
                res.append(ds[:])
                return
            for i in range(len(s1)):
                part=s1[:i+1]
                if part==part[::-1]:
                    ds.append(part)
                    helper(ds,s1[i+1:])
                    ds.pop()
        helper([],s)
        return res
