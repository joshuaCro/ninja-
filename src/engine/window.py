import pygame as pg
import sys
from src.engine.settings import *
from src.engine.support.file_handler import FileHandler
from src.engine.scene import Scene


class Window:
    def __init__(self):
        pg.init()
        pg.display.init()
        pg.font.init()
        pg.mixer.init()

        self.win = pg.display.set_mode(RES)#, flags=pg.FULLSCREEN | pg.NOFRAME)
        pg.display.set_caption(TITLE)

        self.clock = pg.time.Clock()

        self.file_handler = FileHandler()
        self.file_handler.load()
        self.scene = Scene(self.file_handler)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.file_handler.save()
                pg.quit()
                sys.exit()


    def render(self):
        self.scene.render()

        pg.display.set_caption(f'{TITLE} | {self.clock.get_fps() :.0f}')

        pg.display.flip()

    def update(self):
        dt = self.clock.tick(FPS) / 1000

        self.file_handler.auto_save(dt)

        self.scene.update(dt)

    def run(self):
        while 1:
            self.event_handler()
            self.render()
            self.update()
