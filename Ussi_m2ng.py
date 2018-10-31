import pygame
import sys
import random
import time

pg = pygame

pg.image.load("taust.png")

#uss, selle asukoht, liikumine, pikenemine, suremine
class Uss():
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
        
#vajutades neid klahve muudab uss suunda        
    def muudaSuunda(self, suund):
        if suund=="RIGHT" and not self.direction=="LEFT":
            self.direction = "RIGHT"
        if suund=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        if suund=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        if suund=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"
 
