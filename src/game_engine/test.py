from game_engine import game_engine


def move(board, i, player):
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
	print(" " + rep(one) + " | " + rep(two) + "  | " + rep(three))

def draw_board(board):
	print ("")
	draw_line(board[0],board[1],board[2])
	print("--- --- ---")
	draw_line(board[3],board[4],board[5])
	print("--- --- ---")
	draw_line(board[6],board[7],board[8])
	print ("")





easy = game_engine("easy")
normal = game_engine("normal")
hard = game_engine("hard")

# print("Easy:")
# print(easy.available_moves(state))
# print("easy makes move: " + str(easy.makemove(state, 1)))


# print(normal.available_moves(state))
# print(hard.available_moves(state))

currentplayer = 1
state = [0,0,0,0,0,0,0,0,0]
while len(easy.available_moves(state)) != 0:
	state = move(state, easy.makemove(state, currentplayer), currentplayer)
	currentplayer = currentplayer * -1
	draw_board(state)
	if easy.winning(state, currentplayer):
		print("Player " + str(currentplayer) + " won!")
		break




currentplayer = 1
state = [0,0,0,0,0,0,0,0,0]
while len(normal.available_moves(state)) != 0:
	state = move(state, normal.makemove(state, currentplayer), currentplayer)
	currentplayer = currentplayer * -1
	draw_board(state)
	if normal.winning(state, currentplayer):
		print("Player " + str(currentplayer) + " won!")
		break

currentplayer = 1
state = [0,0,0,0,0,0,0,0,0]
while len(hard.available_moves(state)) != 0:
	state = move(state, hard.makemove(state, currentplayer), currentplayer)
	currentplayer = currentplayer * -1
	draw_board(state)
	if hard.winning(state, currentplayer):
		print("Player " + str(currentplayer) + " won!")
		break