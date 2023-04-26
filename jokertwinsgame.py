# Oppong Emmanuel
# 26th February, 2023

#importation of some important modules for the general code
import random, os, time

#Defining rows and columns of the gameboard as global constants
ROWS=5
COLS=5

#Defining the number of players as a global constant 
NUM_PLAYERS=2

#Defining a list of alphabets for printing the gameboard 
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# use random module to generate 0 and 1 at random for a random player to start the game
first_turn = random.randint(0, NUM_PLAYERS-1)

#Initialize the player scores as a list
scores = [0] * NUM_PLAYERS

# creating the two main boards as lists with empty entries
#Board 1 is displayed 
board_one=[]
for row in range(ROWS):
		row_list=[]
		for col in range(COLS):
			row_list.append(" ")
		board_one.append(row_list)


#Board 2 is hidden during gameplay
board_two=[]
for row in range(ROWS):
		row_list=[]
		for col in range(COLS):
			row_list.append(" ")
		board_two.append(row_list)



#Appending Board 1 with #'s for every entry in it for the main game
for row in range(ROWS):
	for col in range(COLS):
		board_one[row][col] = '#'

#Defining Ascii numbers for the Letters A and a respectively
capitalA = 65
smalla = 97



#Appending Board 2 with letters for every entry in it for the main game	
#if sum of row and col is even append a capital letter and increase counter by 1 so that next capital letter is placed in 
#... next odd numbered spot. If letter is O reset to capital A

#if sum of row and col is odd append a small letter and increase counter by 1 so that next small letter is placed in 
#... next even numbered spot. If letter is o reset to small a 

for row in range(ROWS):
	for col in range(COLS):
		if (row+col)%2 == 0:
			if chr(capitalA) == 'O':
				capitalA = 65

			board_two[row][col]= chr(capitalA)
			capitalA += 1

		elif (row+col)%2 == 1:
			if chr(smalla) == 'o':
				smalla = 97
			board_two[row][col]= chr(smalla)
			smalla += 1


# ROWS * COLS = board dimension
# if board dimension is even append 2 jokers (* *)
# else append 3 jokers (* * *)
if (ROWS*COLS)%2 ==  0:
	board_two[ROWS-1][COLS-2], board_two[ROWS-1][COLS-1]  = '*','*'
else:
	board_two[ROWS-1][COLS-3],board_two[ROWS-1][COLS-2], board_two[ROWS-1][COLS-1]  = '*','*','*'


#shuffling rows in the hidden BOARD2 before gameplay		
for row in board_two:
	random.shuffle(row)


#extra shuffling of entries in the hidden BOARD2 before gameplay
for col in range(COLS):
	newcolumn = [board_two[row][col] for row in range(len(board_two))]
	random.shuffle(newcolumn)
	for row in range(len(board_two)):
		 board_two[row][col] = newcolumn[row]


#Defining code for the main gameplay		
def main():

	#setting a condtion to continue accepting coordinates from the players during gameplay	
	game_on = True
	num_moves = 0
	while game_on:
					#Defining what is printed at the beginning of the game
					# Will later prevent this from printing by increamenting it with each player turn
					if num_moves < 1:
						print("Player 2 score: {}".format(scores[1]))
						print("Player 1 score: {}".format(scores[0]))
						print_first_board()

					#Calling on the BoardEmpty function to check for an empty board, break the game and print the game's end results 
					#... if it returns a True
					if boardEmpty() == True:
									time.sleep(2)
									os.system("clear")
									print_first_board()


									#Defining what gets printed on the screen at the end of the game
									print("Game over!")
									print_first_board()
									print(f"Player 1: {scores[0]}    Player 2: {scores[1]}")
									if scores[0] > scores[1]:
										print("Player 1 wins!")
									elif scores[1] > scores[0]:
										print("Player 2 wins!")
									else:
										print("It's a tie!")

									#Asking players if they want to play again 
									# if input is Y or y then a new game starts
									#Anything other than a Y or y stops the game
									playagain = input("Do you want to play again? (y/n)...  ").lower()
									if playagain == 'y':
										print()
										scores[0] = 0
										scores[1] = 0
										restart_game()
										main()

									elif playagain != 'y':
										print()
										print("Goodbye. Thanks for playing!")
										break
								

				#UNCOMMENT LINE BELOW with Cmd+? after selecting TO SEE 2ND GAMEBOARD AT EVERY NEW TURN FOR QUICK TESTING OF GAMEPLAY

					# print_second_board()
					

					#flags to help accept coordinates while certain contains are satisfied
					exit_cord1 = False
					exit_cord2 = False


					#making first turn global so that it is used in every part of the game
					global first_turn

					#players are player 0 or player 1 from the modulus in the first line
					#However this gets increased by 1 in the second line to correctly print player 1 and player 2
					player = first_turn%2
					print(f"Player {player+1}'s turn")


					# ACCEPT 1ST coordinate while a turn is over or returned
					while not exit_cord1:

						# call valid_coordinate() function to check for correct
						# ... input type for 1st coordinate else return false and print re-enter 
						cord1 = input(f"Player {player+1}: Enter first coordinate (e.g. A3): ")
						s = valid_coordinate(cord1)
						if s == True:

							#converting correct player input to coordinate for location on the gameboard
							#same as in code 2nd coordinate
							c = (ord(cord1[0]) - 65)
							r = int(cord1[1])

							#check that we dont go out of the board and inform the player if that is the case
							if r <0 or r>=ROWS or c<0 or c>=COLS:
								print("Out of range. Re-enter. ")
								continue

							#Store value at first coordinate as first card and store its row and col...
							# ... for later checks
							CARD1 = board_two[r][c]
							CARD1_ROW = r
							CARD1_COL = c

							#check to see that coordinate selected by a player does not return an empty spot on the two gameboards
							# whatever gets removed from displayed gameboard 1 is removed from my hidden gameboard 2
							if CARD1 == ' ':
								print("Empty spot on board, Re-enter ")
								continue

							#if the first coordinate is a correct one (letter or joker and not empty) assign its value to card1 for display on board
							else:
								board_one[r][c] = CARD1
								print_first_board()
								time.sleep(2)
								os.system("clear")
								
								#reset board_one to all #'s after displaying card
								reset_board_one()
								print_first_board()

								#break out of coordinate 1 if its a correct input
								exit_cord1 = True

						else:
							print("Incorrect input type. Re-enter. ")

					

					# ACCEPT 2ND coordinate for a player's turn
					while not exit_cord2:

						# call valid_coordinate() function to check for correct
						# ... input type for 2nd coordinate else return false and print re-enter 
						cord2 = input(f"Player {player+1}: Enter second coordinate (e.g. A3): ")
						s = valid_coordinate(cord2)
						if s == True:
							c = (ord(cord2[0]) - 65)
							r = int(cord2[1])
							#check that we dont go out of the board
							if r <0 or r>=ROWS or c<0 or c>=COLS:
								print("Out of range. Re-enter. ")
								continue

							#Store value at 2nd coordinate as second card and store its row and col...
							# ... to later help to identify SIMILAR INPUT AS BEFORE
							CARD2 = board_two[r][c]
							CARD2_ROW = r
							CARD2_COL = c

							#check to see that coordinate selected by a player does not return an empty spot on the two gameboards
							# whatever gets removed from displayed gameboard 1 is removed from my hidden gameboard 2
							if CARD2 == ' ':
								print("Empty spot on board, Re-enter ")
								continue


							# IDENTIFYING A SIMILAR INPUT AS BEFORE
							elif CARD1_ROW == CARD2_ROW and CARD1_COL == CARD2_COL:
								print("Same Entry as before, Re-enter ")
								continue

							#if the second coordinate is a correct one (letter or joker and not empty) assign its value to card2
							else:
								board_one[r][c] = CARD2
								print_first_board()
								time.sleep(2)
								os.system("clear")

								#reset board_one to all #'s after displaying card
								reset_board_one()
								print_first_board()

								#break out of coordinate 2 if its a correct input
								exit_cord2 = True



			            # Unhide the cards by displaying the 2 cards selected 
			            #...if they are two jokers or two letters 
			            #... or display the 3 cards if joker, letter and its twin)
							board_one[CARD1_ROW][CARD1_COL] = CARD1
							board_one[CARD2_ROW][CARD2_COL] = CARD2

							#Defining the conditions for displaying the third card of the 3 cards
							# that's when there is a joker and a letter chosen and we need the letter's twin to show
							if (CARD1 == '*' and CARD2.isalpha()):
								twin = CARD2.swapcase()
								count = 0
								for row in range(ROWS):
									for col in range(COLS):
										if board_two[row][col] == CARD2.swapcase() and count <1:
											board_one[row][col] = twin
											count +=1

							if (CARD2 == '*' and CARD1.isalpha()):
								twin = CARD1.swapcase()
								count = 0
								for row in range(ROWS):
									for col in range(COLS):
										if board_two[row][col] == CARD1.swapcase() and count <1:
											board_one[row][col] = twin
											count +=1


							#waiting for some time so the players memorize position of turned over cards
							print_first_board()
							time.sleep(2)
							reset_board_one()


					#Defining conditions for removing checkers on both boards during gameplay
					#A player should be able to play again if one of the first 2 conditions defined below is true 
					#..or else he loses his turn
					#If the player satisfies one of the first 2 conditions he gets to play again. This was done by INCREMENTING THE PLAYER TURN HERE 
					# ... BEFORE ITS INCREASE AGAIN DOWN BELOW TO BRING AS BACK TO THE SAME OLD PLAYER 


					#Checking for letter twins and replacing places where they are found with spaces as well its equivalent scores
					if (CARD1 == CARD2.swapcase()) and (CARD1.isalpha() and CARD2.isalpha()) :
								board_one[CARD1_ROW][CARD1_COL] = CARD1
								board_one[CARD2_ROW][CARD2_COL] = CARD2
								# time.sleep(2)
								scores[player] += 1


								
								
								#REMOVED # checkers are replaced with single spaces 
								board_one[CARD1_ROW][CARD1_COL] = ' '
								board_one[CARD2_ROW][CARD2_COL] = ' '
								board_two[CARD1_ROW][CARD1_COL] = ' '
								board_two[CARD2_ROW][CARD2_COL] = ' '
								os.system("clear")


								
								# time.sleep(2)
								os.system("clear")
								print("Player 2 score: {}".format(scores[1]))
								print("Player 1 score: {}".format(scores[0]))
								print_first_board()
								print(f"Player {player+1} found a twin")
								print(f"Hey Player {player+1} you found a twin : Enter another set of coordinates (e.g. A3): ")

								#INCREMENTING THE PLAYER TURN HERE 
								# ... BEFORE ITS INCREASED AGAIN DOWN BELOW TO BRING AS BACK TO THE SAME OLD PLAYER 
								first_turn += 1


					#Checking whether a joker was found and defining conditions for removing a joker and a joker 
					#...or a joker and then a letter and its twin as well as their respective scores
					elif CARD1 == '*' or CARD2 =='*':
								board_one[CARD1_ROW][CARD1_COL] = CARD1
								board_one[CARD2_ROW][CARD2_COL] = CARD2
								time.sleep(2)
								if CARD1.isalpha():
									scores[player] += 2
									count = 0

									#loop through board 2 to find just find one swapcase (twin) of letter that paired with a joker the removed its checkers from both boards
									for row in range(ROWS):
										for col in range(COLS):
											if board_two[row][col] == CARD1.swapcase() and count <1:

												#REMOVED # checkers are replaced with single spaces 
												board_two[row][col] = ' '
												board_one[row][col] = ' '
												count +=1
												


								elif CARD2.isalpha():
									scores[player] += 2
									count = 0
									for row in range(ROWS):
										for col in range(COLS):
											if board_two[row][col] == CARD2.swapcase() and count <1:

												#REMOVED # checkers are replaced with single spaces 
												board_two[row][col] = ' '
												board_one[row][col] = ' '
												count +=1


								elif CARD1 =='*' and CARD2 == '*':
									scores[player] += 2

								#REMOVED # checkers are replaced with single spaces 
								board_one[CARD1_ROW][CARD1_COL] = ' '
								board_one[CARD2_ROW][CARD2_COL] = ' '
								board_two[CARD1_ROW][CARD1_COL] = ' '
								board_two[CARD2_ROW][CARD2_COL] = ' '

								os.system("clear")
								print("Player 2 score: {}".format(scores[1]))
								print("Player 1 score: {}".format(scores[0]))
								print_first_board()
								print(f"Player {player+1} found a joker")
								print(f"Hey Player {player+1} you found a joker twin : Enter another set of coordinates (e.g. A3): ")

								#INCREMENTING THE PLAYER TURN HERE 
								# ... BEFORE ITS INCREASED AGAIN DOWN BELOW TO BRING AS BACK TO THE SAME OLD PLAYER 
								first_turn += 1


					#Defining conditions for when neither a joker nor a twin is found by the current player
					elif not (CARD1 == CARD2.swapcase()) and (not(CARD1 == '*' or CARD2 =='*')) :
								time.sleep(2)
								board_one[CARD1_ROW][CARD1_COL] = CARD1
								board_one[CARD2_ROW][CARD2_COL] = CARD2
								reset_board_one()
								os.system("clear")
								print("Player 2 score: {}".format(scores[1]))
								print("Player 1 score: {}".format(scores[0]))
								print_first_board()
								print(f"Player {player+1} did not find a twin nor a joker, turn lost")

					#increase num_moves by one to prevent printing the first style of screen on game start
					num_moves =+1

					#MAIN PARAMETER to increase first turn so that current player changes
					first_turn += 1



#Defining a function that prints the first board
def print_first_board():
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
			print(board_one[row][col]+" | ", end="")
		print("\n  +" + "---+" * COLS)


#Defining a function that prints the SECOND board
def print_second_board():
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
			print(board_two[row][col]+" | ", end="")
		print("\n  +" + "---+" * COLS)


#Defining a function that checks whether an input coordinate is valid
def valid_coordinate(cord):
	if len(cord)!=2 :
		return False

	col = cord[0]
	row = cord[1]
	
	if not (col.isalpha() and col.isupper()) or not row.isdigit():
		return False


	return True

#Defining a function that resets the board to all #'s after entries are revealed for sometime during gameplay
def reset_board_one():
	time.sleep(0.5)
	os.system("clear")
	for row in range(ROWS):
		for col in range(COLS):
			if board_one[row][col].isalpha() or board_one[row][col] == '*':
				board_one[row][col] = '#'

#Defining a function that checks for the end of the game by checking to see if all entries of the 
#....gameboard are empty spaces
def boardEmpty():
	for row in range(ROWS):
		for col in range(COLS):
			if board_one[row][col] == '#':
				return False

	return True

def restart_game():
		#Appending Board 1 with #'s for every entry in it for the main game
	for row in range(ROWS):
		for col in range(COLS):
			board_one[row][col] = '#'

	#Defining Ascii numbers for the Letters A and a respectively
	capitalA = 65
	smalla = 97



	#Appending Board 2 with letters for every entry in it for the main game	
	#if sum of row and col is even append a capital letter and increase counter by 1 so that next capital letter is placed in 
	#... next odd numbered spot. If letter is O reset to capital A

	#if sum of row and col is odd append a small letter and increase counter by 1 so that next small letter is placed in 
	#... next even numbered spot. If letter is o reset to small a 

	for row in range(ROWS):
		for col in range(COLS):
			if (row+col)%2 == 0:
				if chr(capitalA) == 'O':
					capitalA = 65

				board_two[row][col]= chr(capitalA)
				capitalA += 1

			elif (row+col)%2 == 1:
				if chr(smalla) == 'o':
					smalla = 97
				board_two[row][col]= chr(smalla)
				smalla += 1


	# ROWS * COLS = board dimension
	# if board dimension is even append 2 jokers (* *)
	# else append 3 jokers (* * *)
	if (ROWS*COLS)%2 ==  0:
		board_two[ROWS-1][COLS-2], board_two[ROWS-1][COLS-1]  = '*','*'
	else:
		board_two[ROWS-1][COLS-3],board_two[ROWS-1][COLS-2], board_two[ROWS-1][COLS-1]  = '*','*','*'


	#shuffling rows in the hidden BOARD2 before gameplay		
	for row in board_two:
		random.shuffle(row)


	#extra shuffling of entries in the hidden BOARD2 before gameplay
	for col in range(COLS):
		newcolumn = [board_two[row][col] for row in range(len(board_two))]
		random.shuffle(newcolumn)
		for row in range(len(board_two)):
			 board_two[row][col] = newcolumn[row]





if __name__ == "__main__":
	main()




