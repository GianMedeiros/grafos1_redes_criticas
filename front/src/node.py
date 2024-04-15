import pygame
from colors import *


class Node:
    def __init__(self, id, pos):
        self.color = BLUE
        self.id = id
        self.pos = pos

    def critical_node(self):
        self.color = RED
    
    def non_critical_node(self):
        self.color = BLUE

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, 13)
        pygame.draw.circle(screen, self.color, self.pos, 11)


