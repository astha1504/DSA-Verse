
class FreqStack:

    def __init__(self):
        self.st = defaultdict(list) 
        self.freq = defaultdict(int)  
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.st[f].append(val)
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self) -> int:
        x = self.st[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.st[self.maxfreq]:
            self.maxfreq -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()