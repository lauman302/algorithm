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
