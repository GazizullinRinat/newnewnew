import sys

import pygame as pg


class Piece(pg.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pg.image.load(filename)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(350, 0))
        self.acc = 0

    def move(self, x, y):
        self.rect.topleft = (x, y)

    def check_acc(self):
        self.rect.y += self.acc
        self.acc += 1

    def render(self, screen):
        screen.blit(self.image, self.rect)


class Start:
    def __init__(self):
        self.sprites = pg.sprite.Group()
        self.flying = []
        self.y = 0

    def add(self, filename):
        self.flying.append(filename)

    def check(self):
        for i in self.flying:
            i.check_acc()
            if pg.sprite.spritecollide(i, self.sprites, False):
                i.rect.bottomleft = (i.rect.x, self.y)
                self.sprites.add(i)
                self.flying.remove(i)
                self.y = i.rect.topleft[-1]
            elif i.rect.bottomleft[-1] >= 700:
                i.rect.bottomleft = (i.rect.x, 700)
                self.sprites.add(i)
                self.flying.remove(i)
                self.y = i.rect.topleft[-1]

    def render(self, screen):
        self.sprites.draw(screen)
        for i in self.flying:
            i.render(screen)


pg.init()
screen = pg.display.set_mode((700, 700), pg.RESIZABLE)
clock = pg.time.Clock()
start = Start()
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_1:
                start.add(Piece("data_burg/bred.png"))
            elif i.key == pg.K_2:
                start.add(Piece("data_burg/beckon.png"))
            elif i.key == pg.K_3:
                start.add(Piece("data_burg/cheese.png"))
            elif i.key == pg.K_4:
                start.add(Piece("data_burg/chicken.png"))
            elif i.key == pg.K_5:
                start.add(Piece("data_burg/cow.png"))
            elif i.key == pg.K_6:
                start.add(Piece("data_burg/egg.png"))
            elif i.key == pg.K_7:
                start.add(Piece("data_burg/bred_end.png"))
            elif i.key == pg.K_0:
                sys.exit()
    screen.fill("#ffffff")
    start.render(screen)
    start.check()
    pg.display.update()
    clock.tick(60)
