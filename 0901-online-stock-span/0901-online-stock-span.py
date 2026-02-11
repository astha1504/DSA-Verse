class StockSpanner:

    def __init__(self):
        self.stack = []   # stores (price, index)
        self.i = -1       # current index

    def next(self, price: int) -> int:
        self.i += 1   # move to next day index
        
        # pop all smaller or equal prices
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        # if stack empty -> span = i+1
        if not self.stack:
            span = self.i + 1
        else:
            span = self.i - self.stack[-1][1]
        
        # push current price and index
        self.stack.append((price, self.i))
        
        return span