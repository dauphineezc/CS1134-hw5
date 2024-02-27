from ArrayStack import ArrayStack


class Queue:
    def __init__(self):
        self.reserve_stack = ArrayStack()
        self.active_stack = ArrayStack()
        self.n_reserve = 0
        self.n_active = 0

    def __len__(self):
        return self.n_reserve + self.n_active

    def is_empty(self):
        return self.n_reserve == 0 and self.n_active == 0

    def first(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        for i in range(self.n_active):
            self.reserve_stack.push(self.active_stack.pop())
            self.n_reserve += 1
            self.n_active -= 1
        front_elem = self.reserve_stack.top()
        for i in range(self.n_reserve):
            self.active_stack.push(self.reserve_stack.pop())
            self.n_reserve -= 1
            self.n_active += 1
        return front_elem

    def enqueue(self, e):
        self.active_stack.push(e)
        self.n_active += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        for i in range(self.n_active - 1):
            self.reserve_stack.push(self.active_stack.pop())
            self.n_reserve += 1
            self.n_active -= 1
        front_elem = self.active_stack.pop()
        self.n_active -= 1
        for i in range(self.n_reserve):
            self.active_stack.push(self.reserve_stack.pop())
            self.n_reserve -= 1
            self.n_active += 1
        return front_elem
