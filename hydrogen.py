import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Hydrogen Atom Simulation")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main program loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Draw the nucleus
    pygame.draw.circle(screen, RED, [350, 250], 10)

    # Draw the electron
    angle = pygame.time.get_ticks() / 50
    x = int(350 + 100 * math.cos(angle))
    y = int(250 + 100 * math.sin(angle))
    pygame.draw.circle(screen, BLUE, [x, y], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
