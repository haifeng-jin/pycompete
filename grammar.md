# Data Structures
## Queue & Stack
```python
import collections
dq = collections.deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq)  # [3, 1, 2]
dq.pop()
print(dq)  # [3, 1]
dq.popleft()
print(dq)  # [1]
```
## Hash Table
```python
a = {}
a['ab'] = 5
print('ab' in a)  # True
print(a['ab'])  # 5
a.pop('ab')
print('ab' in a)  # False

a = set()
a.add('ab')
print('ab' in a)  # True
```
## Heap
# Strings
## Split Strings
```python
a = 'aba'
print(a.split('a'))  # ['', 'b', '']
print(a.split('x'))  # ['aba']
```
## Count Occurance
```python
a = 'abababa'
print(a.count('aba'))  # 2
```
## Case Changes
```python
a = 'aBA'
print(a.upper())  # ABA
print(a.lower())  # aba 
```
