### Calculate the factorial 
### of a given number n: n!

from math import factorial

### Basic Version:

n = int(input('Please enter the number: '))

fac = 1
for i in range(1, n+1):
    fac *= i

print(fac)

### Advanced Version:
print(factorial(n))
