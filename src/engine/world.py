import pygame as pg

class World:
    def __init__(self, filehandler):
        self.win = pg.display.get_surface()

        self.file_handler = filehandler


    def render(self):...

    def update(self, dt):
        self.file_handler.data = self.file_handler.data


