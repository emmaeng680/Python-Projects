# Emmanuel A Oppong
# CS Assignment 2
# NYU Abu Dhabi
# 13th October, 2022

import random, os, time

ROWS=6
COLS=7

# definining letters as global constant of a tuple
letters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')


# creating the main board as a list
board=[]
for row in range(ROWS):
		row_list=[]
		for col in range(COLS):
			row_list.append(" ")
		board.append(row_list)


# definining players as global constants
players=("X","O","V","H","M")




# main gameplay
def main():
	num_moves=0
	print_board()
	start=0
	if start ==0:

		selection = True

		#get number of players before game starts
		#make a selection of number of players while selection is true and start counter still equal to 0
		while selection and start ==0:
			prompt = "Enter a number of players: 2-5 players allowed... "
			NUM_PLAYERS = input(prompt)
			s=checkNumPlayers(NUM_PLAYERS)
			if s == True:

				#increase start to help break from requiring the number of players loop
				start+=1

				# the number of players about to play the game is printed
				print(NUM_PLAYERS,"players will be playing this game")

				#break from selection loop by setting it to False
				selection = False
			else:
				print("Incorrect input type. Re-enter. ")
		num_players =int(NUM_PLAYERS)

		#define the first turn for any number of players 
		first_turn = random.randint(0, num_players-1)

	   #SETTING (first_turn) for 2 players
		if num_players ==2:
			
			if first_turn ==0:
				player1=players[0]
				player2=players[1]
			else:
				player1=players[1]
				player2=players[0]


		#SETTING (first_turn) for 3 players
		elif num_players ==3:
			if first_turn ==0:
				player1=players[0]
				player2=players[1]
				player3=players[2]
			elif first_turn ==1:
				player1=players[1]
				player2=players[0]
				player3=players[2]
			else:
				player1=players[2]
				player2=players[0]
				player3=players[1]


		#SETTING (first_turn) for 4 players
		elif num_players ==4:
			if first_turn ==0:
				player1=players[0]
				player2=players[1]
				player3=players[2]
				player4=players[3]
			elif first_turn ==1:
				player1=players[1]
				player2=players[0]
				player3=players[2]
				player4=players[3]
			elif first_turn==2:
				player1=players[2]
				player2=players[0]
				player3=players[1]
				player4=players[3]
			else:
				player1=players[3]
				player2=players[0]
				player3=players[1]
				player4=players[2]


		#SETTING (first_turn) for 5 players
		else:
			if first_turn ==0:
				player1=players[0]
				player2=players[1]
				player3=players[2]
				player4=players[3]
				player5=players[4]
			elif first_turn ==1:
				player1=players[1]
				player2=players[0]
				player3=players[2]
				player4=players[3]
				player5=players[4]
			elif first_turn==2:
				player1=players[2]
				player2=players[0]
				player3=players[1]
				player4=players[3]
				player5=players[4]
			elif first_turn==3:
				player1=players[3]
				player2=players[0]
				player3=players[1]
				player4=players[2]
				player5=players[4]
			else:
				player1=players[4]
				player2=players[0]
				player3=players[1]
				player4=players[2]
				player5=players[3]


	#defining game instructions	
	print("Moves are the columns eg. A or B :")
	# Game loop runs while this variable is still True. Game terminates if gameon becomes false at the end of the game due to a user input.
	game_on = True
	
	#play game only when no exit flag has been called
	while game_on:

		num_moves+=1

		#how to play game for a respective number of players

		#if 2 players playing
		if num_players ==2:
			if num_moves<2:

				#printing to the screen which player goes first as obtain from the first turn
				print(players[first_turn], "will go first. ")
		    
			if (num_moves-1)%2 ==0:
				player_ch= player1 
			elif (num_moves-1)%2 == 1:
				player_ch = player2
			putChecker(player_ch)
			update_board()
			
			

        #if 3 players playing
		elif num_players ==3:
			if num_moves<2:
				print(players[first_turn], "will go first. ")
			
			if (num_moves-1)%3 ==0 :
				player_ch = player1
			elif (num_moves-1)%3 ==1:
				player_ch = player2
			else:
				player_ch = player3

			putChecker(player_ch)
			update_board()
			



		#if 4 players playing
		elif num_players ==4:
			if num_moves<2:
				print(players[first_turn], "will go first. ")
			
			if (num_moves-1)%4 ==0 :
				player_ch = player1
			elif (num_moves-1)%4 ==1:
				player_ch = player2
			elif (num_moves-1)%4 ==2 :
				player_ch = player3
			else:
				player_ch = player4

			putChecker(player_ch)
			update_board()
			

        #if 5 players playing
		else:
			if num_moves<2:
				print(players[first_turn], "will go first. ")
			
			if (num_moves-1)%5 ==0:
				player_ch = player1

			elif (num_moves-1)%5 ==1:
				player_ch =player2

			elif (num_moves-1)%5 ==2:
				player_ch =player3

			elif (num_moves-1)%5 ==3:
				player_ch =player4
			else:
				player_ch =player5

				

			putChecker(player_ch)
			update_board()
			

        
        #executes only if a winner has been spotted and the winnercheck function returns true and breaks the gameplay
		if winnerCheck() == True:

			#winner of two TWO PLAYERS
			if num_players ==2:
				if (num_moves-1) %2 == 0:     
					print('Player',player1, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
					str = input(prompt)
					s = playAgain(str)
					if s == True:
						if str== 'y' or str=="Y" :

							#This is printed to the screen if the players key in y or Y which means they want to play again
							print(' Yes you do, Lets go once again ')


							#lines of code to reset the board for a new game
							for row in range(ROWS):
								for col in range(COLS):
									board[row][col]=' '
							main()

				

						elif str=="n" or str == "N":
							print(' No you dont, Goodbye! ')


							#game_on sets to false by a user keying in n/N in this case breaks the game and it ends abruptly
							game_on = False

					else:

						#game_on sets to false by a user keying in an incorrect value like just the enter key without any input or
						# .... something other than y,Y,n,N in this case breaks the game and it ends abruptly
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False

				if (num_moves-1) %2 == 1:
					print('Player',player2, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False

            


            #winner of THREE PLAYERS
			elif num_players ==3:
				if (num_moves-1) %3 == 0:  
					print('Player',player1, "won!")
					#lines added to replay the game if the players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False

				if (num_moves-1) %3 == 1:
					print('Player',player2, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False


				if (num_moves-1) %3 == 2:
					print('Player',player3, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False




			#winner of FOUR PLAYERS
			elif num_players == 4:
				if (num_moves-1) %4 == 0:  
					print('Player',player1, "won!")
					#lines added to replay the game if the players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no...anything apart from these breaks the game    ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False

				if (num_moves-1) %4 == 1:
					print('Player',player2, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False


				if (num_moves-1) %4 == 2:
					print('Player',player3, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False



				if (num_moves-1) %4 == 3:
					print('Player',player4, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no...anything apart from these breaks the game    ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False


            #winner of FIVE PLAYERS
			elif num_players ==5:
				if (num_moves-1) %5 == 0:  #FIVE PLAYERS
					print('Player',player1, "won!")
					#lines added to replay the game if the players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False

				if (num_moves-1) %5 == 1:
					print('Player',player2, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False


				if (num_moves-1) %5 == 2:
					print('Player',player3, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False



				if (num_moves-1) %5 == 3:
					print('Player',player4, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False


				if (num_moves-1) %5 == 4:
					print('Player',player5, "won!")
					#lines added to replay the game if the 2 players want to
					prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game   ")
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
							game_on = False

					else:
						print("Sorry incorrect input type. Goodbye! ")
						game_on = False




		



        # winner function from above is run first then the board full function will tell if its a DRAW after the winner function gives a no outcome whatsoever
		elif boardFull() == True:					
			print("All the columns are full with NO winner. The game ends in a Draw, WOW Brainiacs")
			#lines added to replay the game if the 2 players want to
			prompt=("Do you want to play again Y or y/ N or n for yes or no... anything apart from these breaks the game  ")
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
					game_on = False

			else:
				print("Sorry incorrect input type. Goodbye! ")
				game_on = False



#function that checks if only the top row is full as checker is placed from bottom up to predict that the  board is full
def boardFull():
	for r in range(1):
		for c in range(COLS):
			if board[r][c] == " ":
				return False

	return True
			

			


				
#function that checks for a winner vertically, horizontally, positive diagonally and negative diagonally and sets winner to TRUE if it finds one such case
def winnerCheck():
	#CHECK A WINNER VERTICALLY
	for c in range(COLS):
		for r in range(ROWS-1,2,-1):
		    if  (board[r][c] == "X" and board[r-1][c] == "X" and board[r-2][c] == "X" and board[r-3][c] == "X") or \
		    	(board[r][c] == "O" and board[r-1][c] == "O" and board[r-2][c] == "O" and board[r-3][c] == "O") or \
		    	(board[r][c] == "M" and board[r-1][c] == "M" and board[r-2][c] == "M" and board[r-3][c] == "M") or \
		    	(board[r][c] == "H" and board[r-1][c] == "H" and board[r-2][c] == "H" and board[r-3][c] == "H") or \
		    	(board[r][c] == "V" and board[r-1][c] == "V" and board[r-2][c] == "V" and board[r-3][c] == "V"):
		    	return True

	
		   

	#CHECK A WINNER HORIZONTALLY
	for c in range(COLS-3):
		for r in range(ROWS-1,2,-1):
		    if  (board[r][c] == "X" and board[r][c+1] == "X" and board[r][c+2] == "X" and board[r][c+3] == "X") or \
		    	(board[r][c] == "O" and board[r][c+1] == "O" and board[r][c+2] == "O" and board[r][c+3] == "O") or \
		    	(board[r][c] == "M" and board[r][c+1] == "M" and board[r][c+2] == "M" and board[r][c+3] == "M") or \
		    	(board[r][c] == "H" and board[r][c+1] == "H" and board[r][c+2] == "H" and board[r][c+3] == "H") or \
		    	(board[r][c] == "V" and board[r][c+1] == "V" and board[r][c+2] == "V" and board[r][c+3] == "V"):
		    	return True
	



	


	#CHECK A WINNER ON POSITIVELY SLOPED DIAGONAL
	for c in range(COLS-3):
		for r in range(ROWS-1,2,-1):
		    if  (board[r][c] == "X" and board[r-1][c+1] == "X" and board[r-2][c+2] == "X" and board[r-3][c+3] == "X") or \
		    	(board[r][c] == "O" and board[r-1][c+1] == "O" and board[r-2][c+2] == "O" and board[r-3][c+3] == "O") or \
		    	(board[r][c] == "M" and board[r-1][c+1] == "M" and board[r-2][c+2] == "M" and board[r-3][c+3] == "M") or \
		    	(board[r][c] == "H" and board[r-1][c+1] == "H" and board[r-2][c+2] == "H" and board[r-3][c+3] == "H") or \
		    	(board[r][c] == "V" and board[r-1][c+1] == "V" and board[r-2][c+2] == "V" and board[r-3][c+3] == "V"):
		    	return True
	



	#CHECK A WINNER ON NEGATIVELY SLOPED DIAGONAL
	for c in range(COLS-1,2,-1):
		for r in range(ROWS-1,2,-1):
		    if  (board[r][c] == "X" and board[r-1][c-1] == "X" and board[r-2][c-2] == "X" and board[r-3][c-3] == "X") or \
		    	(board[r][c] == "O" and board[r-1][c-1] == "O" and board[r-2][c-2] == "O" and board[r-3][c-3] == "O") or \
		    	(board[r][c] == "M" and board[r-1][c-1] == "M" and board[r-2][c-2] == "M" and board[r-3][c-3] == "M") or \
		    	(board[r][c] == "H" and board[r-1][c-1] == "H" and board[r-2][c-2] == "H" and board[r-3][c-3] == "H") or \
		    	(board[r][c] == "V" and board[r-1][c-1] == "V" and board[r-2][c-2] == "V" and board[r-3][c-3] == "V"):
		    	return True
	


		    

	





# function that uses checkInput function before placing a checker X or O or M or V or H on the board and can tell if a column is full
def putChecker(player_ch):

	#constantly accept input for the number of players
	while True:
		prompt='Player '+ player_ch + ',please enter a column'+': '
		str = input(prompt)
		# call check inputChecker function to check for correct
		# ... input type else return false and print re-enter 
		s = checkInput(str)
		if s == True:
			c = (ord(str[0]) - 65)

			#checks if column letter entered is on the board and if not prints whats below
			if c<0 or c>=COLS:
				print("Out of range. Re-enter. ")

			#checks if a column full and prints whats below
			elif colFull(str) == True:
				print("Column", str, "is full, Enter a different column letter")



			else:
				#places checker by first looping to see if a bottom row in a column is not empty
				if c==0 or c==1 or c == 2 or c==3 or c==4 or c==5 or c==6 or c == 7 or c==8 or c==9 or c==10  \
				or c==11 or c==12 or c==13 or c==14 or c == 15 or c==16 or c==17 or c==18 or c==19 or c==20 \
				or c==21 or c==22 or c ==23 or c==24 or c==25 or c==26 :
					for r in range(ROWS-1,-1,-1):
						if board[r][c] == " ":
							board[r][c] = player_ch
							return 
								



            # print board and break from while loop
				print_board()
				break


			    
		# asks user to re-enter input as checkinput failed		
		else:
				print("Incorrect input type. Re-enter. ")






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




# function that checks to see if a column is full or not
def colFull(cell):
	c = (ord(cell)-65)
	for r in range(0,ROWS):
	 	if board[r][c] != " ":
	 		return True
	 	else:
	 		return False  


# checks user input as a correct number of players
# .... required for a gameplay
def checkNumPlayers(str):
	if len(str)<1 or len(str)>1:
		return False
	elif len(str)==1 and str.isdigit() and 2<= int(str) <=5:
		return True
	else:
		return False



# function that prints the 2D board
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
		print(" "+" | ", end="")
		for col in range(COLS):
			print(board[row][col]+" | ", end="")
		print("\n  +" + "---+" * COLS)

def update_board():
	#sleep,clear the screen and print recently updated board
	time.sleep(0.5)
	os.system("clear")
	print_board()



# checks user input as correct position on the board
# .... and in the correct format of capital letter for a column	
def checkInput(str):
	if len(str)<1 or len(str)>1:
		return False

	elif len(str)==1 and str[0] in letters:
		return True 

		
	elif str[0] not in letters:
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



if __name__ == "__main__":
	main()
