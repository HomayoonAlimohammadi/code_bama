from random import randint


computer_number = randint(10,100)

for i in range(6):

    user_guess = int(input('Eneter a number from 10 to 100: '))

    if user_guess == computer_number:
        print('You won!')
        break

    # @code_bama

    elif user_guess < computer_number:
        print('You guessed too low!')

    else:
        print('You guessed too high!')

else:
    print('The number was:', computer_number)
    print('Maybe next time!')