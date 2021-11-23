
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
        self.moveCooldown = 50
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
        self.selectItem = {
            "itemName" : "item1",
            "usingItem" : False,
        }

    def playerDisplay(self):
        pygame.draw.rect(self.ecran, (0, 255, 0), (pygame.Rect((self.casepos[0] * self.variable.caseSize + 1), (self.casepos[1] * self.variable.caseSize + 1), (self.variable.caseSize - 1), (self.variable.caseSize - 1))))

    def choseItem(self, itemName):
        self.selectItem["itemName"] = itemName

    def useItem(self):
        self.inventory[self.selectItem["itemName"]] -= 1
        self.selectItem["usingItem"] = True

    def move(self, player) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : 
                return False
            if event.type == pygame.KEYDOWN :
                # print(event.key)
                if event.key == pygame.K_ESCAPE :
                    return False
                if event.key == pygame.K_r :
                    player.win = True
                if event.key == 49 :
                    self.choseItem("item1")
                if event.key == 50 :
                    self.choseItem("item2")
                if event.key == 51 :
                    self.choseItem("item3")
                if event.key == 52 :
                    self.choseItem("item4")
                if event.key == pygame.K_SPACE :
                    self.useItem()
                if event.key == pygame.K_p :
                    time.sleep(20)
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

                            elif ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True and ((self.createNewMap.currentMap[self.casepos[0] - 2])[self.casepos[1]]) == 0 and self.casepos[0] > 1:
                                self.index = 0
                                self.selectItem["usingItem"] = False
                                self.pos[0] -= (self.variable.caseSize * 2)
                                self.casepos[0] -= 2
                                self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) == 0:
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
 
                            elif ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True :
                                if self.casepos[0] < (self.variable.mapSize - 2) and ((self.createNewMap.currentMap[self.casepos[0] + 2])[self.casepos[1]]) == 0  :
                                    self.index = 0
                                    self.pos[0] += (self.variable.caseSize * 2)
                                    self.selectItem["usingItem"] = False
                                    self.casepos[0] += 2
                                    self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) == 0 :
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

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True and ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 2]) == 0 and self.casepos[1] > 1:
                                self.index = 0
                                self.pos[1] -= (self.variable.caseSize * 2)
                                self.selectItem["usingItem"] = False
                                self.casepos[1] -= 2
                                self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) == 0 :
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

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True :
                                if self.casepos[1] < (self.variable.mapSize - 2) and ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 2]) == 0 :
                                    self.index = 0
                                    self.pos[1] += (self.variable.caseSize * 2)
                                    self.selectItem["usingItem"] = False
                                    self.casepos[1] += 2
                                    self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) == 0 :
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
                                
                            elif ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True and ((self.createNewMap.currentMap[self.casepos[0] - 2])[self.casepos[1]]) == 0 and self.casepos[0] > 1:
                                self.index = 0
                                self.selectItem["usingItem"] = False
                                self.pos[0] -= (self.variable.caseSize * 2)
                                self.casepos[0] -= 2
                                self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0] - 1])[self.casepos[1]]) == 0:
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

                            elif ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True :
                                if self.casepos[0] < (self.variable.mapSize - 2) and ((self.createNewMap.currentMap[self.casepos[0] + 2])[self.casepos[1]]) == 0 :
                                    self.index = 0
                                    self.pos[0] += (self.variable.caseSize * 2)
                                    self.selectItem["usingItem"] = False
                                    self.casepos[0] += 2
                                    self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0] + 1])[self.casepos[1]]) == 0 :
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

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True and ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 2]) == 0 and self.casepos[1] > 1:
                                self.index = 0
                                self.pos[1] -= (self.variable.caseSize * 2)
                                self.selectItem["usingItem"] = False
                                self.casepos[1] -= 2
                                self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] - 1]) == 0:
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

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) == 1 and self.selectItem["itemName"] == "item1" and self.selectItem["usingItem"] == True :
                                if self.casepos[1] < (self.variable.mapSize - 2) and ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 2]) == 0 :
                                    self.index = 0
                                    self.pos[1] += (self.variable.caseSize * 2)
                                    self.selectItem["usingItem"] = False
                                    self.casepos[1] += 2
                                    self.walkOnItems()

                            elif ((self.createNewMap.currentMap[self.casepos[0]])[self.casepos[1] + 1]) == 0:
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

