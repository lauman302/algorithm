class StackMax:
    def __init__(self):
        self.items = []
        self.max = []
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items)-1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items)-1])
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return 'error'
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if self.isEmpty():
            return 'None'
        return self.max[len(self.items) - 1]    

stack = StackMax()
cnt_commands = int(input())
result = []
for i in range(cnt_commands):
    command = input().split()
    if command[0] == 'push':
        stack.push(command[1])
    if command[0] == 'pop':
        if stack.pop() == 'error':
            result.append('error')
    if command[0] == 'get_max':
        result.append(stack.get_max)
print(*result, sep='\n')