"""
An implementation of the training interface using pygame.
"""

import pygame
from view import View, ViewSetup
from typing import Tuple

# TODO: maybe we should have an Enum for different preset views,
# and an Enum for different view types?
DEFAULT_SETUP = ViewSetup(
    window_shape=(500, 500),
    targets=[(0, 250), (250, 0), (250, 490), (490, 250)],
    target_shape=(10, 10),
    cursor_pos=(250, 250),
    cursor_radius=5
)


class Target(pygame.sprite.Sprite):
    """
    Represents the target the user is trying to reach with their cursor
    """

    def __init__(self, pos: Tuple[int, int], size: Tuple[int, int]):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = pos


class Cursor(pygame.sprite.Sprite):
    """
    Represents the moving cursor
    """

    def __init__(self, start_pos: Tuple[int, int], size: int):
        pygame.sprite.Sprite.__init__(self)
        self.start_pos = start_pos
        self.curr_pos = start_pos
        self.surface = pygame.Surface((size * 2, size * 2))
        self.surface.fill((1, 1, 1))
        self.surface.set_colorkey((1, 1, 1))
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = start_pos

        pygame.draw.circle(self.surface, (0, 0, 0), (size, size), size, size)

    def reinit(self):
        self.move(self.start_pos)

    def move(self, pos: Tuple[int, int]):
        self.rect.x, self.rect.y = pos

class PyGameView(View):
    """
    Implements the View interface using pygame.
    """

    def __init__(self):
        pygame.init()

    def initialize(self, setup: ViewSetup):
        # Initialize screen
        self.screen = pygame.display.set_mode(setup.window_shape)

        # Fill background
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250, 250, 250))

        # Instantiate cursor and targets
        self.cursor = Cursor(setup.cursor_pos, setup.cursor_radius)
        self.targets = []
        for target_coords in setup.targets:
            self.targets.append(Target(target_coords, setup.target_shape))

        # Add everything to the screen
        self.__blit()

    def __blit(self):
        """
        Helper method to "blit" everything to the screen so that it all shows up.
        """
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.cursor.surface, self.cursor.rect)
        for target in self.targets:
            self.screen.blit(target.surface, target.rect)
        pygame.display.flip()

    def move(self, x: int, y: int):
        self.cursor.move((x, y))
        self.__blit()

    def clear(self):
        # Cover everything with the background.
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def restart(self):
        self.cursor.reinit()
        self.__blit()

    def update(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
