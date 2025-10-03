from time import sleep



#decides board size and creates the board
game_dimensions = {"x" : 10,"y" : 10}

EMPTY = "."
board = []

#clamp function, returns an int within provided range
def clamp(value,min_val,max_val):
    return max(min_val,min(value,max_val))

#makes the board as a matrix by looping through the x and y values of the game_dimensions
for y in range(0,game_dimensions["y"]):
    new_row = []
    for x in range(0,game_dimensions["x"]):
        new_row.append(EMPTY)
    
    board.append(new_row)


#all of this is enemy nonsense
# basic reusable class for enemies
class enemy:
    def __init__(self, name: str, visual: str, hp: int, atk: int, spd: int, defense: int, x:int,y:int):

        #data that is consistent for all enemies
        self.visual = visual
        self.name = name

        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.defense = defense

        #position values
        self.x = x
        self.y = y
    def move(self,x_move,y_move):
        #current_space
        board[self.y][self.x] = EMPTY
        #target_space
        self.y = clamp(self.y + y_move, 0, game_dimensions["y"]-1)
        self.x = clamp(self.x + x_move, 0, game_dimensions["x"]-1)
        board[self.y][self.x] = self.visual
        
def spawn(instance: any, x, y):
    if type(instance) is enemy:
        instance.x = x
        instance.y = y

        board[y][x] = instance.visual


#Game nonsense
#Renders the full game board, adding spacing inbetween the objects to spread out the positions evenly in a visual grid
def render_board():
    for row in board:
        for space in row:
            space_filling = "   " + space + "   "
            print(space_filling,end="")
        print("\n")



new_enemy = enemy("gogad","🥸",10,5,1,0,0,0)
spawn(new_enemy,5,5)


while True:
    render_board()
    sleep(1)
    new_enemy.move(1,0)