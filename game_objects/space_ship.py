# Класс объекта игрока
import pygame as pg
import game_config


def load_img(name):
    img = pg.image.load(name)
    #img = img.convert()
    #colorkey = img.get_at((0, 0))
    #img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (100, 100))
    return img


class SpaceShip(pg.sprite.Sprite):
    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_img("picture/spaceship.png")
        self.rect = self.image.get_rect()


        self.rect.bottom = game_config.WINDOW_SIZE[1] - 10
        self.rect.centerx = game_config.WINDOW_SIZE[0] // 2
        self.speedx = 0

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.speedx = -8
        elif keys[pg.K_RIGHT]:
            self.speedx = 8
        else:
            self.speedx = 0

        self.rect.x += self.speedx
        if self.rect.right > game_config.WINDOW_SIZE[0]:
            self.rect.right = game_config.WINDOW_SIZE[0]
        if self.rect.left < 0:
            self.rect.left = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)
