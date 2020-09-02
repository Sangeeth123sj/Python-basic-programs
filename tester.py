#Game Board
board = [ "_","_","_",
		  "_","_","_",
		  "_","_","_"]

game_still_on = True

position = None

winner = None

#whose turn

current_player = "X"


def display_board():
	print(board[0]+"|"+board[1]+"|"+board[2])
	print(board[3]+"|"+board[4]+"|"+board[5])
	print(board[6]+"|"+board[7]+"|"+board[8])




def play_game():
	display_board()#display board
	
	while game_still_on:
		handle_turn(current_player)
		
		check_if_game_over()

		flip_player()
		


	# Game end
	if winner == "X" or winner == "O":
		print(winner+" won!")
		play_again()

	elif winner == None:
		print("It's a  Tie!")
		play_again()


def play_again():
	global game_still_on
	global winner

	k = raw_input("Play again?(y/n)")
	
	if k=="y":
		for x in range(9):
			board[x] = "_"
			
			print x
		game_still_on = True
		winner = None
		play_game()
	
	elif k == "n":
		print("Thank you")
	elif k != "y" and k != "n":
		print ("wrong input")
		play_again()




def flip_player():
	
	global current_player
	
	if current_player == "X":
    		current_player="O"

	elif current_player == "O":
    		current_player="X"


	




 
def handle_turn(player):
	global position
	position = input("Enter the position from 1 to 9: ")
	position = int(position)-1

	playeropposite = None
	if player == "X":
		playeropposite = "O"
	else:
		playeropposite = "X"



	if check_for_repeat(player) != True:
		board[position]= player
	else:
		print("chosen position is already occupied by " + playeropposite)


	display_board()
	

def check_for_repeat(player):

	if board[position] != player and board[position] != "_":
		return True





def check_if_game_over():

	check_row()
	check_column()
	check_diagonal()
	check_filled()

def check_row():
	global winner	
	global game_still_on

	row_1 = board[0] == board[1] == board[2] != "_"
	row_2 = board[3] == board[4] == board[5] != "_"
	row_3 = board[6] == board[7] == board[8] != "_"

	if row_1:
		winner=  board[0]
		game_still_on = False
	elif row_2:
		winner= board[3]
		game_still_on = False
	elif row_3:
		winner= board[6]
		game_still_on = False



def check_column():
	global winner	
	global game_still_on

	column_1 = board[0] == board[3] == board[6] != "_"
	column_2 = board[1] == board[4] == board[7] != "_"
	column_3 = board[2] == board[5] == board[8] != "_"

	if column_1:
		winner=  board[0]
		game_still_on = False
	elif column_2:
		winner= board[1]
		game_still_on = False
	elif column_3:
		winner= board[2]
		game_still_on = False


def check_diagonal():
	global winner	
	global game_still_on

	diagonal_1 = board[0] == board[4] == board[8] != "_"
	diagonal_2 = board[2] == board[4] == board[6] != "_"
	

	if diagonal_1:
		winner=  board[0]
		game_still_on = False
	elif diagonal_2:
		winner= board[2]
		game_still_on = False
	


def check_filled():
	global winner	
	global game_still_on
	i=int(0)
	for x in board:
		if x != "_":
			i= i+1
	
	if i == 9:
		game_still_on = False
		winner= None






play_game()


#board
#display board
#play game
#handle turn
#check win
	#check rows
	#check columns
	#check diagonals
#check tie
#flip player
