'''
Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума
среди элементов в стеке. 
Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None.
При этом push(x) и pop() также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000.
Далее идут команды по одной в строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».

Пример 1:

Ввод                        Вывод:
10                          error
pop                         error
pop                         4
push 4                      None
push -5
push 7
pop
pop
get_max
pop
get_max
'''


class StackMaxEffective:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.items:
            new_max = max(item, self.items[-1][1])
        else:
            new_max = item
        self.items.append((item, new_max))

    def pop(self):
        if self.isEmpty():
            return 'error'
        return self.items.pop()

    def get_max(self):
        if self.isEmpty():
            return 'None'
        return self.items[-1][1]


if __name__ == '__main__':
    stack = StackMaxEffective()
    cnt_commands = int(input())
    result = []
    for i in range(cnt_commands):
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        if command[0] == 'get_max':
            result.append(stack.get_max())
    print(*result, sep='\n')
