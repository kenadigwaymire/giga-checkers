#Board should have a list of pieces which will be piece objects
import pygame

class Board:
    RED = (255, 0, 0)
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)
    GOLD = (212, 175, 55)
    SQUARE_WIDTH = 100
    SQUARE_HEIGHT = 100

    def __init__(self):
        self.board = []
        self.screen = None
        self.x_size = 0
        self.y_size = 0
        self.screen_size_x = 0
        self.screen_size_y = 0
    
    def draw_board(self, screen, screen_size_x, screen_size_y, x_size, y_size):
        self.screen = screen
        self.screen_size_x = screen_size_x
        self.screen_size_y = screen_size_y
        self.x_size = x_size
        self.y_size = y_size
        for i in range(y_size):
            for x in range(x_size):
                if i % 2 == 0:
                    if x % 2 == 0:
                        curr_color = self.RED
                    else:
                        curr_color = self.BLACK
                else:
                    if x % 2 == 0:
                        curr_color = self.BLACK
                    else:
                        curr_color = self.RED
                self.board[i].append(Square(self.SQUARE_WIDTH, self.SQUARE_HEIGHT, curr_color))
        for row in self.board:
            row_index = self.board.index(row)
            for square in row:
                square_index = row.index(square)
                square.set_coords(square_index, row_index)
                pygame.draw.rect(screen, square.color, ((screen_size_x // x_size) * square_index, (screen_size_y // y_size) * row_index, square.width, square.height))

    def get_square(self, x, y):
        return self.board[x][y]
    
    def kill_piece_at_coords(self, x, y):
        square = self.get_square(x, y)
        square.piece.kill_piece()
        square.piece.remove(square.piece)
        pygame.draw.rect(self.screen, square.color, ((self.screen_size_x // self.x_size) * square.get_x_coord(), (self.screen_size_y // self.y_size) * square.get_y_coord(), square.width, square.height))
    

class Square(Board):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.piece = []
        self.coords = []
        self.has_piece = False

    def add_piece(self, piece):
        self.has_piece = True
        self.piece.append(piece)
    
    def piece_on_square(self):
        return self.has_piece

    def get_x_coord(self):
        return self.coords[0]
    
    def get_y_coord(self):
        return self.coords[1]
    
    def get_coords(self):
        return self.coords
    
    def set_x_coord(self, x_coord):
        self.coords[0] = x_coord

    def set_y_coord(self, y_coord):
        self.coords[1] = y_coord

    def set_coords(self, x_coord, y_coord):
        self.set_x_coord(x_coord)
        self.set_y_coord(y_coord)