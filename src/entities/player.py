import pygame as pg
from src.entities.entity import Entity

class Player(Entity):
    def __init__(self,pos,group):
        img = pg.Surface((64,64))

        super().__init__(pos,img,group)

