
import random

class Enemy :
    def __init__(self, createNewMap, ennemicasePos):
        self.createNewMap = createNewMap
        self.casePos = ennemicasePos
        self.pos = (self.casePos[0], self.casePos[1])
        self.index = 0
        self.wallNumber = 0
        self.movingCooldown = 100
        self.newBox = []
        self.walkedBox = []
        self.deadEndBox = []
        self.walkableBox = []
        self.tempWalkableBox = []
        self.boxToSuppr = []
        self.surroundingBox = []

    def move(self) :
        self.index += 1
        if self.index == self.movingCooldown :
            self.decisionMaker()
            self.refreshVars() # à la fin

    def decisionMaker(self) :
        self.directionsChecker()
        for walkableBox in self.walkableBox:
            self.tempWalkableBox.append(walkableBox)
            if len(self.deadEndBox) > 0 :
                for deadEndBox in self.deadEndBox :
                    # print(str(walkableBox) + " and " + str(deadEndBox))
                    if walkableBox == deadEndBox :
                        self.boxToSuppr.append(walkableBox)
                        break
            if len(self.walkableBox) > 0 and len(self.walkedBox) > 0 :
                for walkedBox in self.walkedBox :
                    if walkableBox == walkedBox :
                        self.boxToSuppr.append(walkableBox)
                        break  
        # print("this is walkedBox = " + str(self.walkedBox))
        # print("this is deadEndBox = " + str(self.deadEndBox))
        # print(str(len(self.walkableBox)) + " and it's " + str(self.walkableBox))
        self.SupprBoxes()

        self.movementDecision()

    def movementDecision(self) :
        if len(self.walkableBox) > 0 :
            boxNumber = random.randint(0, len(self.walkableBox) - 1)
            self.casePos[0] = self.walkableBox[boxNumber][0]
            self.casePos[1] = self.walkableBox[boxNumber][1]
            self.pos = self.walkableBox[boxNumber]
        else :
            for tempBox in self.tempWalkableBox :
                self.walkableBox.append(tempBox)
            for walkableBox in self.walkableBox:
                for deadEndBox in self.deadEndBox :
                    if walkableBox == deadEndBox :
                        self.boxToSuppr.append(walkableBox)

            self.SupprBoxes()

            if len(self.walkableBox) > 0 :
                boxNumber = random.randint(0, len(self.walkableBox) - 1)
                self.casePos[0] = self.walkableBox[boxNumber][0]
                self.casePos[1] = self.walkableBox[boxNumber][1]
                self.pos = self.walkableBox[boxNumber]
            else : 
                print("Can't move 😢")

    def directionsChecker(self) :
        x, y = self.directionToPosition(self.pos, "North")
        self.boxChecker(x, y)

        x, y = self.directionToPosition(self.pos, "South")
        self.boxChecker(x, y)

        x, y = self.directionToPosition(self.pos, "East")
        self.boxChecker(x, y)

        x, y = self.directionToPosition(self.pos, "West")
        self.boxChecker(x, y)

        self.whatsInMyBox(self.pos)

    def boxChecker(self, x, y):
        if x < len(self.createNewMap.currentMap) and x >= 0 and y < len(self.createNewMap.currentMap) and y >= 0 :
            if self.createNewMap.currentMap[x][y] == 2 :
                return

            if self.createNewMap.currentMap[x][y] == 1 :
                self.wallNumber += 1
                return

            if self.createNewMap.currentMap[x][y] == 0 :
                for newBox in self.newBox :
                    if newBox[0] == x and newBox[1] == y :
                        self.walkableBox.append((x, y))
                        return
                if self.walkedBox :
                    for walkedBox in self.walkedBox :
                        if walkedBox[0] == x and walkedBox[1] == y :
                            self.walkableBox.append((x, y))
                            return
                if self.deadEndBox :
                    for deadEndBox in self.deadEndBox :
                        if deadEndBox[0] == x and deadEndBox[1] == y :
                            self.walkableBox.append((x, y))
                            return
                self.newBox.append((x, y))
                self.walkableBox.append((x, y))
                return
        else :
            self.wallNumber += 1
            return

    def directionToPosition(self, pos, direction) :
        x, y = (pos[0], pos[1])
        if direction == "North":
            y = pos[1] - 1
            return x, y
        if direction == "South":
            y = pos[1] + 1
            return x, y
        if direction == "East":
            x = pos[0] + 1
            return x, y
        if direction == "West":
            x = pos[0] - 1
            return x, y

    def refreshVars(self) :
        self.pos = (self.casePos[0], self.casePos[1] )
        self.wallNumber = 0
        self.index = 0
        self.walkableBox.clear()
        self.tempWalkableBox.clear()
   
    def SupprBoxes(self) :
        for boxToSuppr in self.boxToSuppr :
            self.walkableBox.remove(boxToSuppr)
        self.boxToSuppr.clear()

    def whatsInMyBox(self, pos) :
        # print("this is newBox = " + str(self.newBox))
        # print("this is walkedBox = " + str(self.walkedBox))
        # print("this is deadEndBox = " + str(self.deadEndBox))
        # print("this is walkableBox = " + str(self.walkableBox))

        if self.wallNumber >= 3 :
            for deadEndBox in self.deadEndBox :
                if deadEndBox == pos :
                    return
            self.deadEndBox.append(pos)
        else :
            for walkedBox in self.walkedBox :
                if walkedBox == pos :
                    return
            self.walkedBox.append(pos)

