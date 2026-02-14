class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if len(self.s)==0:
            self.s.append((val, val))
        else:
            m = self.s[-1][1]
            if val < m:
                self.s.append((val, val))
            else:
                self.s.append((val, m))

    def pop(self) -> None:
        if len(self.s)>0:
            self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()