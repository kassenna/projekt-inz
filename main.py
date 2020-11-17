import pygame as pg
from data import Data
from product import Product
from screen import Screen
from menu import Menu
from level import Level
def main():
    data = Data()
    data.insert_product_to_receipe(0)
    data.display_receipes()
    clock = pg.time.Clock()
    window = pg.display.set_mode(Screen.get_size())
    menu = Menu(data, window, clock)
    menu.set_levels()
    menu.run()

if __name__ == "__main__":
    main()

