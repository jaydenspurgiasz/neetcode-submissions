class MinStack:
    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.m) == 0:
            self.m.append(val)
        elif val <= self.m[-1]:
            self.m.append(val)
        else:
            cur = self.m.pop()
            self.m.append(val)
            self.m.append(cur)

    def pop(self) -> None:
        val = self.s.pop()
        self.m.remove(val)

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
