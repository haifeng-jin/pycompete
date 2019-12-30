# Data Structures
## Queue & Stack
```python
import collections
dq = collections.deque()
dq.append(1)
dq.append(2)
dq.append_left(3)
print(dq)  # [3, 1, 2]
dq.pop()
print(dq)  # [3, 1]
dq.pop_left()
print(dq)  # [1]
```
## Hash Table
```python
a = {}
a['ab'] = 5
print('ab' in a)  # True
print(a['ab'])  # 5

a = set()
a.add('ab')
print('ab' in a) # True
```
## Heap
# Strings
## split strings
```python
a = 'aba'
print(a.split('a'))   # ['', 'b', '']
```
## count occurance
```python
a = 'abababa'
print(a.count('aba'))  # 2
```
