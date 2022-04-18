'''
Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size, 
означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди. 
Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». 
При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.

Пример 1

Ввод                Вывод
8                   None                  
2                   5                   
peek                2
push 5              2
push 2              error
peek                2
size
size
push 1
size


Пример 2

Ввод                Вывод
10                  1
1                   error
push 1              1
size                error
push 3              1
size                1
push 1              error
pop
push 1
pop
push 3
push 3
'''

class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, elem):
        if self.size != self.max_size:
            self.queue[self.tail] = elem
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return 'None'
        elem = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return elem

    def peek(self):
        if self.is_empty():
            return 'None'
        elem = self.queue[self.head]
        return elem

    def size(self):
        return self.size

if __name__ == '__main__':
    result = []
    cnt_commands = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for i in range(cnt_commands):
        command = input().split()
        if command[0] == 'push':
            if queue.push(command[1]) == 'error':
                result.append('error')
        elif command[0] == 'pop':
            result.append(queue.pop())
        elif command[0] == 'peek':
            result.append(queue.peek())
        elif command[0] == 'size':
            result.append(queue.size)
    print(*result, sep='\n')
