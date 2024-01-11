import pygame as pg
from src.engine.settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self,pos,img,group):
        super().__init__(group)

        self.image = img
        self.rect = self.image.get_rect(center = pos)