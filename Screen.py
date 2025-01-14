import pygame, sys
from Warriors import Samurai  # Assuming the Samurai class is in samurai.py

# General setup
pygame.init()
clock = pygame.time.Clock()

# Screen setup
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gladiator Mania")

# Load and scale the background image
background = pygame.image.load("images/gladiator_mania_screen.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Creating the Samurai sprite
moving_sprites = pygame.sprite.Group()
player = Samurai(100, 400)  # Place Samurai near the center of the screen
player.image = pygame.transform.scale(player.image, (player.image.get_width() * 3, player.image.get_height() * 3))  # Scale the sprite 3x
moving_sprites.add(player)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:  # Attack 1
                player.set_attack(1)
            elif event.key == pygame.K_x:  # Attack 2
                player.set_attack(2)
            elif event.key == pygame.K_c:  # Attack 3
                player.set_attack(3)

    # Draw everything
    screen.blit(background, (0, 0))  # Draw the background first
    moving_sprites.draw(screen)      # Draw the sprite group after the background
    moving_sprites.update()          # Update the sprite animations
    pygame.display.flip()
    clock.tick(60)
