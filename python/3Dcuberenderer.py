import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Circle Collision Example")

# Create a list of circles
circles = []
for i in range(10):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    r = random.randint(20, 50)
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    circles.append({'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy})

# Define a function to check for circle collisions
def circle_collision(circle1, circle2):
    distance = ((circle1['x'] - circle2['x']) ** 2 + (circle1['y'] - circle2['y']) ** 2) ** 0.5
    if distance <= circle1['r'] + circle2['r']:
        return True
    else:
        return False

# Define the main game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update the positions of the circles
    for circle in circles:
        circle['x'] += circle['vx']
        circle['y'] += circle['vy']

        # Check for collisions with the edges of the screen
        if circle['x'] - circle['r'] < 0 or circle['x'] + circle['r'] > SCREEN_WIDTH:
            circle['vx'] = -circle['vx']
        if circle['y'] - circle['r'] < 0 or circle['y'] + circle['r'] > SCREEN_HEIGHT:
            circle['vy'] = -circle['vy']

        # Check for collisions with other circles
        for other_circle in circles:
            if circle != other_circle and circle_collision(circle, other_circle):
                circle['vx'] = -circle['vx']
                circle['vy'] = -circle['vy']
                other_circle['vx'] = -other_circle['vx']
                other_circle['vy'] = -other_circle['vy']

        # Draw the circle
        pygame.draw.circle(screen, BLACK, (int(circle['x']), int(circle['y'])), circle['r'])

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
