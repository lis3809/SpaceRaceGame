import pygame as pg

import game_config
import game_config as config
from data_base.db_manager import DataBase
from game_objects.asteroid import Asteroid
from game_dialog import GameDialog
from game_objects.space_ship import SpaceShip


def load_img(name):
    img = pg.image.load(name)
    # img = img.convert()
    # colorkey = img.get_at((0, 0))
    # img.set_colorkey(colorkey)
    img = pg.transform.scale(img, config.WINDOW_SIZE)
    return img


class SpaceGame():
    """Базовый класс для запуска игры"""

    def __init__(self):
        # Фон игры
        self.background = load_img("picture/space.jpg")
        # Скорость обновления кадров
        self.__FPS = config.FPS
        self.__clock = pg.time.Clock()

        # Создаем объект класса DBManager, отвечающий за работу с базой данных
        self.__db_manger = DataBase()
        self.table_name = 'scores'
        self.__db_manger.create_table(self.table_name)

        # Создаем объект класса GameDialog
        self.__game_dialog = GameDialog()

        # Запрашиваем имя игрока
        self.__player_name = self.__game_dialog.show_dialog_login()
        print(self.__player_name)

        # Сохраняем игрока в базу данных
        # TODO
        self.__db_manger.insert(self.table_name, self.__player_name, 0)

        # Вызываем метод инициализациии остальных параметров
        self.__init_game()

    def __init_game(self):

        # Текущее значение очков игрока
        self.__current_player_score = 0

        # Создаем объект основного окна
        self.screen = pg.display.set_mode(game_config.WINDOW_SIZE)
        pg.display.set_caption("Космическая гонка")

        # Список всех спрайтов (графических объектов)
        self.all_sprites = pg.sprite.Group()

        # Отдельный список астероидов
        self.asteroids = pg.sprite.Group()

        # В начале игры три астероида
        self.count_asteroid = 3

        # Объект коробля игрока
        self.spaceship = SpaceShip(self.screen)
        self.all_sprites.add(self.spaceship)

        # Создаем астероиды
        for i in range(self.count_asteroid):
            # Объект астероида
            asteroid = Asteroid(self.screen)
            self.all_sprites.add(asteroid)
            self.asteroids.add(asteroid)

    def check_collision(self):
        # Проверяем столкновение игрока с астероидом
        list_colid = pg.sprite.spritecollide(self.spaceship, self.asteroids, False)
        if len(list_colid) > 0:
            self.__db_manger.update_player_data(self.table_name, self.__player_name, self.__current_player_score)
            if self.__game_dialog.show_dialog_game_over():
                self.__init_game()
            else:
                exit()

        # Если астероид вылетел за край экрана
        for asteroid in self.asteroids:
            if asteroid.rect.y > self.screen.get_height():
                self.__current_player_score += 1
                self.asteroids.remove(asteroid)
                self.all_sprites.remove(asteroid)

                # Увеличваем количество астероидов
                if self.__current_player_score % 3 == 0:
                    self.count_asteroid += 1

        # Если количество астероидов уменьшилось
        if len(self.asteroids) < self.count_asteroid:
            # Объект астероида
            newAsteroid = Asteroid(self.screen)
            self.all_sprites.add(newAsteroid)
            self.asteroids.add(newAsteroid)

    def __draw_score(self):
        # Надпись с именем игрока
        # Шрифт и размер текста
        font = pg.font.Font(None, 28)
        text_name = font.render(f"Игрок: {self.__player_name}", True, 'white')
        text_name_rect = text_name.get_rect(topleft=(10, 30))
        self.screen.blit(text_name, text_name_rect)

        # Надпись с текущими очками игрока
        text_score = font.render(f"Очки: {self.__current_player_score}", True, 'white')
        text_score_rect = text_score.get_rect(topleft=(10, 50))
        self.screen.blit(text_score, text_score_rect)

    def __draw_scene(self):
        # отрисовка
        self.screen.blit(self.background, (0, 0))

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        # Отрисовываем очки
        self.__draw_score()

        # Проверяем столкновения
        self.check_collision()

        # Обновляем экран
        pg.display.update()
        pg.display.flip()
        self.__clock.tick(self.__FPS)

    def run_game(self, game_is_run):
        # Основной цикл игры
        while game_is_run:
            # Обрабатываем событие закрытия окна
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            # Отрисовываем всё
            self.__draw_scene()
