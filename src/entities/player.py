import pygame as pg
from src.engine.settings import *
from src.entities.entity import Entity

class Player(Entity):
    def __init__(self,pos,group):
        image = pg.Surface((100,100))

        super().__init__(pos,image,group)