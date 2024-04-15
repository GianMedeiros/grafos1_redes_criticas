import pygame
from front.src.colors import *


class Node:
    def __init__(self, id, pos):
        self.color = BLUE
        self.id = id
        self.pos = pos

    def toggle_color(self):
        if self.color == BLUE:
            self.color = RED
        else:
            self.color = BLUE

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, 13)
        pygame.draw.circle(screen, self.color, self.pos, 11)


