import pygame as pg
from src.engine.settings import *
from src.entities.player import Player

class Generator:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.visual_sprites = pg.sprite.Group()

        self.player = Player((100,100),self.visual_sprites)

    def render(self):
        self.visual_sprites.draw(self.win)

    def update(self,dt):
        self.visual_sprites.update(dt)
