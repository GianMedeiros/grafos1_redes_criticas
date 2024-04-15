from node import Node
from colors import WHITE
import pygame

class Edge:
    def __init__(
            self,
            start_node: Node,
            end_node: Node
            ) -> None:
        self.start = start_node
        self.end = end_node
    
    def draw(self, screen):
        pygame.draw.line(screen, WHITE, self.start.pos, self.end.pos, 2)