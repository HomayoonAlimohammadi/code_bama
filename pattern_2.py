### Print the following pattern.

n = int(input('Please enter the biggest number: '))

### Basic version:

for i in range(n):
    line = ''
    for j in range(n-i, 0, -1):
        line += str(j) + ' '
    print(line)

### Advanced version:

for i in range(n):
    line = ' '.join([str(j) for j in range(5-i, 0, -1)])
    print(line)
