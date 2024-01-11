import pygame as pg
from src.engine.world import World


class Scene:
    def __init__(self, filehandler):
        self.win = pg.display.get_surface()

        self.filehandler = filehandler

    def render(self):
        self.win.fill((10, 40, 70))

    def update(self, dt):...
