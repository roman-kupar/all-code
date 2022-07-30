import random
import sys   
list = ['rock','paper','scissors']
while(True):
    a = str(input())
    number = random.choice(list)
    print(number)   
    if a == 'rock':
        if number == a:
            print('Draw')
        elif number == 'scissors':
            print('You win')
        elif number == 'paper':
            print('You lost')    
    elif a == 'paper':
        if number == a:
            print('Draw')
        elif number == 'scissors':
            print('You lost')
        elif number == 'rock':
            print('You win')
    elif a == 'scissors':
        if number == a:
            print('Draw')
        elif number == 'paper':
            print('You win')
        elif number == 'rock':
            print('You lost') 