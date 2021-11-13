from Enemies.enemy import *
import pygame

class Enemies :

    def __init__(self, ecran, variable, createNewMap):
        self.variable = variable
        self.createNewMap = createNewMap
        self.ecran = ecran
        self.ennemiColor = (255, 0, 0)
        self.ennemiCasePosList = []
        self.ennemis = {}

    def ennemiesInit(self) :          
        for i in range(0, self.variable.ennemiNumber) :
            self.ennemiCasePosList.append([(self.variable.mapSize - 1), 0])
            self.ennemis["Ennemi{0}".format(i)] = Enemy(self.createNewMap, self.ennemiCasePosList[i]) # Créé un dictionnaire d'énnemis

    def ennemies(self):
        self.ennemiesMove()
        self.ennemiesDisplay()

    def ennemiesMove(self) :
        for i in range(0, self.variable.ennemiNumber) :
            self.ennemis["Ennemi{0}".format(i)].move()
            
    def ennemiesDisplay(self):
        for ennemi in self.ennemiCasePosList :
            pygame.draw.rect(self.ecran, (255, 0, 0), (pygame.Rect((ennemi[0] * self.variable.caseSize + 1), (ennemi[1] * self.variable.caseSize + 1), (self.variable.caseSize - 1), (self.variable.caseSize - 1))))