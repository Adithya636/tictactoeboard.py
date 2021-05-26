#This is a tic-tac-toe's board using python
# Rementioning only board and 9 moves

'''
1 | 2 | 3
__________

4 | 5 | 6
__________

7 | 8 | 9

'''
#key, ,values for a board
theBoard = {'1' : ' ','2' : ' ', '3' : ' ', '4' : ' ', '5' : ' ', '6' : ' ', '7' : ' ', '8' : ' ', '9' : ' ',}

def board(boards):
	print(boards['1'] + ' | ' +  boards['2'] + ' | ' + boards['3'])
	print('---------')
	print(boards['4'] + ' | ' +  boards['5'] + ' | ' + boards['6'])
	print('---------')
	print(boards['7'] + ' | ' +  boards['8'] + ' | ' + boards['9'])
#board(theBoard)
#-----------------------until this is board--------------------------
#-------------moves--------------------------------------------------
Turn = 'x'
for i in range(10):
	board(theBoard)
	print('turn for ' + Turn + ' move')
	move = input('enter the place as number: ')
	theBoard[move] = Turn
	if Turn == 'x':
		Turn = 'o'
	elif Turn == 'o':
		Turn = 'x'

board(theBoard)
input('your game ended: ')