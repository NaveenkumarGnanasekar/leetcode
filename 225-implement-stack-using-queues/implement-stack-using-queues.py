class MyStack:

    def __init__(self):
        self.stack =  collections.deque()

    def push(self, x):
        self.stack.append(x)

        # Move previous elements behind x
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self):
        return self.stack.popleft()

    def top(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0