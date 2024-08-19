import pygame

class Piece:

    def __init__(self, color, piece_type, position, spritesheet, cols, rows):
        self.color = color
        self.type = piece_type
        self.kinged = False
        self.position = position
        self.alive = True
        self.piece_name = ""
        pygame.sprite.Sprite.__init__(self)
        self.pieces = {
            "red_mini_oneway": 1,
            "red_regular_oneway": 2,
            "red_giga_oneway": 3,
            "red_mini_flipped": 4,
            "red_regular_flipped": 5,
            "red_giga_flipped": 6,
            "black_mini_oneway": 7,
            "black_regular_oneway": 8,
            "black_giga_oneway": 9,
            "black_mini_flipped": 10,
            "black_regular_flipped": 11,
            "black_giga_flipped": 12}
        self.spritesheet = pygame.image.load(spritesheet).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.cell_count = cols * rows

        self.rect = self.spritesheet.get_rect()
        w = self.cell_width = self.rect.width // self.cols
        h = self.cell_height = self.rect.height // self.rows

        self.cells = list([(i % cols * w, i // cols * h, w, h) for i in range(self.cell_count)])

    def draw(self, surface, piece_name, coords):
        self.piece_name = piece_name
        piece_index = self.pieces[piece_name]
        surface.blit(self.spritesheet, coords, self.cells[piece_index])

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_type(self, piece_type):
        self.type = piece_type

    def get_type(self):
        return self.type
    
    def is_kinged(self):
        return self.kinged

    def king_piece(self):
        self.kinged = True
    
    def set_position_x(self, x_position):
        self.position[0] = x_position
    
    def set_position_y(self, y_position):
        self.position[1] = y_position

    def get_position_x(self):
        return self.position[0]
    
    def get_position_y(self):
        return self.position[0]
    
    def set_position(self, x, y):
        self.set_position_x(x)
        self.set_position_y(y)
    
    def get_position(self):
        return [self.get_position_x(), self.get_position_y()]
    
    def is_alive(self):
        return self.alive
    
    def kill_piece(self):
        if self.is_alive():
            self.alive = False
        else:
            print("Piece already dead")
            # put some error here

    def revive_piece(self):
        if not self.is_alive:
            self.alive = True
        else:
            print("Piece is already alive")
            # put some error here
    