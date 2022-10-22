# Emmanuel A Oppong
# CS Assignment 1
# NYU Abu Dhabi
#29th September, 2022


import random, os, time


NUM_PLAYERS=2

# use random module to generate 0 and 1 at random
first_turn = random.randint(0, NUM_PLAYERS-1)


# definining players as global constants
players=("O","X")

# setting player1 according to the 0 or 1 generated randomly 
if first_turn ==1:
	player1=players[1]
	player2=players[0]
else:
	player1=players[0]
	player2=players[1]

# definining number of rows and number of columns as global constants
ROWS=6
COLS=6


# definining blocker type as global constant
BLOCKER="#"


# definining letters as global constant of a tuple
letters = ('A','B','C','D','E','F','G','H','I','J')


# creating the main board as a list
board=[]
for row in range(ROWS):
		row_list=[]
		for col in range(COLS):
			row_list.append(" ")
		board.append(row_list)




# main gameplay
def main():
	num_moves=0
	print_board()
	print("Moves are colrow eg. A5 :")
	exit_game = False
	#play game only when no exit flag has been called
	while not exit_game:
		num_moves+=1
		# random player who starts is printed
		if num_moves<2:
			print (f"{player1} will go first. ")
		player_ch= player1 if num_moves%2 >0 else player2
		putChecker(player_ch)
		update_board()

		#executes only if checkwinner function returns true and breaks the gameplay
		if checkWinner():
			if num_moves %2 >0:
				print(player1, "wins")
				print(player2, "loses")
				#lines added to replay the game if the 2 players want to
				prompt=("Do you want to play again Y or y/ N or n for yes or no...   ")
				str = input(prompt)
				s = playAgain(str)
				if s == True:
					if str== 'y' or str=="Y" :
						print(' Yes you do, Lets go once again ')
						for row in range(ROWS):
							for col in range(COLS):
								board[row][col]=' '
						main()

				

					elif str=="n" or str == "N":
						print(' No you dont, Goodbye! ')
						break

				else:print("Sorry incorrect input type. Goodbye! ")






			else:   
			    print(player2, "wins")
			    print(player1, "loses")

                #lines added to replay the game if the 2 players want to
			    prompt=("Do you want to play again Y or y/ N or n for yes or no...  ")
			    str = input(prompt)
			    s = playAgain(str)
			    if s == True:
			    	if str== 'y' or str=="Y":
			    		print(' Yes you do, Lets go once again ')
			    		for row in range(ROWS):
			    			for col in range(COLS):
			    				board[row][col]= " "

			    		main()


			    	
			    	elif str =='n' or str=='N' :
			    		print(' No you dont,Goodbye! ')
			    		break
			    else:print("Sorry incorrect input type. Goodbye! ")

					
					

			break
		
		
		
	


# a function that updates and prints the new board after a marker is placed
def update_board():
	#sleep,clear the screen and print recently updated board
	time.sleep(1.5)
	os.system("clear")
	print_board()
	

# function that prints 2D board
def print_board():
	
    #prints column header letters
	for i in letters[:COLS]:
		if(i == 'A'):
			print('    '+ i , end='  ')
		else:
			print(' '+ i , end='  ')
	#print row numbers by side of table
	print("\n  +"+"---+"*COLS)
	for row in range(ROWS):
		print(str(row)+" | ", end="")
		for col in range(COLS):
			print(board[row][col]+" | ", end="")
		print("\n  +" + "---+" * COLS)

# function that loops through the board to check if all squares are occupied and returns true if so.
def checkWinner():
	for row in range(ROWS):
		for col in range(COLS):
			if board[row][col] == " ":
				return False
	return True
		
		    
	    	


# function that uses checkInput function before placing a checker X or O on the board and blocks areas with selected BLOCKER eg. "#"
def putChecker(player_ch):
	#constantly accept input for the two players
	while True:
		prompt='Enter move for '+ player_ch + ': '
		str = input(prompt)
		# call check inputChecker function to check for correct
		# ... input type else return false and print re-enter 
		s = checkInput(str)
		if s == True:
			c = (ord(str[0]) - 65)
			r = int(str[1])
			#check that we dont go out of the board
			if r <0 or r>=ROWS or c<0 or c>=COLS:
				print("Out of range. Re-enter. ")
			elif board[r][c] != " " :
				print("Occupied square. Re-enter. ")
			else:
				board[r][c] = player_ch
				# conditions for placing defined BLOCKER in any area in the middle 
				# ...set of cells in your rectangular or 
				# ...square grid
				if r+1<ROWS and r-1>=0 and c-1>=0 and c+1<COLS and (board[r][c]== "X" or board[r][c] == "O"):
					if board[r-1][c-1] == " ":
						board[r-1][c-1] = BLOCKER
					if board[r-1][c] == " ":
						board[r-1][c] = BLOCKER
					if board[r-1][c+1] == " ":
						board[r-1][c+1] = BLOCKER
					if board[r][c-1] == " ":
						board[r][c-1] = BLOCKER
					if board[r][c+1] == " ":
						board[r][c+1] = BLOCKER
					if board[r+1][c-1] == " ":
						board[r+1][c-1] = BLOCKER
					if board[r+1][c] == " ":
						board[r+1][c] = BLOCKER
					if board[r+1][c+1] == " ":
						board[r+1][c+1] = BLOCKER 

                # conditions for placing defined BLOCKER in any cell in the first row excluding 
                # ... its first and last cells
				elif r==0 and c-1>=0  and c+1<COLS and (board[r][c]== "X" or board[r][c]== "O"):
					if board[r][c+1] == " ":
						board[r][c+1] = BLOCKER
					if board[r][c-1] == " ":
						board[r][c-1] = BLOCKER

					if board[r+1][c-1] == " ":
						board[r+1][c-1] = BLOCKER
					if board[r+1][c] == " ":
						board[r+1][c] = BLOCKER
					if board[r+1][c+1] == " ":
						board[r+1][c+1] = BLOCKER
                # conditions for placing defined BLOCKER in any cell in the last row excluding 
                # ... its first and last cells
				elif r==ROWS-1 and c-1>=0  and c+1<COLS and (board[r][c]== "X" or board[r][c]== "O"):
					if board[ROWS-1][c+1] == " ":
						board[ROWS-1][c+1] = BLOCKER
					if board[ROWS-1][c-1] == " ":
						board[ROWS-1][c-1] = BLOCKER

					if board[ROWS-2][c-1] == " ":
						board[ROWS-2][c-1] = BLOCKER
					if board[ROWS-2][c] == " ":
						board[ROWS-2][c] = BLOCKER
					if board[ROWS-2][c+1] == " ":
						board[ROWS-2][c+1] = BLOCKER

               
                # conditions for placing defined BLOCKER in any cell in the first column excluding 
                # ... its first and last cells             
				elif c==0 and r+1<ROWS and r-1>=0 and (board[r][c]== "X" or board[r][c]== "O"):
					if board[r-1][c] == " ":
						board[r-1][c] = BLOCKER
					if board[r+1][c] == " ":
						board[r+1][c] = BLOCKER

					if board[r-1][c+1] == " ":
						board[r-1][c+1] = BLOCKER
					if board[r][c+1] == " ":
						board[r][c+1] = BLOCKER
					if board[r+1][c+1] == " ":
						board[r+1][c+1] = BLOCKER
					
                # conditions for placing defined BLOCKER in any cell in the last column excluding 
                # ... its first and last cells

				elif c==COLS-1 and r+1<ROWS and r-1>=0 and (board[r][c]== "X" or board[r][c]== "O"):
					if board[r-1][COLS-1] == " ":
						board[r-1][COLS-1] = BLOCKER
					if board[r+1][COLS-1] == " ":
						board[r+1][COLS-1] = BLOCKER

					if board[r-1][COLS-2] == " ":
						board[r-1][COLS-2] = BLOCKER
					if board[r][COLS-2] == " ":
						board[r][COLS-2] = BLOCKER
					if board[r+1][COLS-2] == " ":
						board[r+1][COLS-2] = BLOCKER

					
                # conditions for placing defined BLOCKER in any of the four cells
                # ... at the corner of your rectangular or square grid

				else:

					# conditions for placing defined BLOCKER in first row left corner cell
					if r==0 and c==0 and (board[r][c]== "X" or board[r][c]== "O"):
					
						if board[r][c+1] == " ":
							board[r][c+1] = BLOCKER

						if board[r+1][c] == " ":
							board[r+1][c] = BLOCKER

						if board[r+1][c+1] == " ":
							board[r+1][c+1] = BLOCKER
						
					# conditions for placing defined BLOCKER in first row right/last corner cell	
					if r==0 and c==COLS-1 and (board[r][c]== "X" or board[r][c]== "O"): 
						if board[r][COLS-2] == " ":
							board[r][COLS-2] = BLOCKER

						if board[r+1][COLS-1] == " ":
							board[r+1][COLS-1] = BLOCKER

						if board[r+1][COLS-2] == " ":
							board[r+1][COLS-2] = BLOCKER

					# conditions for placing defined BLOCKER in last row left corner cell	
					if r==ROWS-1 and c==0 and (board[r][c]== "X" or board[r][c]== "O"):
						if board[ROWS-2][c] == " ":
							board[ROWS-2][c] = BLOCKER

						if board[ROWS-2][c+1] == " ":
							board[ROWS-2][c+1] = BLOCKER

						if board[ROWS-1][c+1] == " ":
							board[ROWS-1][c+1] = BLOCKER
						


                    # conditions for placing defined BLOCKER in last row right corner cell
					if r==ROWS-1 and c==COLS-1 and (board[r][c]== "X" or board[r][c]== "O"):
						if board[ROWS-1][COLS-2] == " ":
							board[ROWS-1][COLS-2] = BLOCKER
						if board[ROWS-2][COLS-2] == " ":
							board[ROWS-2][COLS-2] = BLOCKER

						if board[ROWS-2][COLS-1] == " ":
							board[ROWS-2][COLS-1] = BLOCKER	


            # print board and break from while loop
				print_board()
				break




			    
		# asks user to re-enter input as checkinput failed		
		else:
			print("Incorrect input type. Re-enter. ")





# checks user input as correct position on the board
# .... and in the correct format of capital letter
# .... with a number and of correct length	
def checkInput(str):
	if len(str)<2 or len(str)>2:
		return False

	elif len(str)==2 and str[0] in ('A','B','C','D','E','F','G','H','I','J') and str[1] in ('0','1','2','3','4','5','6','7','8','9'):
		return True 

		
	elif str[1] in ('A','B','C','D','E','F','G','H','I','J'):
		return False

	elif len(str) < 2  or len(str)>2:
		return False


	else:
		return False

# function that checks to see if user wants to play again
def playAgain(str):
	if len(str)<1 or len(str)>1:
		return False

	elif len(str)==1 and str[0] in ('Y','N','y','n'): 
		return True 

	elif len(str)==1 and str[0] not in ('Y','N','y','n'): 
		return False

	else: 
		return False



 #runs the main gameplay function for the game.


if __name__ == "__main__":
	main()












