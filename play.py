import pygame as pg
from abc import ABC


class Play(ABC):
    def __init__(self, data, screen, clock):
        self.screen = screen
        self.data = data
        self.clock = clock
        self.FPS = 60
