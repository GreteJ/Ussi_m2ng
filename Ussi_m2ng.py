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
 
#liikumine suuna järgi
    def liikumine(self,foodPos):
        if self.direction== "RIGHT":
            self.position[0] += 10
        if self.direction== "LEFT":
            self.position[0] -= 10
        if self.direction== "UP":
            self.position[1] -= 10
        if self.direction== "DOWN":
            self.position[1] += 10
        self.body.insert(0,list(self.position))
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0
 
#keha juurde tekkimine
    def kehaTulek(self):
        return self.body

#kui uss põrkub enda või seinaga saab surma
    def porkumine(self):
        if self.position[0] > 590 or self.position[0]< 0:
            return 1
        elif self.position[1] > 590 or self.position[1]< 0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0
    
    def peaKoordinaat(self):
        return self.position
    
    def peaKoordinaat(self):
        return self.body
