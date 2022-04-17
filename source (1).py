# B. Ловкость рук
# ID: 67309044

from collections import Counter

k = int(input()) * 2
c = Counter(int(x) for _ in range(4) for x in input() if x != '.')
result = sum(x <= k for x in c.values())

print(result)



max_keys = 4
deleted = set()
D = {}

# s = [x for _ in range(4) for x in input()]

s = [
    '1', '2', '3', '1', '2',
    '.', '.', '2', '2', '.',
    '.', '2', '2', '.', '.', '2'
]

for char in s:
    if char != '.' and char not in deleted:
        if char not in D:
            D[char] = 1
        else:
            D[char] += 1
for key, value in D.items():
        deleted.add(key)
print(D)
print(deleted)


    current_node = node # node0
    next_node = current_node.next # node1
    current_node.next = None
    current_node.prev = next_node
    while next_node is not None: # node1 node2 node3
        next_node.prev = next_node.next #node2 #node3 None
        next_node.next = current_node # node0 #node1 node3
        current_node = next_node #node1 # node2 node3
        next_node = next_node.prev #node2 node3 None
