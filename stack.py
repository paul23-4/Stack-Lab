class Stack:
    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit

    def push(self, item):
        if self.limit is None or len(self.stack) < self.limit:
            self.stack.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def is_full(self):
        return self.limit is not None and len(self.stack) == self.limit

    def search(self, item):
        if item in self.stack:
            return self.size() - self.stack.index(item) - 1
        return -1