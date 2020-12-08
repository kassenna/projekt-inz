import pygame
import pygame as pg
from data.data import Data
from abstract_class.object_display import Object_display
from other.screen import Screen
from menu import Menu
import pygameAssets
import pygame_menu
from abstract_class.play import Play
from shop.product import Product


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
    Product.data = data

    pygameAssets.TextBox.setScreen(window)
    menu = pygame_menu.Menu(Screen.get_size()[1], Screen.get_size()[0], 'menu', theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button('Graj', select_level)
    menu.mainloop(window)

    # menu.add_button('wyjscie', 'exit' )
    #


if __name__ == "__main__":
    main()
