import pygame
class Player : 
    def __init__(self, ecran, variable, createNewMap) :
        self.variable = variable
        self.createNewMap = createNewMap
        self.ecran = ecran
        self.vit = 5 
        self.pos = [1, 1]
        self.casepos = [0, 0]
        self.vivant = True
        self.win = False

    # def deplacement(self, dir):
    #     self.pos[0] += dir*vit

    def move(self, event) : 
        
        if event.key == pygame.K_LEFT or event.key == pygame.K_q :
            if self.casepos[0] > 0 :
                if ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) == 2 :
                    self.pos[0] -= self.variable.caseSize
                    self.casepos[0] -= 1
                    self.win = True
                    self.variable.winNumber += 1
                    print("You won")

                elif ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) != 1:
                    self.pos[0] -= self.variable.caseSize
                    self.casepos[0] -= 1

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d : 
            if self.casepos[0] < (self.variable.mapSize - 1) :

                if ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) == 2 :
                    self.pos[0] += self.variable.caseSize
                    self.casepos[0] += 1
                    self.win = True
                    self.variable.winNumber += 1
                    print("You won")

                elif ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) != 1 :
                    self.pos[0] += self.variable.caseSize
                    self.casepos[0] += 1

        if event.key == pygame.K_UP or event.key == pygame.K_z :
            if self.casepos[1] > 0 :
                if ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) == 2 :
                    self.pos[1] -= self.variable.caseSize
                    self.casepos[1] -= 1
                    self.win = True
                    self.variable.winNumber += 1
                    print("You won")

                elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) != 1:
                    self.pos[1] -= self.variable.caseSize
                    self.casepos[1] -= 1

        if event.key == pygame.K_DOWN or event.key == pygame.K_s : 
            if self.casepos[1] < (self.variable.mapSize - 1) :
                if ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) == 2 :
                    self.pos[1] += self.variable.caseSize
                    self.casepos[1] += 1
                    self.win = True
                    self.variable.winNumber += 1
                    print("You won")

                elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) != 1:
                    self.pos[1] += self.variable.caseSize
                    self.casepos[1] += 1

                

