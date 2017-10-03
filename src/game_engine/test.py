from game_engine import game_engine


def move(board, i, player):
	if board[i] == 0:
		board[i] = player
	return board

def rep(v):
	if v == 0:
		return " "
	elif v == 1:
		return "X"
	else:
		return "0"


def draw_line(one, two, three):
	print(" " + rep(one) + " | " + rep(two) + " | " + rep(three))

def draw_board(board):
	print ("")
	draw_line(board[0],board[1],board[2])
	print("--- --- ---")
	draw_line(board[3],board[4],board[5])
	print("--- --- ---")
	draw_line(board[6],board[7],board[8])
	print ("")





hard = game_engine("hard")


maxdepth = 9
depth = 0

currentplayer = 1
state = [0,0,0,0,0,0,0,0,0]
while len(hard.available_moves(state)) != 0:
	
	mm = hard.makemove(state, currentplayer)
	print("player " + str(currentplayer) + " got: " + str(mm))
	state = move(state, mm, currentplayer)
	draw_board(state)
	
	
	if hard.winning(state, currentplayer):
		print("Player " + str(currentplayer) + " won!")
		break
	currentplayer = currentplayer * -1
	print("")

	if depth == maxdepth:
		break

	depth = depth +1

