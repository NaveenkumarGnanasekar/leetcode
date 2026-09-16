class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack =[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.minstack or value < self.minstack[-1]:
            self.minstack.append(value)
        else :
            self.minstack.append(self.minstack[-1])
        self.stack.append(value)


    def pop(self):
        """
        :rtype: None
        """
        self.minstack.pop()
        return self.stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()