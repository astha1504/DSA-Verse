from typing import List
import heapq

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        base = nums[0]          # first subarray always starts at 0
        need = k - 1            # remaining starts to choose
        
        small = []              # max heap (negative values)
        large = []              # min heap
        small_sum = 0
        ans = float('inf')

        # helper functions
        def add(x):
            nonlocal small_sum
            if len(small) < need:
                heapq.heappush(small, -x)
                small_sum += x
            else:
                if small and x < -small[0]:
                    small_sum += x + heapq.heappop(small)
                    heapq.heappush(small, -x)
                else:
                    heapq.heappush(large, x)

        def remove(x):
            nonlocal small_sum
            if small and x <= -small[0]:
                small_sum -= x
                small.remove(-x)
                heapq.heapify(small)
                if large:
                    y = heapq.heappop(large)
                    heapq.heappush(small, -y)
                    small_sum += y
            else:
                large.remove(x)
                heapq.heapify(large)

        # sliding window
        for i in range(1, n):
            add(nums[i])

            if i > dist:
                remove(nums[i - dist])

            if len(small) == need:
                ans = min(ans, base + small_sum)

        return ans
