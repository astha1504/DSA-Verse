from typing import List
from collections import defaultdict

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()

        def union_length(intervals):
            if not intervals:
                return 0
            intervals.sort()
            total = 0
            s, e = intervals[0]
            for a, b in intervals[1:]:
                if a > e:
                    total += e - s
                    s, e = a, b
                else:
                    e = max(e, b)
            return total + (e - s)

        active = defaultdict(int)
        prev_y = events[0][0]
        strips = []
        total_area = 0

        i = 0
        while i < len(events):
            y = events[i][0]
            dy = y - prev_y

            intervals = [iv for iv, c in active.items() if c > 0]
            if dy > 0 and intervals:
                w = union_length(intervals)
                area = w * dy
                strips.append((prev_y, dy, w))
                total_area += area

            while i < len(events) and events[i][0] == y:
                _, t, x1, x2 = events[i]
                active[(x1, x2)] += t
                i += 1

            prev_y = y

        half = total_area / 2
        acc = 0

        for y, h, w in strips:
            if acc + w * h >= half:
                return y + (half - acc) / w
            acc += w * h

        return prev_y
