'''
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно.
Но, если в деке было много элементов, программа работала очень долго.
Дело в том, что не все операции выполнялись за O(1).

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000.
Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000.
В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека.
Если в деке уже находится максимальное число элементов, вывести «error».

push_front(value) – добавить элемент в начало дека.
Если в деке уже находится максимальное число элементов, вывести «error».

pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
'''

class Deque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push_back(self, value):
        if self.is_full():
            print('error')
        else:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def push_front(self, value):
        if self.is_full():
            print('error')
        else:
            self.head = (self.head - 1) % self.max_size
            self.deque[self.head] = value
            self.size += 1

    def pop_back(self):
        if self.is_empty():
            print('error')
        else:
            self.tail = (self.tail - 1) % self.max_size
            value = self.deque[self.tail]
            self.deque[self.tail] = None
            self.size -= 1
            print(value)

    def pop_front(self):
        if self.is_empty():
            print('error')
        else:
            value = self.deque[self.head]
            self.deque[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            print(value)


if __name__ == '__main__':
    result = []
    count_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for i in range(count_commands):
        command = input().split()
        if len(command) > 1:
            getattr(deque, command[0])(command[1])
        else:
            getattr(deque, command[0])()
