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
