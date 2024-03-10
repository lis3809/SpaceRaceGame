# Класс машины игрока
import pygame
import game_config


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("picture/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = game_config.WINDOW_SIZE[1] - 10
        self.rect.centerx = game_config.WINDOW_SIZE[0] // 2
        self.speedx = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -8
        elif keys[pygame.K_RIGHT]:
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
