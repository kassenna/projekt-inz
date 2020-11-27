import pygame
import pygame as pg
from data.data import Data
from other.screen import Screen
from menu import Menu
import pygameAssets
import pygame_menu


def select_level(data, window):
    clock = pg.time.Clock()
    Menu(data, window, clock)


def main():
    data = Data()

    # data.display_recipes()
    pygame.init()
    window = pg.display.set_mode(Screen.get_size())
    pygameAssets.TextBox.setScreen(window)
    menu = pygame_menu.Menu(Screen.get_size()[1], Screen.get_size()[0], 'menu', theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button('Graj', select_level, data, window)
    menu.mainloop(window)

    # menu.add_button('wyjscie', 'exit' )
    #


if __name__ == "__main__":
    main()
