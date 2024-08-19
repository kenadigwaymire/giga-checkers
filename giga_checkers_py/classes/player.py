import pygame

class Player:
    NUM_PIECES = 12
    def __init__(self, color):
        self.pieces = []
        self.color = ""
        self.is_turn = False
    
    def add_piece(self, piece):
        self.pieces.append(piece)
    
    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def get_pieces(self):
        return self.pieces
    
    def num_pieces(self):
        return len(self.pieces)
    
    def set_player_color(self, color):
        self.color = color
    
    def get_player_color(self):
        return self.color
    
    def start_turn(self):
        if not self.is_turn: 
            self.is_turn = True
        else:
            print(f"Already {self.color} player's turn")

    def get_turn(self):
        return self.is_turn