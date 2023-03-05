import pygame
import math

# Initialize Pygame
pygame.init()

# Set the window size and caption
size = (800, 600)
caption = "3D Cube Renderer"
pygame.display.set_caption(caption)
color = (255, 0, 0)
 
# Changing surface color

# Set up the screen
screen = pygame.display.set_mode(size)
screen.fill(color)
# Define the cube's vertices
vertices = [(100, 100, 100), (100, -100, 100), (-100, -100, 100), (-100, 100, 100), (100, 100, -100), (100, -100, -100), (-100, -100, -100), (-100, 100, -100)]

# Define the edges between vertices
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

# Define the cube's rotation
angle_x = 0
angle_y = 0
angle_z = 0

# Define the function to rotate the vertices
def rotate_vertex(vertex):
    # Rotate around the X-axis
    new_y = vertex[1] * math.cos(angle_x) - vertex[2] * math.sin(angle_x)
    new_z = vertex[1] * math.sin(angle_x) + vertex[2] * math.cos(angle_x)
    vertex = (vertex[0], new_y, new_z)
    # Rotate around the Y-axis
    new_x = vertex[0] * math.cos(angle_y) - vertex[2] * math.sin(angle_y)
    new_z = vertex[0] * math.sin(angle_y) + vertex[2] * math.cos(angle_y)
    vertex = (new_x, vertex[1], new_z)
    # Rotate around the Z-axis
    new_x = vertex[0] * math.cos(angle_z) - vertex[1] * math.sin(angle_z)
    new_y = vertex[0] * math.sin(angle_z) + vertex[1] * math.cos(angle_z)
    vertex = (new_x, new_y, vertex[2])
    return vertex

# Define the function to draw the cube
def draw_cube():
    # Clear the screen
    screen.fill((255, 255, 255))
    # Draw each edge of the cube
    for edge in edges:
        vertex_1 = vertices[edge[0]]
        vertex_2 = vertices[edge[1]]
        vertex_1 = rotate_vertex(vertex_1)
        vertex_2 = rotate_vertex(vertex_2)
        # Project the vertices onto the screen
        x1 = vertex_1[0] + size[0] / 2
        y1 = vertex_1[1] + size[1] / 2
        x2 = vertex_2[0] + size[0] / 2
        y2 = vertex_2[1] + size[1] / 2
        # Draw the line
        pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)
    # Update the display
    pygame.display.flip()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Handle key presses
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_w:
                    angle_x += 0.1
                elif event.key == pygame.K_s:
                    angle_x -= 0.1
                elif event.key == pygame.K_a:
                    angle_y += 0.1
                elif event.key == pygame.K_d:
                    angle_y -= 0.1
                elif event.key == pygame.K_q:
                    angle_z += 0.1
                elif event.key == pygame.K_e:
                    angle_z -= 0.1

    # Draw the cube
    draw_cube()

pygame.quit()
