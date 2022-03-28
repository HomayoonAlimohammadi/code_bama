### Print the following pattern

n = int(input('Please enter the maximum number of stars: '))

### Basic Version:

for i in range(1, n+1):
    print(i*'*')

for i in range(n-1, 0, -1):
    print(i*'*')


### Advanced Version:

for i in list(range(1, n+1)) + list(range(n-1, 0,-1)):
    print(i*'*')

