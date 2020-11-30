import pygame as pg
import abc


class Play(abc.ABC):
    def __init__(self, data, screen, clock):
        self.screen = screen
        self.data = data
        self.clock = clock
        self.FPS = 60

    @abc.abstractmethod
    def run(self):
        pass

