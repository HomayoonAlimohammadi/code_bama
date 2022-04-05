list_1 = ['hello', 'world!']
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

concat = []

for i in range(min(len(list_1), len(list_2))):
    concat.append((list_1[i], list_2[i]))
# ----------------------------------------------
'''
@code_bama:
    concat --> [('hello', 'salam'), ('world!', 'donya!')]
'''


result = list(zip(list_1, list_2))
# ----------------------------------------------
'''
@code_bama:
    result --> [('hello', 'salam'), ('world!', 'donya!')]
'''