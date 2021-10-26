from Ennemis.ennemi import *
import pygame

class Ennemis :

    def __init__(self, variable, createNewMap):
        self.variable = variable
        self.createNewMap = createNewMap
        self.ennemiColor = (255, 0, 0)
        self.ennemiCasePosList = []
        self.ennemis = {}

    def ennemisInit(self) :          
        for i in range(0, self.variable.ennemiNumber) :
            self.ennemiCasePosList.append([(self.variable.mapSize - 1), 0])
            self.ennemis["Ennemi{0}".format(i)] = Ennemi(self.createNewMap, self.ennemiCasePosList[i]) # Créé un dictionnaire d'énnemis

    def ennemisMove(self) :
        for i in range(0, self.variable.ennemiNumber) :
            self.ennemis["Ennemi{0}".format(i)].move()
            
    def ennemisDisplay(self, ecran):
        for ennemi in self.ennemiCasePosList :
            pygame.draw.rect(ecran, (255, 0, 0), (pygame.Rect((ennemi[0] * self.variable.caseSize + 1), (ennemi[1] * self.variable.caseSize + 1), (self.variable.caseSize - 1), (self.variable.caseSize - 1))))