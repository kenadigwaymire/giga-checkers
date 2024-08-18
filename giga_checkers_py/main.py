'''  
 _____      _____
|     |    |     |
|     |    |     |        /|
|     |    |     |     <=====
|     |    |     |        \|
|     |    |     |
|     |    |     |
|     |    |     |
|     |    |     |
|     |    |     |
|     |    |     |
|     |    |     |
|     |    |     |
--------------------------------
'''

import pygame
import sys

startup = True
WINDOW_SIZE = (800, 800)
FPS_LIMIT = 60
RUN = True
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)

def init():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()

def main():
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()