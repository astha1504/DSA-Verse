from typing import List
import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        heap = []
        max_val = 0
        result = 0
        for start, end, value in events:
            while heap and heap[0][0] < start:
                _, val = heapq.heappop(heap)
                max_val = max(max_val, val)
            result = max(result, value)
            result = max(result, value + max_val)
            heapq.heappush(heap, (end, value))
        return result
