# Класс астероида
import pygame as pg
import random


def load_img(name):
    img = pg.image.load(name)
    #img = img.convert()
    #colorkey = img.get_at((0, 0))
    #img.set_colorkey(colorkey)
    img = pg.transform.scale(img, (50, 111))
    return img

class Asteroid(pg.sprite.Sprite):
    def __init__(self, screen):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = load_img("picture/asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.bottom = 0
        self.speed = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.screen.get_height():
            self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
            self.rect.bottom = 0
            self.speed = random.randint(3, 8)

    def draw(self):
        self.screen.blit(self.image, self.rect)
