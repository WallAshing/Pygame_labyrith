import pygame

class Ennemis :
    def __init__(self, variable):
        self.variable = variable
        self.ennemiColor = (255, 0, 0)
        self.ennemiCasePosList = []
        self.index = 0
        self.ennemiNewBox = []
        self.ennemiWalkedBox = []
        self.ennemiDeadEndBox = []

    def ennemiInit(self) :
        for i in range(0, self.variable.ennemiNumber) :
            self.ennemiCasePosList.append([(self.variable.mapSize - 3), 0])
            print(str(i) + " ennemi spawned")

    def ennemiDisplay(self, ecran):
        for ennemi in self.ennemiCasePosList :
            # print("ennemi :" + str(ennemi[0]))
            # print(self.variable.caseSize)
            # print(ennemi[0] * self.variable.caseSize)
            # print(ennemi[1] * self.variable.caseSize)
            pygame.draw.rect(ecran, (255, 0, 0), (pygame.Rect((ennemi[0] * self.variable.caseSize + 1), (ennemi[1] * self.variable.caseSize + 1), (self.variable.caseSize - 1), (self.variable.caseSize - 1))))   

    def ennemiMove(self) : 
        self.index += 1
        if self.index == 150 :
            self.ennemiCasePosList[0][1] += 1
            self.index = 0
        # for x in range(len(self.ennemiCasePosList)) :
            
            # tempCasePos = self.ennemiCasePosList[x]
            # self.ennemiCasePosList[x] = [tempCasePos[0], tempCasePos[1]]

    def ennemiPathing(self, ennemiNumber) : 
        ennemiBox = self.ennemiCasePosList[ennemiNumber]

        #North
        tempBoxToCheckX = ennemiBox[0]
        tempBoxToCheckY = ennemiBox[1] - 1
        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY)     

        #South
        tempBoxToCheckY = ennemiBox[1] + 1
        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY)

        #East
        tempBoxToCheckX = ennemiBox[0] + 1
        tempBoxToCheckY = ennemiBox[1]
        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY)

        #West
        tempBoxToCheckX = ennemiBox[0] - 1
        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY)


    def ennemiBoxChecker(self, x, y) :
        if x >= 0 and x <= (self.variable.mapSize - 1) and y >= 0 and y <= (self.variable.mapSize - 1) :
            
            # for box in checkedBox :
            #     if box == (x, y) :
            #         return

            # for box in self.boxToCheck :
            #     if box == (x, y) :
            #         return

            if self.createNewMap.currentMap[x][y] == 1 :
                return

            if self.createNewMap.currentMap[x][y] == 0 :
                for box in self.ennemiNewBox : 
                    if box != (x, y) :
                        self.ennemiNewBox.append((x, y))

                        



