class MyQueue(object):

    def __init__(self):
        self.instack =[]
        self.outstack=[]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.instack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.outstack ==[]:
            while self.instack:

                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]
    def empty(self):

        """
        :rtype: bool
        """
        return self.outstack ==[] and self.instack ==[]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()