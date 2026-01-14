from typing import List

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

        active = []          # store active intervals explicitly
        strips = []
        total_area = 0

        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y

            if dy > 0 and active:
                w = union_length(active)
                area = w * dy
                strips.append((prev_y, dy, w))
                total_area += area

            # process all events at this y
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                i += 1

            prev_y = y

        half = total_area / 2
        acc = 0

        for y, h, w in strips:
            area = w * h
            if acc + area >= half:
                return y + (half - acc) / w
            acc += area

        return prev_y
