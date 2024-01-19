import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hydrogen and Oxygen Interaction")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the clock
clock = pygame.time.Clock()

# Set up molecule positions
hydrogen_x = 350
hydrogen_y = 250
oxygen_x = 450
oxygen_y = 250

# Set up molecule velocities
hydrogen_vx = 1
hydrogen_vy = 0
oxygen_vx = -1
oxygen_vy = 0

# Set up molecule radii
hydrogen_radius = 10
oxygen_radius = 20

# Set up collision distance
collision_distance = hydrogen_radius + oxygen_radius

# Flag to track if water molecule is formed
water_formed = False

# Game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update molecule positions
    hydrogen_x += hydrogen_vx
    hydrogen_y += hydrogen_vy
    oxygen_x += oxygen_vx
    oxygen_y += oxygen_vy

    # Check for collision
    distance = math.sqrt((hydrogen_x - oxygen_x) ** 2 + (hydrogen_y - oxygen_y) ** 2)
    if distance <= collision_distance and not water_formed:
        # Perform reaction - Form water molecule
        water_formed = True
        water_x = (hydrogen_x + oxygen_x) // 2
        water_y = (hydrogen_y + oxygen_y) // 2
        pygame.draw.circle(screen, BLUE, [water_x, water_y], 15)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the molecules
    pygame.draw.circle(screen, RED, [hydrogen_x, hydrogen_y], hydrogen_radius)
    pygame.draw.circle(screen, BLUE, [oxygen_x, oxygen_y], oxygen_radius)

    # Update the screen
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()