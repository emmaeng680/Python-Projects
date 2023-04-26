#Emmanuel A Oppong
#22nd April 2023


#importing random module to handle events that should be done at random during gameplay
import random

#creaing a general list that contains all the colour codes needed for this game
COLOR_LIST = [color(255, 51, 52), color(12, 150, 228), color(30, 183, 66), color(246, 187, 0), color(76, 0, 153), color(255, 255, 255),color(0, 0, 0)]

#Declaratin of some global constants for the game
GAME_WIDTH = 200
GAME_HEIGHT = 400
ROWS = 20
COLS = 10


#Creation of a Piece class
#Piece class can create rectangular blocks at a definite place on the processing canvas
class Piece:
    #initialization of piece class
    def __init__(self,x,y,color): 
       
        #declaration of piece class attributes 
        self.x = x
        self.y = y
        self.color = color
    
        # displays the piece created at the specific x,y on the processing canvas by first passing a colour to it
    def display(self):
        
        fill(self.color)
        stroke(180)
        rect(self.y*20, self.x*20, 20, 20)
        
#Creating of a Tetrimino block which inherits from the Piece class but unlike the Piece class its spawned with a random color from the color list 
class TetriBlock(Piece):
    
    #initialization of tetriblock class
    def __init__(self,x,y):
        
        #passing on properties of Piece class to the TetriBlock class (inheritance)
        Piece.__init__(self,x,y,random.choice(COLOR_LIST)) 
        
        #defining a way to control a spawned tetrimino in gameplay using the keyboard right and left keys
        self.keyhandler = {LEFT: False, RIGHT:False}
        
        #used during game time to know current speed of block -- it acts more as a boolean in code instances below
        self.speed = 1
        
    #displays currently generated tetrimino
    def display(self):
        """Display the grid piece."""
        fill(self.color)  
        stroke(180) 
        rect(self.y*20, self.x*20, 20, 20)
        self.move_down()
        self.move_sideways()
        
    
    #defining method to control how the coloured tetrimino moves down and conditions to be satisfied  
    def move_down(self):
        
        if game.currentblock.x+1 < ROWS:
            game.currentblock.x+= self.speed
            
        else:
            game.currentblock.speed = 0
            if game.check_collision() ==True:
                game.speed +=0.25
            
            
     #defining methods to control how the coloured tetrimino move right or left and conditions to be satisfied      
    def move_sideways(self):
        #First chcking for horizontal overlap of a dropping block with filled columns to prevent such an overlapping movement
        # if true block column does not have to change
        if game.check_hor_collision() == True:
            game.currentblock.y = game.currentblock.y
        elif self.y>0 and self.keyhandler[LEFT] == True :
            game.currentblock.y -=self.speed
            
        elif self.y<COLS-1 and self.keyhandler[RIGHT] == True :
            game.currentblock.y +=self.speed
            
            
#Definition of a game class to handle gameplay
class Game:
    #initialization of game class
    def __init__(self):
        
        #definition of game class attributes
        self.score = 0
        # game speed starts at 9 upon game commencement, reset back to this later on after four tetriminos of same color is detected
        self.speed = 9
        
        # a boolean to check that game is currently running
        self.gameon = True
        # create an empty 2D list to store the game objects. it is empty at the beginning of the game as its appended with ' '
        self.game_objects = []
        for row in range(ROWS):
            a_row = []
            for col in range(COLS):
                a_row.append(' ')
            self.game_objects.append(a_row)
            
                
        #generating first tetriBlock with a random color    
        self.generate_tetriblock()
                
   #defining a method that generate tetrimino blocks in only columns that are not fully filled
    def generate_tetriblock(self):
        non_full_cols = [col for col in range(COLS) if self.check_non_fullcolumn(col) == True ]
        
        if non_full_cols:
            random_col = random.choice(non_full_cols)
        else:
            random_col = random.randint(0, COLS - 1)
   ### generating block outside grid so that grid can become full with time with no bugs in block generation
   #I later use the gridFull function to check if the games block_objects nested list (game grid) is full or not before generating a new block
        self.currentblock = TetriBlock(-2, random_col)
        
        ### Updating tetrimino block speed
        ####if it breaks put this back
        self.currentblock.speed =+ 1
        return self.currentblock
    
    #check for headon vertical collision of a dropping block with blocks below in th grid to prevent vertical overlap of blocks in columns
    def check_collision(self):
        if  self.currentblock.x+1 < ROWS and self.game_objects[self.currentblock.x+1][self.currentblock.y] != ' ':
            self.speed+=0.25
            # self.game_objects[self.currentblock.x][self.currentblock.y] = self.currentblock
            self.currentblock.speed = 0
            return True
        return False
    
    def blockgenerated(self):
        if self.generate_block:
            print('block generated')
            return True
        return False
    
    ### check horizontal collision to prevent a moving block's overlap with filled column 
    ### keyhandlers are set to False to help get around this case
    def check_hor_collision(self):
        if self.currentblock.y+1 < COLS and self.game_objects[self.currentblock.x][self.currentblock.y+1] != ' ':
            self.currentblock.keyhandler[RIGHT] = False
            return True
        elif self.currentblock.y-1 >=0 and self.game_objects[self.currentblock.x][self.currentblock.y-1] != ' ':
            self.currentblock.keyhandler[LEFT] = False
            return True
        return False
    
    
    #function that checks whether a column is full or not full, was used above for block generation in partially filled 
    #...columns only during gameplay
    def check_non_fullcolumn(self,y):
        if y+1<COLS or y-1>=0:
            ### ... over here i check that a column is not full if its top row still contains an empty string ie. ' '
            ### in some other cases I use the gray colour code -2960686 in processing for checks below
            if self.game_objects[0][y] == ' ':
                return True
        return False
    
 
   ### ... only if not even one empty string ie ' ' initially appended to only the the game_objects 2D list top row
   ##... still has its empty string ie. ' ' value   
    def gridFull(self):
        for element in self.game_objects[0]:
             if element == ' ':
                 return False
        return True
    
    ### method checks to find 4 blocks on the game_objects 2D grid that have same colour other than their spots being empty and takes them out of grid
    #...by reseting such spots back to an empty space
    def check_same_connect4(self):
        for col in range(COLS):
            for row in range(ROWS-1, 2, -1):
                if self.game_objects[row][col] != ' ' and  self.game_objects[row-1][col] != ' ' and self.game_objects[row-2][col] != ' ' and self.game_objects[row-3][col] != ' ':

                    if (self.game_objects[row][col].color == self.game_objects[row-1][col].color == self.game_objects[row-2][col].color == self.game_objects[row-3][col].color):
                        self.game_objects[row][col] = ' '
                        self.game_objects[row-1][col] = ' '
                        self.game_objects[row-2][col] = ' '
                        self.game_objects[row-3][col] = ' '
                        ###  Game speed is reset back to initial value of 9 after a connected 4 of same color is found
                        self.speed = 9
                        self.score +=1
                        
                        
                        return True
        #updating game speed after any block comes to rest even without finding 4 of same color
        self.speed+=0.25       
        return False
            
    # method displays the game_objects 2D list objects as a beautiful grid when the code is run. 
    def display(self):
        
        ### print out empty spots as rectangles with a gray color and call tetrimino block piece display method to show color for spots containing tetriminos
        for row in range(ROWS):
            for col in range(COLS):
                if self.game_objects[row][col] == ' ':    
                    fill(210)
                    stroke(180)
                    rect(col*20,row*20,20,20)
                else:
                    if self.game_objects[row][col] != ' ': 
                        self.game_objects[row][col].display()
        # calling TetriBlock display method on current tetrimino block generated to show it
        self.currentblock.display()
        
        #checking for headon vertical collisions once a block is generated
        self.check_collision()
        
        ###### check to see if 4 blocks of same color are stacked up vertically
        self.check_same_connect4()
        
        #Generate a new block if the current block comes to rest and increase game speed
        if self.currentblock.speed == 0 and self.gridFull() == False:
            self.game_objects[self.currentblock.x][self.currentblock.y] = self.currentblock
            self.speed +=0.25 
            self.generate_tetriblock()
            
        ## Game must stop running if game_objects 2D grid becomes full and checking a connected 4 upon last dropped block in the grid..
        ## ...doesnt return a vertical allignment of 4 blocks
        if self.gridFull() == True and self.check_same_connect4() == False:
            self.gameon = False
            
#creating an istance of the game object         
game = Game()
 
#general processing canvas set up for game            
def setup():
    size(GAME_WIDTH,GAME_HEIGHT)
    background(210)
    
    ## game speed always passed to frameRate to manage it during gameplay
    frameRate(game.speed)

    
def draw():
    # making game instance always available as global variable
    global game
    
    # using assignment game slow down code to make game run smoothly
    if frameCount%(max(1, int(8 - game.speed)))==0 or frameCount==1:
        background(210)
        #this calls the display method of the game class for main game running
        if (game.gameon == True):    
            game.display()
            fill(0)
            textSize(15)
            text('Score  : {}'.format(game.score),130,20)

     #this sets up a new game after the game has halted and the mouse is pressed at such a time 
        elif game.gameon == False and mousePressed:
            game = Game()
            game.display()
            
        #this displays the final score if the current game ends and the mouse hasn't been pressed yet    
        else:
            for row in range (ROWS):
                for col in range(COLS):
                    fill(210)
                    stroke(180)
                    rect(col*20,row*20,20,20)
                    
            # prints this text at the center of the canvas
            fill(0)
            textSize(15)
            text('  Game Over! \n Final Score: {}'.format(game.score),50,180)
     
    

# ## Defining keypressed functionalities to make game interactive
def keyPressed():
    if keyCode == LEFT:
        game.currentblock.keyhandler[LEFT] = True
        
    elif keyCode == RIGHT:
        game.currentblock.keyhandler[RIGHT] = True

#Defining what happens when keys are released and there is no more user-game interactivity
def keyReleased():
    if keyCode == LEFT:
        game.currentblock.keyhandler[LEFT] = False
        
    elif keyCode == RIGHT:
        game.currentblock.keyhandler[RIGHT] = False
        
        
