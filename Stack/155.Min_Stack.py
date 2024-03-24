class MinStack:

    def __init__(self):
        self.minarr = []
        self.arr = []

    def push(self, val: int) -> None:
        if len(self.arr) == 0 or val < self.minarr[-1]:
            self.minarr.append(val)
        else:
            self.minarr.append(self.minarr[-1])
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.pop())
print(obj.top())
print(obj.getMin())