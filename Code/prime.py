### Print all prime numbers
### in a given range

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


start = int(input('Please enter the starting point: '))
end = int(input('Please enter the ending point: '))

for i in range(start, end+1):
    if isPrime(i):
        print(i)
