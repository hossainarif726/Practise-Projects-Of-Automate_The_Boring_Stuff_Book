#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board = {'top-left':' ', 'top-middle':' ', 'top-right':' ',
         'mid-left':' ', 'mid-middle':' ', 'mid-right':' ',
         'low-left':' ', 'low-middle':' ', 'low-right':' '}

moveslis = ['top-left','top-middle','top-right','mid-left','mid-middle','mid-right',
            'low-left','low-middle','low-right']

def displayboard(dic):
    print()
    print(dic['top-left']+'|'+dic['top-middle']+'|'+dic['top-right'])
    print('-+-+-')
    print(dic['mid-left']+'|'+dic['mid-middle']+'|'+dic['mid-right'])
    print('-+-+-')
    print(dic['low-left']+'|'+dic['low-middle']+'|'+dic['low-right'])

turn = 'X'
print("You Have To Type These In Blank Box For Each Turn. Don't Cheat Or You Will Get Caught.")
for i in moveslis:
    print(i.rjust(40))

for i in range(9):
    displayboard(board)
    print('\nTurn for '+ turn +'. Move on which place?\n')
    move = input()
    
    if move in moveslis:
        del moveslis[moveslis.index(move)]
    else:
        print('\nWhy are you cheating? This place is already taken by '+board[move]+
              ' Enter a valid position:')
        move = input('\n')
        
    board[move] = turn
        
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
    if (board['top-left'] == board['top-middle'] == board['top-right']) and board['top-left'] != ' ':
        displayboard(board)
        print(board['top-left']+' IS THE WINNER')
        break

    elif (board['top-left'] == board['mid-left'] == board['low-left']) and board['top-left'] != ' ':
        displayboard(board)
        print(board['top-left']+' IS THE WINNER')
        break

    elif board['mid-left'] == board['mid-middle'] == board['mid-right'] and board['mid-left'] != ' ':
        displayboard(board)
        print(board['mid-left']+' IS THE WINNER')
        break

    elif board['top-right'] == board['mid-right'] == board['low-right'] and board['top-right'] != ' ':
        displayboard(board)
        print(board['top-right']+' IS THE WINNER')
        break

    elif board['low-left'] == board['low-middle'] == board['low-right'] and board['low-left'] != ' ':
        displayboard(board)
        print(board['low-left']+' IS THE WINNER')
        break

    elif board['top-left'] == board['mid-middle'] == board['low-right'] and board['top-left'] != ' ':
        displayboard(board)
        print(board['top-left']+' IS THE WINNER')
        break

    elif board['top-right'] == board['mid-middle'] == board['low-left'] and board['top-right'] != ' ':
        displayboard(board)
        print(board['top-right']+' IS THE WINNER')
        break

    elif board['top-middle'] == board['mid-middle'] == board['low-middle'] and board['top-middle'] != ' ':
        displayboard(board)
        print(board['mid-middle']+' IS THE WINNER')
        break
 
    elif i == 8:
        displayboard(board)
        print('\nTHE GAME IS DRAWN')


# In[ ]:




