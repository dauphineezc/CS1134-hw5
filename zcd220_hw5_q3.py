from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque


class MidStack:
    def __init__(self):
        self.front_data = ArrayStack()
        self.back_data = ArrayDeque()
        self.n_stack = 0
        self.n_deque = 0

    def __len__(self):
        return self.n_stack + self.n_deque

    def is_empty(self):
        return self.n_stack == 0 and self.n_deque == 0

    def push(self, e):
        if self.n_stack <= self.n_deque:
            if self.n_deque == 0:
                self.front_data.push(e)
                self.n_stack += 1
            else:
                self.n_stack += 1
                remove_from_deque = self.back_data.dequeue_first()
                self.front_data.push(remove_from_deque)
                self.back_data.enqueue_last(e)
        else:
            self.back_data.enqueue_last(e)
            self.n_deque += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if self.n_deque != 0:
            return self.back_data.last()
        else:
            return self.front_data.top()

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if self.n_deque != 0:
            val = self.back_data.dequeue_last()
            self.n_deque -= 1
        else:
            val = self.front_data.pop()
            self.n_stack -= 1
        return val

    def mid_push(self, e):
        self.n_stack += 1
        self.front_data.push(e)
