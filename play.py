import pygame
import abc


class Play(abc.ABC):
    screen = None
    data = None
    clock = pygame.time.Clock()
    FPS = 60

    @abc.abstractmethod
    def run(self):
        pass

