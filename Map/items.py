import pygame
import random

class Items :
    def __init__(self, ecran, variables, createNewMap) :
        self.ecran = ecran
        self.variables = variables
        self.createNewMap = createNewMap
        self.items = {
            "item1" : [],
            "item2" : [],
            "item3" : [],
            "item4" : [],
        }
        
    
    def itemsInit(self) :
        for item in self.items :
            for i in range(self.variables.itemsNumber[item]) :
                case = self.createNewMap.spawnableCaseList[random.randint(0, (len(self.createNewMap.spawnableCaseList) - 1))] 
                self.items[item].append(case)
            


    def itemsDisplay(self) :
        for item in self.items["item1"] :
            pygame.draw.circle(self.ecran, (255, 255, 255), ((item[0] * self.variables.caseSize + (self.variables.caseSize/2) + 1), (item[1] * self.variables.caseSize + (self.variables.caseSize/2)  + 1 )), 5)
        for item in self.items["item2"] :
            pygame.draw.circle(self.ecran, (255, 0, 0), ((item[0] * self.variables.caseSize + (self.variables.caseSize/2) + 1), (item[1] * self.variables.caseSize + (self.variables.caseSize/2)  + 1 )), 5)
        for item in self.items["item3"] :
            pygame.draw.circle(self.ecran, (0, 0, 255), ((item[0] * self.variables.caseSize + (self.variables.caseSize/2) + 1), (item[1] * self.variables.caseSize + (self.variables.caseSize/2)  + 1 )), 5)
        for item in self.items["item4"] :
            pygame.draw.circle(self.ecran, (0, 255, 0), ((item[0] * self.variables.caseSize + (self.variables.caseSize/2) + 1), (item[1] * self.variables.caseSize + (self.variables.caseSize/2)  + 1 )), 5)