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



easy = game_engine("easy")
hard = game_engine("hard")


# maxdepth = 9
# depth = 0

# currentplayer = 1
# state = [0,0,0,0,0,0,0,0,0]
# while len(hard.available_moves(state)) != 0:
	
# 	mm = hard.makemove(state, currentplayer)
# 	# print("player " + str(currentplayer) + " got: " + str(mm))
# 	state = move(state, mm, currentplayer)
# 	draw_board(state)
	
	
# 	if hard.winning(state, currentplayer):
# 		print("Player " + str(currentplayer) + " won!")
# 		break
# 	currentplayer = currentplayer * -1
# 	print("")

# 	if depth == maxdepth:
# 		break

# 	depth = depth +1



assert hard.game_over([1,1,1,1,1,1,1,1,1])==True
assert hard.game_over([0,0,0,0,0,0,0,0,0])==False
assert hard.game_over([1,1,1,0,0,0,0,0,0])==True


assert hard.winning([1,1,1,0,0,0,0,0,0], 1)==True
assert hard.winning([1,1,1,0,0,0,0,0,0], -11)==False

assert hard.available_moves([0,1,1,1,1,1,1,1,1])==[0]
assert hard.available_moves([1,0,1,1,1,1,1,1,1])==[1]
assert hard.available_moves([1,0,0,1,1,1,1,1,1])==[1,2]
assert hard.available_moves([1,1,1,1,1,1,1,1,1])==[]

assert hard.randommove([0,1,1,1,1,1,1,1,1], 1)==0
assert hard.randommove([0,0,0,1,1,1,1,1,1], 1) in range(3)
assert hard.randommove([0,0,0,0,0,0,0,0,0], 1) in range(9)

assert hard.hardmove([1,1,0,0,0,0,0,0,0], -1)==2
assert hard.hardmove([1,-1,-1,0,1,0,0,0,0], -1)==8
assert hard.hardmove([0,0,0,1,1,0,-1,-1,0], -1)==8
assert hard.hardmove([-1,-1,0,0,0,0,0,0,0], 1)==2



assert hard.hardmove([1,1,0,0,0,0,0,0,0], -1)==hard.makemove([1,1,0,0,0,0,0,0,0], -1)

assert easy.makemove([0,0,0,0,0,0,0,0,0], 1) in range(9)
assert easy.makemove([0,0,0,0,0,0,0,1,1], 1) in range(7)

print("All tests passed")

