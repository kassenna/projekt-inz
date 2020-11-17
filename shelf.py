from display_objects.shelf_image import Shelf_image
class Shelf:
    def __init__(self, id, x, y, xmax, ymax, screen_width, screen_height, ):
        self.id = id
        self.image = Shelf_image(x, y, xmax, ymax, screen_width, screen_height, None)

    def draw(self, screen= None):
        self.image.draw()

    def resize(self, w, h):
        self.image.resize(w, h)