class MinStack(object):

    def __init__(self):

        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):

        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] != "":
                self.stack.pop(i)
                return

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()