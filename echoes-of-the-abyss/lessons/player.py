import pygame


class Player:
    def __init__(self, x, y, size, speed, image_path):
        # Keep floating-point movement separate from the integer collision Rect.
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.speed = speed
        self.rect = pygame.Rect(x, y, size, size)

        # Keep image transparency and prepare the pixel art once for drawing.
        loaded_image = pygame.image.load(image_path).convert_alpha()
        self.sprite = pygame.transform.scale(loaded_image, (size, size))

    def update(self, keys, dt, screen_width, screen_height, walls):
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_RIGHT]:
            direction.x += 1
        if keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_DOWN]:
            direction.y += 1
        if keys[pygame.K_UP]:
            direction.y -= 1

        if direction.length() > 0:
            direction = direction.normalize()

        # Resolve each axis on its own, preserving the existing wall behavior.
        previous_x = self.position.x
        self.position.x += direction.x * self.speed * dt
        self.rect.topleft = (round(self.position.x), round(self.position.y))

        for wall in walls:
            if self.rect.colliderect(wall):
                self.position.x = previous_x
                self.rect.topleft = (round(self.position.x), round(self.position.y))
                break

        previous_y = self.position.y
        self.position.y += direction.y * self.speed * dt
        self.rect.topleft = (round(self.position.x), round(self.position.y))

        for wall in walls:
            if self.rect.colliderect(wall):
                self.position.y = previous_y
                self.rect.topleft = (round(self.position.x), round(self.position.y))
                break

        # Clamp the top-left coordinate so the whole player remains visible.
        self.position.x = max(0, min(screen_width - self.size, self.position.x))
        self.position.y = max(0, min(screen_height - self.size, self.position.y))
        self.rect.topleft = (round(self.position.x), round(self.position.y))

    def draw(self, surface):
        # The sprite shares the collision Rect's position; alpha reveals
        # the world.
        surface.blit(self.sprite, self.rect.topleft)