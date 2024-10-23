import pygame

class CircleShape(pygame.sprite.Sprite):
    containers = ()
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers) # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # will override
        pass

    def update(self, dt):
        # will override
        pass

    def collision(self, shape):
        if pygame.math.Vector2.distance_to(self.position, shape.position) <= self.radius + shape.radius:
            return True
        return False
