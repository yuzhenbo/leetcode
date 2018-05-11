class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.lst) == 0:
            self.min_v = x

        self.lst.append(x - self.min_v)
        if x < self.min_v:
            self.min_v = x

    def pop(self):
        """
        :rtype: void
        """
        v = self.lst.pop()

        # the min_value gets popped, find the previous min
        if v < 0:
            item_to_pop = self.min_v
            prev_min_v = item_to_pop - v
            self.min_v = prev_min_v
            return item_to_pop
        else:
            return v + self.min_v

    def top(self):
        """
        :rtype: int
        """

        # similar logic to pop
        v = self.lst[-1]

        if v < 0:
            item_to_pop = self.min_v
            return item_to_pop
        else:
            return v + self.min_v

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_v

if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(4)
    min_stack.push(5)
    min_stack.push(7)
    min_stack.push(6)
    min_stack.push(-3)
    min_stack.push(-6)
    min_stack.push(18)
    min_stack.pop()
    min_stack.pop()
    print(min_stack.getMin())