import pygame

import game_config
import game_config as config
from game_objects.asteroid import Asteroid
from game_dialog import GameDialog
from game_objects.space_ship import SpaceShip


class SpaceGame():
    def __init__(self):
        # Фон игры
        self.background = pygame.image.load("picture/space.jpg")
        # Скорость обновления кадров
        self.__FPS = config.FPS
        self.__clock = pygame.time.Clock()

        # Текущее значение очков игрока
        self.__current_player_score = 0

        # Создаем объект класса GameDialog
        self.__game_dialog = GameDialog()

        # TODO
        self.__first_player_score = 10

        # Вызываем метод инициализациии остальных параметров
        self.__init_game()

    def __init_game(self):
        # Создаем объект основного окна
        self.screen = pygame.display.set_mode(game_config.WINDOW_SIZE)
        pygame.display.set_caption("Космическая гонка")

        # Список всех спрайтов (графических объектов)
        self.all_sprites = pygame.sprite.Group()

        # Отдельный список астероидов
        self.asteroids = pygame.sprite.Group()

        # Объект коробля игрока
        self.spaceship = SpaceShip(self.screen)
        self.all_sprites.add(self.spaceship)

        for i in range(3):
            # Объект астероида
            asteroid = Asteroid(self.screen)
            self.all_sprites.add(asteroid)
            self.asteroids.add(asteroid)

    def __draw_scene(self):
        # отрисовка
        self.screen.blit(self.background, (0, 0))

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        # Обновляем экран
        pygame.display.update()
        pygame.display.flip()
        self.__clock.tick(self.__FPS)

    def run_game(self, game_is_run):
        # Основной цикл игры
        while game_is_run:
            # Обрабатываем событие закрытия окна
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            # Отрисовываем всё
            self.__draw_scene()
