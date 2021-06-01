import random
import enchant

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

d = enchant.Dict('en_US')

name = input('ENTER YOUR NAME:')

play_again = False

while not play_again:
    letter = random.choice(letters)
    lives = 3
    word_done = []
    winner = False
    while not winner:
        print(f'LIVES: {lives}')
        print('')
        if lives > 0:
            word_user = input(f'ENTER A WORD STARTING FROM {letter}:')
            if word_user[0] != letter:
                print('YOU USED A INVALID WORD. YOU LOST A LIFE')
                lives = lives - 1
                letter = word_user[-1]
            elif len(word_user) < 3:
                print('YOU USED A SHORT WORD OF LESS THAN 2 LETTERS. YOU LOST A LIFE')
                lives = lives - 1
                letter = word_user[-1]
            elif d.check(word_user):
                if word_user not in word_done:
                    word_done.append(word_user)
                    letter = word_user[-1]
                else:
                    print('YOU USED A DUPLICATE WORD. YOU LOST A LIFE')
                    lives = lives - 1
                    letter = word_user[-1]
            else:
                print('YOU USED A WRONG WORD. YOU LOST A LIFE')
                lives = lives - 1
                letter = word_user[-1]
        else:
            print('YOU LOST ALL YOUR LIVES.')
            winner = True
    reply = input('DO YOU WANT TO PLAY AGAIN?:').lower()
    if reply in ['yes', 'y']:
        play_again = False
    else:
        play_again = True
