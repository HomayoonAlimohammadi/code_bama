### Print the Following pattern.

n = int(input('Please enter the maximum number: '))

### Basic Version:

for i in range(n+1):
    line = ''
    for j in range(1, i + 1):
        line += str(j) + " "

    print(line)

### Advanced Version:

for i in range(n+1):
    line = ' '.join([str(i) for i in range(1, i+1)])
    print(line)
