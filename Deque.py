# A. Дек
# ID: https://contest.yandex.ru/contest/23759/run-report/67801414/


class MaxItemsException(Exception):
    ''' Достигнуто максимальное количество элементов в деке.'''
    pass


class NoItemsException(Exception):
    ''' В деке нет элементов.'''
    pass


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
            raise MaxItemsException
        else:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise MaxItemsException
        else:
            self.head = (self.head - 1) % self.max_size
            self.deque[self.head] = value
            self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise NoItemsException
        else:
            self.tail = (self.tail - 1) % self.max_size
            value = self.deque[self.tail]
            self.deque[self.tail] = None
            self.size -= 1
            return value

    def pop_front(self):
        if self.is_empty():
            raise NoItemsException
        else:
            value = self.deque[self.head]
            self.deque[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value


if __name__ == '__main__':
    result = []
    count_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for i in range(count_commands):
        try:
            command = input().split()
            if len(command) > 1:
                getattr(deque, command[0])(command[1])
            else:
                print(getattr(deque, command[0])())
        except NoItemsException:
            print('error')
        except MaxItemsException:
            print('error')
