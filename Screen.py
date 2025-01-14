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
player = Samurai(100, 300)  # Place Samurai near the center of the screen
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:  # Attack 1
                player.set_attack(1)
            elif event.key == pygame.K_x:  # Attack 2
                player.set_attack(2)
            elif event.key == pygame.K_c:  # Attack 3
                player.set_attack(3)
            elif event.key == pygame.K_SPACE:  # Jump
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:  # Stop running
                player.stop_running()

    # Check for continuous movement with held keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Run left
        player.run("left")
    elif keys[pygame.K_d]:  # Run right
        player.run("right")
    else:
        player.stop_running()  # Stop running if neither A nor D is pressed

    # Draw everything
    screen.blit(background, (0, 0))  # Draw the background first
    moving_sprites.draw(screen)      # Draw the sprite group after the background
    moving_sprites.update()          # Update the sprite animations
    pygame.display.flip()
    clock.tick(60)

