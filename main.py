import pygame as pg
from pygame.locals import *
import random

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Fruit Catcher")
        self.scn_width = 1280
        self.scn_height = 720
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.bgpic = pg.image.load("img/bg01.jpg")
        self.bgpic = pg.transform.scale(self.bgpic, (self.scn_width, self.scn_height))
        self.screen = pg.display.set_mode((self.scn_width, self.scn_height))
        self.fruits = []
        self.running = True
        self.start_t = pg.time.get_ticks()
        self.end_t = pg.time.get_ticks()
        self.fruits_list = ["apple", "banana", "cherry", "grapes", "green_apple", "lemon",
                            "mango", "orange", "pear", "strawberry", "watermelon"]
        self.basket = Basket(self.scn_width, self.scn_height)

    def main(self):
        while self.running:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
            keys = pg.key.get_pressed()
            self.basket.move(keys)
            self.screen.blit(self.bgpic, (0, 0))
            self.end_t = pg.time.get_ticks()
            self.screen.blit(self.basket.img, self.basket.img_rect)
            if self.end_t - self.start_t > 2000:
                self.start_t = self.end_t
                fname = random.choice(self.fruits_list)
                f = Fruit(fname)
                x = random.randint(0, self.scn_width - f.img_rect.width)
                f.init_loc(x)
                self.fruits.append(f)
            for f in self.fruits:
                f.drop()
                self.screen.blit(f.img, f.img_rect)
            pg.display.flip()
            self.clock.tick(self.FPS)


class Fruit:
    def __init__(self, kind):
        self.kind = kind
        self.x_speed = 0
        self.y_speed = 3
        self.img = pg.image.load("img/" + kind + ".png")
        self.img = pg.transform.scale(self.img, (int(self.img.get_width()/2), int(self.img.get_height()/2)))
        self.img_rect = self.img.get_rect()

    def init_loc(self, x):
        self.img_rect.topleft = (x, 0)

    def drop(self):
        self.img_rect.move_ip(self.x_speed, self.y_speed)


class Basket:
    def __init__(self, scn_width, scn_height):
        self.x_speed = 9
        self.img = pg.image.load("img/basket.png")
        self.img = pg.transform.scale(self.img, (int(self.img.get_width()/2), int(self.img.get_height()/2)))
        self.img_rect = self.img.get_rect()
        self.img_rect.bottom = scn_height
        self.img_rect.centerx = scn_width / 2

    def move(self, keys):
        if not (keys[K_LEFT] and keys[K_RIGHT]):
            if keys[K_LEFT]:
                self.img_rect.move_ip(-self.x_speed, 0)
            elif keys[K_RIGHT]:
                self.img_rect.move_ip(self.x_speed, 0)


if __name__ == "__main__":
    game = Game()
    game.main()
