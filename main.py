from constants import *
import pygame

from player import Player

def main():
    if not pygame.get_init():
        pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        pygame.Surface.fill(screen, (0,0,0))
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60.0) / 1000


if __name__ == "__main__":
    main()
