import pygame as pg
from src.engine.settings import *


class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.hitbox = None
        self.win = pg.display.get_surface()
        self.offset = pg.math.Vector2()

    def custom_draw(self):
        for layers in LAYERS.values():
            for sprites in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):



                if layers == sprites.z:
                    self.win.blit(sprites.image, sprites.rect)
