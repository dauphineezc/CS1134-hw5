from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.n = 0
        self.max_val = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def push(self, e):
        if self.is_empty():
            self.data.push((e, e))
            self.max_val = e
        else:
            curr_max = max(e, self.data.top()[1])
            self.data.push((e, curr_max))
            self.max_val = curr_max
        self.n += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        val = self.data.pop()[0]
        self.n -= 1
        return val

    def max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.top()[1]
