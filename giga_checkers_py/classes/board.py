#Board should have a list of pieces which will be piece objects
import pygame
from classes.piece import *

class Board:
    RED = (255, 0, 0)
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)
    GOLD = (212, 175, 55)
    SQUARE_DIM = 100

    def __init__(self, screen, screen_size_x, screen_size_y, x_size, y_size):
        self.board = []
        self.screen = None
        self.x_size = 0
        self.y_size = 0
        self.screen_size_x = 0
        self.screen_size_y = 0
    
    def draw_board(self):
        self.screen = self.screen
        for i in range(self.y_size):
            for x in range(self.x_size):
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
                self.board[i].append(Square(self.SQUARE_DIM, self.SQUARE_DIM, curr_color))
        for row in self.board:
            row_index = self.board.index(row)
            for square in row:
                square_index = row.index(square)
                square.set_coords(((self.screen_size_x // self.x_size) * square_index), ((self.screen_size_y // self.y_size) * row_index))
                pygame.draw.rect(self.screen, square.color, ((self.screen_size_x // self.x_size) * square_index, (self.screen_size_y // self.y_size) * row_index, square.width, square.height))

    def get_square(self, x, y):
        return self.board[x][y]
    
    def kill_piece_at_coords(self, x, y):
        square = self.get_square(x, y)
        square.piece.kill_piece()
        square.piece.remove(square.piece)
        pygame.draw.rect(self.screen, square.color, ((self.screen_size_x // self.x_size) * square.get_x_coord(), (self.screen_size_y // self.y_size) * square.get_y_coord(), square.width, square.height))
    

class Square(Board):
    def __init__(self, width, height, color, board):
        self.width = width
        self.height = height
        self.color = color
        self.board = board
        self.piece = []
        self.coords = []
        self.has_piece = False

    def add_piece(self, piece):
        self.has_piece = True
        self.piece.append(piece)
        dest = self.get_centerpoint()
        piece.draw(self.board.screen, (dest[0], dest[1]))
    
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

    def get_centerpoint(self):
        return [self.get_x_coord + (self.width // 2), self.get_y_coord + (self.height // 2)]