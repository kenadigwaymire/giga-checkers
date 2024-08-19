import pygame

class Utils:
    def get_mouse_event(self):
        position = pygame.mouse.get_pos()
        return position

    def left_click_event(self):
        mouse_button = pygame.mouse.get_pressed()
        left_click = False
        if mouse_button[0]:
            left_click = True
        return left_click