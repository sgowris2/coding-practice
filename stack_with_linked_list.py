from collections import deque


class Stack:

    def __init__(self):
        self.lst = deque()

    def push(self, obj):
        self.lst.appendleft(obj)

    def pop(self):
        obj = self.lst.popleft()
        return obj

    def print_all(self):
        print(self.lst.__str__())

    def clear(self):
        self.lst.clear()


if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push('a')
    print(stack.pop())
    stack.clear()
    stack.print_all()
