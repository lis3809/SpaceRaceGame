# Класс астероида
import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("picture/asteroid.png")
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
