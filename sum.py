### Print the sum of all numbers
### from 1 to the given number.

n = int(input('Please enter the number: '))

Sum = 0
for i in range(1, n+1):
    Sum += i
print(Sum)

### Advanced:

print(sum(range(n+1)))
