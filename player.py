import pygame

from variables import *

variables = Variables()

class Player : 
    def __init__(self, ecran) :
        self.ecran = ecran
        self.vit = 5 
        self.pos = [1, 1]
        self.casepos = [0, 0]
        self.vivant = True

    # def deplacement(self, dir):
    #     self.pos[0] += dir*vit

    def attack(self) : 
        print("ATTAQUER")

    def move(self, event) : 
        if event.key == pygame.K_LEFT :
            if self.pos[0] >= variables.caseSize :
                self.pos[0] -= variables.caseSize
                self.casepos[0] -= 1

        if event.key == pygame.K_RIGHT : 
            if self.pos[0] < (500 - variables.caseSize) :
                self.pos[0] += variables.caseSize
                self.casepos[0] += 1


        if event.key == pygame.K_UP :
            if self.pos[1] >= variables.caseSize :
                self.pos[1] -= variables.caseSize
                self.casepos[1] -= 1

        if event.key == pygame.K_DOWN : 
            if self.pos[1] < (500 - variables.caseSize) :
                self.pos[1] += variables.caseSize
                self.casepos[1] += 1

                

