class Solution:
    def sumFourDivisors(self, nums):
        def isp(x):
            if x < 2: return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True
        tot = 0
        for n in nums:
            r = round(n ** (1/3))
            if r ** 3 == n and isp(r):
                tot += 1 + r + r*r + r**3
                continue
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    j = n // i
                    if i != j and isp(i) and isp(j):
                        tot += 1 + i + j + n
                    break
        return tot
