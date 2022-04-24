class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()


def calculate(line):
    for symbol in line:
        if symbol == '+':
            first, two = stack.items[-2:]
            result = first + two
            stack.items[-2] = result
            stack.pop()
        elif symbol == '-':
            first, two = stack.items[-2:]
            result = first - two
            stack.items[-2] = result
            stack.pop()
        elif symbol == '*':
            first, two = stack.items[-2:]
            result = first * two
            stack.items[-2] = result
            stack.pop()
        elif symbol == '/':
            first, two = stack.items[-2:]
            result = first // two
            stack.items[-2] = result
            stack.pop()
        else:
            stack.push(int(symbol))
    return stack.items[-1]


if __name__ == '__main__':
    stack = Stack()
    line = input().split()
    print(calculate(line))