import pygame
import sys
from front.src.colors import *
from front.src.node import Node
from front.src.edge import Edge
from back.src.main import Graph

pygame.init()

WIDTH, HEIGHT = 800, 600

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Redes Críticas")

# Graph
nodes = []
edges = []
lis_edges = []

connecting = False
start_node = None

node_color = BLUE


def draw_graph():
    screen.fill(BLACK) 
    for edge in edges:
        edge.draw(screen)
    for node in nodes:
        node.draw(screen)


def critical_node(color, ids):
    global nodes
    for id in ids:
        nodes[id-1].toggle_color(color)


def find_clicked_node(pos):
    for node in nodes:
        dist = ((pos[0] - node.pos[0])**2 + (pos[1] - node.pos[1])**2)**0.5
        if dist < 10:
            return node
    return None


# Main loop
class Interface:
    def __init__(self) -> None:
        self.running = True
        self.clock = pygame.time.Clock()
        self.dragging = False
        self.selected_node = None
    
    def run(self):
        global connecting, start_node
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        self.selected_node = find_clicked_node(pos)
                        if self.selected_node is None:
                            new_node = Node(len(nodes)+1, pos)
                            nodes.append(new_node)
                        else:
                            self.dragging = True
                    elif event.button == 3:
                        global start_node
                        if connecting:
                            pos = pygame.mouse.get_pos()
                            end_node = find_clicked_node(pos)
                            if end_node is not None and end_node != start_node:
                                edge = Edge(start_node, end_node)
                                lis_edges.append([nodes.index(start_node)+1, nodes.index(end_node)+1])
                                edges.append(edge)
                            connecting = False
                        else:
                            pos = pygame.mouse.get_pos()
                            start_node = find_clicked_node(pos)
                            if start_node is not None:
                                connecting = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.dragging = False
                        self.selected_node = None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        grph = Graph(nodes, lis_edges)
                        color, criticos = grph.run()
                        critical_node(color, criticos)
            if self.dragging and self.selected_node is not None:
                pos = pygame.mouse.get_pos()
                self.selected_node.pos = pos

            draw_graph()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Interface().run()
