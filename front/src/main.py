import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

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
        pygame.draw.line(screen, WHITE, nodes[edge[0]], nodes[edge[1]], 2)
    
    for node in nodes:
        pygame.draw.circle(screen, WHITE, node, 13)
        pygame.draw.circle(screen, node_color, node, 11)


def toggle_node_color(pos):
    node = find_clicked_node(pos)

    global node_color
    if node_color == RED:
        node_color = BLUE
    else:
        node_color = RED


def find_clicked_node(pos):
    for i, node in enumerate(nodes):
        dist = ((pos[0] - node[0])**2 + (pos[1] - node[1])**2)**0.5
        if dist < 10:
            return i
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
                    nodes.append(pos)
                else:
                    dragging = True
            elif event.button == 3:
                if connecting:
                    pos = pygame.mouse.get_pos()
                    end_node = find_clicked_node(pos)
                    if end_node is not None and end_node != start_node:
                        edges.append((start_node, end_node))
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
        nodes[selected_node] = pos

    draw_graph()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
