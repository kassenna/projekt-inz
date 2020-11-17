import pygame
import pygame_menu


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game(label):
    for i in label:
        i.set_background_color((0,10,100))
    # Do the job here !
    pass


pygame.init()
surface = pygame.display.set_mode((600, 400))
theme = pygame_menu.themes.Theme(background_color=(200, 200, 0, 200),
                                 title_background_color=(250, 250, 0),
                                 title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE,
                                 widget_font=pygame_menu.font.FONT_OPEN_SANS_ITALIC,
                                 title_font_size=25,
                                 title_shadow = False,
                                 widget_font_size = 20)
menu = pygame_menu.Menu(200, 200, 'Przepis',
                        theme=theme, menu_position=(10, 10))
label = []
label.append(menu.add_label('0'))
label.append(menu.add_label('1'))
label.append(menu.add_label('2'))
label.append(menu.add_label('3'))
label.append(menu.add_label('4'))

menu.add_button('Play', start_the_game, label)

menu.mainloop(surface)
