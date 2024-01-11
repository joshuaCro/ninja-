import pygame as pg
from src.engine.settings import *
from os import walk

def load_folder(path,scale = (TILE_SIZE,TILE_SIZE)):
    img = []
    for _,__,values in walk(path):
        for v in values:
            image = pg.transform.scale(pg.image.load(path + '/' + v).convert(),scale)
            image.set_colorkey(TRANSPARET_COLOUR)

            img.append(image)

    return img