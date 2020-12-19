import pygame
import pygame as pg
from tinydb import TinyDB
from data import Data
from uml.object_display import Object_display
from screen import Screen
from menu import Menu
import pygameAssets
import pygame_menu
from play import Play
from product import Product


def select_level(window):
    data = Data()
    Object_display.screen = window
    Object_display.data = data
    Play.data = data
    Play.screen = window
    Product.data = data
    Play.clock = pg.time.Clock()
    Menu()


def clear(window, path='data/db.json'):
    db = TinyDB(path)
    r = db.table('Recipes')
    r.update({'completed': False})
    select_level(window)


def main():
    pygame.init()
    window = pg.display.set_mode(Screen.get_size())
    print(type(window))
    pygameAssets.TextBox.setScreen(window)
    menu = pygame_menu.Menu(Screen.get_size()[1], Screen.get_size()[0], 'menu', theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button('Graj', select_level, window)
    menu.add_button('Od nowa', clear, window)
    menu.mainloop(window)

if __name__ == "__main__":
    main()

