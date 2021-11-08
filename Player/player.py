import pygame
import time
class Player : 
    def __init__(self, ecran, variable, createNewMap, items) :
        self.ecran = ecran
        self.variable = variable
        self.createNewMap = createNewMap
        self.items = items
        self.pos = [1, 1]
        self.casepos = [0, 0]
        self.vivant = True
        self.win = False
        self.moveCooldown = 150
        self.index = 0
        self.holdDirection = {
            "LEFT"  : False,
            "RIGHT" : False,
            "UP"    : False,
            "DOWN"  : False,
        }
        self.inventory = {
            "item1" : 0,
            "item2" : 0,
            "item3" : 0,
            "item4" : 0,
        }


    def move(self, player) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : 
                return False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    return False
                if event.key == pygame.K_r :
                    player.win = True
                if event.key == pygame.K_p :
                    time.sleep(100)
                if event.key == pygame.K_LEFT or event.key == pygame.K_q :
                    self.holdDirection["LEFT"] = True
                    self.holdDirection["RIGHT"] = False
                    self.holdDirection["UP"] = False
                    self.holdDirection["DOWN"] = False 
                    if self.index == self.moveCooldown :
                        if self.casepos[0] > 0 :
                            if ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) == 2 :
                                self.pos[0] -= self.variable.caseSize
                                self.casepos[0] -= 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")

                            elif ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) != 1:
                                self.index = 0
                                self.pos[0] -= self.variable.caseSize
                                self.casepos[0] -= 1
                                self.walkOnItems()

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d : 
                    self.holdDirection["LEFT"] = False
                    self.holdDirection["RIGHT"] = True
                    self.holdDirection["UP"] = False
                    self.holdDirection["DOWN"] = False
                    if self.index == self.moveCooldown :
                        if self.casepos[0] < (self.variable.mapSize - 1) :
                            if ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) == 2 :
                                self.pos[0] += self.variable.caseSize
                                self.casepos[0] += 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")

                            elif ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) != 1 :
                                self.index = 0
                                self.pos[0] += self.variable.caseSize
                                self.casepos[0] += 1
                                self.walkOnItems()

                if event.key == pygame.K_UP or event.key == pygame.K_z :
                    self.holdDirection["LEFT"] = False
                    self.holdDirection["RIGHT"] = False
                    self.holdDirection["UP"] = True
                    self.holdDirection["DOWN"] = False
                    if self.index == self.moveCooldown :
                        if self.casepos[1] > 0 :
                            if ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) == 2 :
                                self.pos[1] -= self.variable.caseSize
                                self.casepos[1] -= 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) != 1:
                                self.index = 0
                                self.pos[1] -= self.variable.caseSize
                                self.casepos[1] -= 1
                                self.walkOnItems()
                    

                if event.key == pygame.K_DOWN or event.key == pygame.K_s : 
                    self.holdDirection["LEFT"] = False
                    self.holdDirection["RIGHT"] = False
                    self.holdDirection["UP"] = False
                    self.holdDirection["DOWN"] = True

                    if self.index == self.moveCooldown :
                        if self.casepos[1] < (self.variable.mapSize - 1) :
                            if ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) == 2 :
                                self.pos[1] += self.variable.caseSize
                                self.casepos[1] += 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) != 1:
                                self.index = 0
                                self.pos[1] += self.variable.caseSize
                                self.casepos[1] += 1
                                self.walkOnItems()
                return True

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT :
                    self.holdDirection["LEFT"] = False
                if event.key == pygame.K_RIGHT :
                    self.holdDirection["RIGHT"] = False
                if event.key == pygame.K_UP :
                    self.holdDirection["UP"] = False
                if event.key == pygame.K_DOWN :
                    self.holdDirection["DOWN"] = False

        for direction in self.holdDirection :
            if self.holdDirection[direction] :
                if direction == "LEFT" :
                    if self.index == self.moveCooldown :
                        if self.casepos[0] > 0 :
                            if ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) == 2 :
                                self.pos[0] -= self.variable.caseSize
                                self.casepos[0] -= 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")
                                

                            elif ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) != 1:
                                self.index = 0
                                self.pos[0] -= self.variable.caseSize
                                self.casepos[0] -= 1
                                self.walkOnItems()
                
                if direction == "RIGHT" : 
                    if self.index == self.moveCooldown :
                        if self.casepos[0] < (self.variable.mapSize - 1) :
                            if ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) == 2 :
                                self.pos[0] += self.variable.caseSize
                                self.casepos[0] += 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")

                            elif ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) != 1 :
                                self.index = 0
                                self.pos[0] += self.variable.caseSize
                                self.casepos[0] += 1
                                self.walkOnItems()

                if direction == "UP" :
                    if self.index == self.moveCooldown :
                        if self.casepos[1] > 0 :
                            if ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) == 2 :
                                self.pos[1] -= self.variable.caseSize
                                self.casepos[1] -= 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) != 1:
                                self.index = 0
                                self.pos[1] -= self.variable.caseSize
                                self.casepos[1] -= 1
                                self.walkOnItems()

                if direction == "DOWN" : 
                    if self.index == self.moveCooldown :
                        if self.casepos[1] < (self.variable.mapSize - 1) :
                            if ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) == 2 :
                                self.pos[1] += self.variable.caseSize
                                self.casepos[1] += 1
                                self.win = True
                                self.variable.winNumber += 1
                                print("You won")

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) != 1:
                                self.index = 0
                                self.pos[1] += self.variable.caseSize
                                self.casepos[1] += 1
                                self.walkOnItems()
                break

    def walkOnItems(self) :
        for i, item in enumerate(self.items.items) :
            for pos in self.items.items[item] :
                # print(str(i) + ": " + str(self.casepos) + str(pos))
                if self.casepos[0] == pos[0] and self.casepos[1] == pos[1] :
                    self.items.items[item].remove(pos)
                    self.inventory[item] += 1
                    return



    def movingCooldown(self) :
        if self.index != self.moveCooldown :
            self.index += 1
        # print(self.index)

    

    
