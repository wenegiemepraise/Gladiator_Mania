import pygame

class Samurai(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        # Load and scale animations
        self.attack1_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Attack1/ATTACK1_frame_{i}.png"), (178, 176)) for i in range(1, 6)]
        self.attack2_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Attack2/ATTACK2_frame_{i}.png"), (178, 176)) for i in range(1, 6)]
        self.attack3_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Attack3/ATTACK3_frame_{i}.png"), (178, 176)) for i in range(1, 11)]
        self.idle_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Idle/IDLE_frame_{i}.png"), (178, 176)) for i in range(1, 6)]
        self.run_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Run/run_frame_{i}.png"), (178, 176)) for i in range(1, 8)]
        self.jump_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Jump/jump_frame_{i}.png"), (178, 176)) for i in range(1, 4)]

        # Initial state
        self.sprites = self.idle_sprites
        self.current_sprite = 0
        self.is_animating = False
        self.facing_right = True
        self.jumping = False
        self.running = False
        self.vertical_movement = 0

        # Set initial sprite and position
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def set_attack(self, attack_number):
        """Set the animation for the selected attack."""
        self.running = False  # Stop running while attacking
        if attack_number == 1:
            self.sprites = self.attack1_sprites
        elif attack_number == 2:
            self.sprites = self.attack2_sprites
        elif attack_number == 3:
            self.sprites = self.attack3_sprites

        self.current_sprite = 0  # Reset animation
        self.is_animating = True

    def run(self, direction):
        """Start the running animation and move the Samurai."""
        if not self.jumping and not self.is_animating:  # Prevent switching to run while jumping or attacking
            self.sprites = self.run_sprites
            self.is_animating = True
        if direction == "left":
            self.running = "left"
            if self.facing_right:
                self.flip()
        elif direction == "right":
            self.running = "right"
            if not self.facing_right:
                self.flip()

    def stop_running(self):
        """Stop running."""
        self.running = False
        if not self.jumping and not self.is_animating:  # Return to idle if not jumping or attacking
            self.sprites = self.idle_sprites
            self.is_animating = False
            self.current_sprite = 0

    def jump(self):
        """Set the animation for jumping and move the Samurai vertically."""
        if not self.jumping:  # Allow jumping only if not already in the air
            self.jumping = True
            self.sprites = self.jump_sprites
            self.current_sprite = 0
            self.is_animating = True
            self.vertical_movement = -15  # Initial upward movement
            self.starting_y = self.rect.y  # Store the initial height

    def flip(self):
        """Flip the sprite horizontally."""
        self.facing_right = not self.facing_right

    def update(self):
        """Update the animation state."""
        if self.is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                if self.jumping:  # Continue jump animation until landing
                    pass
                elif self.running:
                    pass  # Keep running until stop
                self.current_sprite = 0
                self.is_animating = False

        # Loop idle or run animations
        if not self.is_animating:  # Only loop if no current animation
            self.current_sprite += 0.1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

        # Update vertical movement (jumping)
        if self.jumping:
            self.rect.y += self.vertical_movement
            self.vertical_movement += 1  # Gravity effect
            if self.rect.y >= self.starting_y:  # Land back on ground
                self.rect.y = self.starting_y
                self.jumping = False
                self.sprites = self.idle_sprites  # Switch to idle after jump

        # Update horizontal movement (running)
        if self.running == "left":
            self.rect.x -= 5
        elif self.running == "right":
            self.rect.x += 5

        # Ensure the sprite faces the correct direction
        self.image = self.sprites[int(self.current_sprite)]
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)



