class MinStack:
    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.m) == 0:
            self.m.append(val)
        else:
            self.m.append(min(val, self.m[-1]))

    def pop(self) -> None:
        val = self.s.pop()
        self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
