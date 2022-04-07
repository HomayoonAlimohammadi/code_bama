list_1 = ['hello', 'world!']
list_2 = ['salam', 'donya!']

concat = []

for i in range(len(list_1)):
    concat.append((list_1[i], list_2[i]))
# ----------------------------------------------
'''
@code_bama:
    concat --> [('hello', 'salam'), ('world!', 'donya!')]
'''

list_1 = ['hello', 'world!', 'code_bama']
list_2 = ['salam', 'donya!']

concat = []

for i in range(min(len(list_1), len(list_2))):
    concat.append((list_1[i], list_2[i]))
# ----------------------------------------------
'''
@code_bama:
    concat --> [('hello', 'salam'), ('world!', 'donya!')]
'''

list_1 = ['hello', 'world!', 'code_bama']
list_2 = ['salam', 'donya!']

result = list(zip(list_1, list_2))
# ----------------------------------------------
'''
@code_bama:
    result --> [('hello', 'salam'), ('world!', 'donya!')]
'''

from random import sample
from time import time
from sys import getsizeof

l1 = sample(range(10_000_000), 1_000_000)
l2 = sample(range(10_000_000), 1_000_000)

t0 = time()
for i in range(min(len(l1), len(l2))):
    concat.append((l1[i], l2[i]))

print(time() - t0) # >>> ~ 0.22
print(getsizeof(concat) / 10**6) # >>> ~ 8.69 MB


t0 = time()
concat = list(zip(l1, l2))

print(time() - t0) # >>> ~ 0.09
print(getsizeof(concat) / 10**6) # >>> ~ 8.25 MB



