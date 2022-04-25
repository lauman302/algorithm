# B. Калькулятор
# ID: https://contest.yandex.ru/contest/23759/run-report/67801884/


OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '*': lambda x, y: x * y,
    '/': lambda x, y: y // x
}


class NoItemsException(Exception):
    ''' Стек не содержит элементы.'''
    pass


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise NoItemsException
        return self.items.pop()


def calculate(line):
    for value in line:
        operation = OPERATIONS.get(value)
        stack.push(
            operation(stack.pop(), stack.pop())
            if operation else int(value)
        )
    return stack.pop()


if __name__ == '__main__':
    stack = Stack()
    line = input().split()
    print(calculate(line))
