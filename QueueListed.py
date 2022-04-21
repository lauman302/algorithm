'''
Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка.
Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его.
Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число,
не превосходящее 1000.
В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.
Пример 1

Ввод                    Вывод
10                      -34
put -34                 1
put -23                 -23
get                     0
size                    error
get                     error
size                    1
get
get
put 80
size

Пример 2

Ввод                    Вывод
6                       2
put -66                 2
put 98                  -66
size                    98
size
get
get
'''

class QueueListed:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next
        
        def __str__(self):
            return self.value

    def __init__(self):
        self.queue = []
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def isEmpty(self):
        return self.queue == 0
    
    def get(self):
        if self.isEmpty():
            return 'error'
        value = self.queue.pop(self.head)
        self.head += 1
        return value
        

    def put(self, item):
        if self.isEmpty():
            self.queue[self.tail] = self.Node(item)
            self.tail += 1
            self.size += 1
        else:
            prev_node = self.queue[self.tail - 1]
            new_node = self.Node(item)
            prev_node.next = new_node
            self.queue[self.tail] = new_node


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
