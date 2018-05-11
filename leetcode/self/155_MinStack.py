class MinStack:
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        self.q.pop()

    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1]

    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return min(self.q)