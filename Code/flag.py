number = int(input('Enter a number: '))

isPrime = True

for i in range(2, int(number**0.5)+1):
    if number % i == 0:
        isPrime = False
        print('the number is not prime')
        break

else:
    print('the number is prime')
