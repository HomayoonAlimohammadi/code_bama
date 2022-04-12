def isPrime(n):
    '''
    Check too see if a number is Prine
    '''
    try:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    except (ValueError, TypeError) as e:
        print(e)
        return False

    finally:
        print('isPrime function was called')
    

number = int(input('Enter a number: '))



try:
    number = int(input('Enter a number: '))

except:
    print('You did not enter a number.')



try:
    number = int(input('Enter a number: '))
    result = 10 / number

except (ValueError, ZeroDivisionError) as e:
    print(e)



number = input('Enter a number: ')

if number.isdigit() and number != 0:
    number = int(number)
    result = 10 / number

else:
    print('Invalid input.')

