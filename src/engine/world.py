import pygame as pg
from src.world.generator import Generator

class World:
    def __init__(self, filehandler):
        self.win = pg.display.get_surface()

        self.file_handler = filehandler

        self.generator = Generator()

    def render(self):
        self.generator.render()

    def update(self, dt):
        self.file_handler.data = self.file_handler.data

        self.generator.update(dt)
