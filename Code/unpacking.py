my_list = [1,2]

a, b = my_list

# >>> a = 1
# >>> b = 2


my_list = [1,2,3]

# a, b = my_list

# >>> ValueError: too many values to unpack (expected 2)

a, *b = [1, 2, 3]

# >>> a = 1
# >>> b = [2, 3]


# a, *b, c = [1,2,3,4]

# >>> a = 1
# >>> b = [2, 3]
# >>> c = 4




full_name = {'fist_name':'code', 'last_name':'bama'}
pages = {'github': 'https://github.com/HomayoonAlimohammadi/code_bama',
         'instagram': 'http://instagram.com/code_bama'}

code_bama_data = {**full_name, **pages}

# print(code_bama_data)

# ------------------------------------------------------------------------

# >>> {'fist_name': 'code', 'last_name': 'bama',
#     'github': 'https://github.com/HomayoonAlimohammadi/code_bama',
#     'instagram': 'http://instagram.com/code_bama'}



def code_bama(*args, **kwargs):

    for arg in args:
        print(arg, end=' ')
    
    print()
    
    for key, value in kwargs.items():
        print(key,'-->', value)


code_bama('welcome', 'to', '@code_bama!',
         github = 'https://github.com/HomayoonAlimohammadi/code_bama',
         instagram = 'http://instagram.com/code_bama')

# ----------------------------------------------------------------------

# >>> welcome to @code_bama! 
#     github --> https://github.com/HomayoonAlimohammadi/code_bama
#     instagram --> http://instagram.com/code_bama



