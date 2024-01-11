import pygame as pg
import pickle

class FileHandler:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.data = {'player':{
                               'fruits':0,
                               },
                     'level':0
                     }
        self.orig_data = self.data

        self.timer = 0

    def save(self):
        with open('docs/saves/save-1.sav','wb') as file:
            pickle.dump(self.data,file)

    def load(self):
        try:
            with open('docs/saves/save-1.sav','rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print('[ERROR] file not found')

    def auto_save(self,dt):
        self.timer += 1 * dt

        if self.timer >= 1:
            self.save()
            self.timer = 0
            print('auto saved')
