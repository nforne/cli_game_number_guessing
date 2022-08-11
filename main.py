from art import logo
import random
from replit import clear

print(logo)
print('Welcome to the number guessing Game!')


def play():
    number, times, chances = random.randint(1, 100), 0, 0
    while True:
        difficulty = input('Enter the difficulty level: Easy "E" or Hard "H" ').upper()
        if difficulty == 'E':
            chances += 10
            break
        elif difficulty == 'H':
            chances += 5
            break
        else:
            print("Wrong entry. E/H, please!")
    user_input = int(input('I have a number in mind between 1 and 100. What do you think it is? \nTake a guess:  '))
    while chances != 0:
        times += 1
        chances -= 1
        if user_input == number:
            print(f'You Win! After {times} tries!')
            break
        if user_input < number:
            print('Your guess is lower than what i have in mind.')
        elif user_input > number:
            print('Your guess is higher than what i have in mind.')
        if chances == 0:
            print(f'You lose! After {times} tries!')
            print(f'the answer is {number}')
            break
        print('=>|-----------------------------------------------------------------|')
        user_input = int(input(f'You have {chances} chances left. \nGuess again:  '))
    print('=>|-----------------------------------------------------------------|')
    to_continue = input('Would you like to play it again? Y/N  ').upper()
    if to_continue == 'Y':
        clear()
        play()
    else:
        for _ in [times, chances, number, user_input]:
            del _
        return


play()
