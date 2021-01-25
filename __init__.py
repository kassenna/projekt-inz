import pygame_menu
import pygame
import pygameAssets
from tinydb import TinyDB
from data import Data
from object_display import Object_display
from screen import Screen
from menu import Menu
from play import Play
from product import Product


def select_level(window):
    data = Data()
    Object_display.screen = window
    Object_display.data = data
    Play.data = data
    Play.screen = window
    Product.data = data
    Play.clock = pygame.time.Clock()
    Menu()


def clear(window, path='data/db.json'):
    db = TinyDB(path)
    r = db.table('Recipes')
    r.update({'completed': False})
    select_level(window)

def close():
    exit(0)

def main():
    pygame.init()
    icon = pygame.image.load('images/jabłko.png')
    pygame.display.set_icon(icon)

    window = pygame.display.set_mode(Screen.get_size())
    pygame.display.set_caption('Przepis na matematykę')
    pygameAssets.TextBox.setScreen(window)
    theme = pygame_menu.themes.THEME_BLUE

    menu = pygame_menu.Menu(Screen.get_size()[1], Screen.get_size()[0], 'menu', theme=theme, onclose=close, )
    menu.add_button('Graj', select_level, window)
    menu.add_button('Od nowa', clear, window)
    menu.mainloop(window)

if __name__ == "__main__":
    main()

