import pygame, sys
from pygame.locals import *
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 640
HEIGHT = 480
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Cube')

# Define the vertices of the cube
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Define the edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the camera position and rotation
camera_position = [0, 0, -5]
camera_rotation = [0, 0, 0]

# Define the projection parameters
fov = 90
near = 0.1
far = 1000
aspect_ratio = WIDTH / HEIGHT

# Define a function to multiply two matrices
# Define a function to multiply two matrices or a matrix and a scalar
def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    if cols_a != rows_b:
        raise ValueError("Number of columns in A must match number of rows in B")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result

# Define a function to project the vertices onto the screen
def project(vertex):
    x, y, z = vertex

    # Apply camera rotation
    x, y, z = rotate_x(x, y, z, camera_rotation[0])
    x, y, z = rotate_y(x, y, z, camera_rotation[1])
    x, y, z = rotate_z(x, y, z, camera_rotation[2])

    # Apply camera translation
    x += camera_position[0]
    y += camera_position[1]
    z += camera_position[2]

    # Perform perspective projection
    fov_radians = math.radians(fov)
    f = 1 / math.tan(fov_radians / 2)
    projection_matrix = [
        [aspect_ratio * f, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), -1],
        [0, 0, (2 * far * near) / (near - far), 0]
    ]
    x, y, z, w = matrix_multiply([x, y, z, 1], projection_matrix)
    x = x / w
    y = y / w

    # Scale and shift the projected point to the screen coordinates
    x = (x + 1) * WIDTH / 2
    y = (y + 1) * HEIGHT / 2

    return int(x), int(y)

# Define a function to rotate a point around the x-axis
def rotate_x(x, y, z, angle):
    radians = math.radians(angle)
    cos = math.cos(radians)
    sin = math.sin(radians)
    y = y * cos - z * sin
    z = y * sin + z * cos
    return x, y, z

# Define a function to rotate a point around the y-axis
def rotate_y(x, y, z, angle):
    radians = math.radians(angle)
    cos = math.cos(radians)
    sin = math.sin(radians)
    x = x * cos + z * sin
    z = -x * sin + z * cos
    return x, y, z

# Define a function to rotate a point around the z-axis
def rotate_z(x, y, z, angle):
    radians = math.radians(angle)
    cos = math.cos(radians)
    sin = math.sin(radians)
    x = x * cos - y * sin
    y = x * sin + y * cos
    return x, y, z

# Start the main game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    DISPLAY.fill((0, 0, 0))

    # Draw the edges of the cube
    for edge in edges:
        start = project(vertices[edge[0]])
        end = project(vertices[edge[1]])
        pygame.draw.line(DISPLAY, (255, 255, 255), start, end)

    # Rotate the camera
    camera_rotation[1] += 1

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)
