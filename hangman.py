import random

def hangman(word):
    wrong = 0
    stages = ['',
              '________        ',
              '|               ',
              '|       |       ',
              '|       0       ',
              '|      /|>      ',
              '|      / >      ',
              '|               '
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ようそろ！ハングマンへ！')

    while wrong < len(stages):
        print('\n')
        msg = '一文字を予想してね > '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち！')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages))
        print('あなたの負け！正解は {}.'.format(word))

with open('EDM Artists.txt', 'r', encoding='utf_8') as f:
    artists = f.readlines()

for i, artist in enumerate(artists):
   artists[i] = artist.lower().replace(' ', '').replace('\n', '')


hangman(random.choice(artists))
        
