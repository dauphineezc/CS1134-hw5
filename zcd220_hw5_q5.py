from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()

    queue.enqueue([])

    for i in range(len(lst)-1):
        n = len(queue)
        for j in range(n):
            p = queue.dequeue()
            for k in range(len(p) + 1):
                stack.push(p[:k] + [lst[i]] + p[k:])

        while not stack.is_empty():
            queue.enqueue(stack.pop())

    n = len(queue)
    for i in range(n):
        p = queue.dequeue()
        for j in range(len(p) + 1):
            queue.enqueue(p[:j] + [lst[-1]] + p[j:])

    for i in range(len(lst)):
        lst.pop()

    while not queue.is_empty():
        lst.append(queue.dequeue())
    return lst
