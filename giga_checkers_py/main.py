import pygame
import sys

WINDOW_SIZE = (800, 800)
ROWS, COLS = 8, 8
SQ_SIZE = WINDOW_SIZE[0] // COLS
FPS_LIMIT = 60

def main():
    startup = True
    run = True
    while run:
        if startup == True:
            pygame.init()
            screen = pygame.display.set_mode(WINDOW_SIZE)
            clock = pygame.time.Clock()
            startup = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill("purple")
        pygame.display.flip()
        clock.tick(FPS_LIMIT)
    pygame.quit()

main()
'''
def create_board(window)
    window.fill(BLACK)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2)
            pygame.draw.rect(window, WHITE, (row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
'''