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

    #toit, selle tekkimine ja asukoht
class toit():
    def __init__(self):
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen = True
        
    def toiduKoordinaat(self):
        return self.position

#toit tekib suvalistesse kohtadesse
    def toitTekib(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
            self.isFoodOnScreen == True
            
#loob uue toidu kuhugi punkti         
    def looToit(self, x, y):
        self.position = [x,y]
        
        
#mängu suurus, nimi
window = pg.display.set_mode((600,600))
pg.display.set_caption("Ussi_mäng")
fps = pg.time.Clock()

score = 0

uss = Uss()
toit = toit()

#mäng lõppeb, läheb kinni
def over():
    pg.quit()
    sys.exit()

#mäng algab
while True:
    taust = pygame.image.load("taust.png")
    window.blit(taust, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] == 1:
            uss.muudaSuunda("RIGHT")
        elif pressed[pygame.K_LEFT] == 1:
            uss.muudaSuunda("LEFT")
        elif pressed[pygame.K_UP] == 1:
            uss.muudaSuunda("UP")
        elif pressed[pygame.K_DOWN] == 1:
            uss.muudaSuunda("DOWN")
        elif pressed[pygame.K_ESCAPE] == 1:
            gameOver()

#kui uss sööb toidu, siis toit kaob ja saab punkti (skoori süsteem)
    foodPos = toit.toiduKoordinaat()
    if(uss.liikumine(foodPos)==1):
        score+=1
        xx = random.randrange(1,50)*10
        yy = random.randrange(1,50)*10
        toit.looToit(xx, yy)
        
    for pos in uss.kehaTulek():
        pg.draw.rect(window,pg.Color(255,255,0),pg.Rect(pos[0],pos[1],10,10))
    pg.draw.rect(window,pg.Color(255,255,255),pg.Rect(foodPos[0],foodPos[1],10,10))
    if(uss.porkumine()==1):
        over()
    pg.display.set_caption("Uss | Score : "+ str(score) )
    pg.display.flip()
    fps.tick(24)

