import pygame

class CircleShape(pygame.sprite.Sprite):
    containers = ()
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # overridable
        pass

    def update(self, dt):
        # overridable
        pass
