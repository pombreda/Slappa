from config import *
from point import *


class Image(object):
    def __init__(self, game, x, y, key, scale=Point(1, 1)):
        self.game = game
        self.__width = 0
        self.__height = 0
        self.__smoothed = True
        if key != '':
            self.__image = game.load.images[key]
            new_scale = Point(scale.x, scale.y)
            new_scale.multiply(game.scale.scale)
            self.__width = int(self.__image.get_width() * new_scale.x)
            self.__height = int(self.__image.get_height() * new_scale.y)
            self.__set_scale()
        else:
            self.__image = None
            self.image = None
        self.x = x
        self.y = y
        self.anchor = Point(0.5, 0.5)
        self.alpha = 1.0
        self.visible = True

    def __set_scale(self):
        if self.__image:
            if self.smoothed:
                self.image = pygame.transform.smoothscale(
                    self.__image, (self.__width, self.__height))
            else:
                self.image = pygame.transform.scale(
                    self.__image, (self.__width, self.__height))
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = int(value * self.game.scale.scale.x)
        self.__set_scale()
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = int(value * self.game.scale.scale.y)
        self.__set_scale()
    @property
    def smoothed(self):
        return self.__smoothed
    @smoothed.setter
    def smoothed(self, value):
        self.__smoothed = value
        self.__set_scale()

    def set_scale(self, scale):
        self.__width = int(self.__width * scale.x)
        self.__height = int(self.__height * scale.y)
        self.__set_scale()


    def update(self, time):
        pass

    def draw(self, surface):
        if not self.visible:
            return
        if self.image is not None:
            self.image.set_alpha(int(self.alpha * 255))
            point = Point(self.x, self.y)
            point.multiply(self.game.scale.scale)
            point.subtract(Point(self.width * self.anchor.x,
                                 self.height * self.anchor.y))
            surface.blit(self.image, (int(point.x), int(point.y)))
        if self.game.config.DEBUG_DRAW_SPRITE_ANCHOR:
            point = Point(self.x, self.y)
            point.multiply(self.game.scale.scale)
            pygame.draw.circle(surface,
                               (0, 0, 255),
                               (int(point.x), int(point.y)),
                               3,
                               0)

    def exists(self):
        return True