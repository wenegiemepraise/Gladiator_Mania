import pygame

class Samurai(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        # Load and scale the animation frames (3x bigger)
        self.attack1_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Attack1/ATTACK1_frame_{i}.png"), (200, 200)) for i in range(1, 6)]
        self.attack2_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Attack2/ATTACK2_frame_{i}.png"), (200, 200)) for i in range(1, 6)]
        self.attack3_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Attack3/ATTACK3_frame_{i}.png"), (200, 200)) for i in range(1, 11)]
        self.idle_sprites = [pygame.transform.scale(pygame.image.load(f"images/Samurai/Idle/IDLE_frame_{i}.png"), (200, 200)) for i in range(1, 6)]

        # Initial state: Idle
        self.sprites = self.idle_sprites
        self.current_sprite = 0
        self.is_animating = False

        # Set initial sprite and position
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def set_attack(self, attack_number):
        """Set the animation for the selected attack."""
        if attack_number == 1:
            self.sprites = self.attack1_sprites
        elif attack_number == 2:
            self.sprites = self.attack2_sprites
        elif attack_number == 3:
            self.sprites = self.attack3_sprites

        self.current_sprite = 0  # Reset animation
        self.is_animating = True

    def update(self):
        """Update the animation state."""
        if self.is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.sprites = self.idle_sprites  # Switch back to idle
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]
        else:
            # Loop idle animation
            self.current_sprite += 0.1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
