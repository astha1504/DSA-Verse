class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total=sum(apple)
        capacity.sort(reverse=True)
        used=0
        current=0
        for box in capacity:
            current+=box
            used+=1
            if current>=total:
                return used
