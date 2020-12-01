import pygame
import pygame as pg
from data.data import Data
from display_objects.object_display import Object_display
from other.screen import Screen
from menu import Menu
import pygameAssets
import pygame_menu
from play import Play


def select_level():

    Menu()


def main():
    pygame.init()
    window = pg.display.set_mode(Screen.get_size())
    data = Data()
    Object_display.screen = window
    Object_display.data = data
    Play.clock = pg.time.Clock()
    Play.data = data
    Play.screen = window

    pygameAssets.TextBox.setScreen(window)
    menu = pygame_menu.Menu(Screen.get_size()[1], Screen.get_size()[0], 'menu', theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button('Graj', select_level)
    menu.mainloop(window)

    # menu.add_button('wyjscie', 'exit' )
    #


if __name__ == "__main__":
    main()
