import pygame
import sys
from colors import *
from node import Node
from edge import Edge

pygame.init()

WIDTH, HEIGHT = 800, 600

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Redes Críticas")

# Graph
nodes = []
edges = []

connecting = False
start_node = None

node_color = BLUE


def draw_graph():
    screen.fill(BLACK) 
    for edge in edges:
        edge.draw(screen)
    
    for node in nodes:
        node.draw(screen)


def toggle_node_color():

    global node_color
    if node_color == RED:
        node_color = BLUE
    else:
        node_color = RED


def find_clicked_node(pos):
    for node in nodes:
        dist = ((pos[0] - node.pos[0])**2 + (pos[1] - node.pos[1])**2)**0.5
        if dist < 10:
            return node
    return None


# Main loop
running = True
clock = pygame.time.Clock()
dragging = False
selected_node = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                selected_node = find_clicked_node(pos)
                if selected_node is None:
                    new_node = Node(len(nodes), pos)  # Cria um novo objeto Node
                    nodes.append(new_node)  # Adiciona o novo objeto Node à lista
                else:
                    dragging = True
            elif event.button == 3:
                if connecting:
                    pos = pygame.mouse.get_pos()
                    end_node = find_clicked_node(pos)
                    if end_node is not None and end_node != start_node:
                        edge = Edge(start_node, end_node)
                        edges.append(edge)
                    connecting = False
                else:
                    pos = pygame.mouse.get_pos()
                    start_node = find_clicked_node(pos)
                    if start_node is not None:
                        connecting = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                selected_node = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_node_color()

    if dragging and selected_node is not None:
        pos = pygame.mouse.get_pos()
        selected_node.pos = pos

    draw_graph()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
