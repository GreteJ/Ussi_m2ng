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
        
