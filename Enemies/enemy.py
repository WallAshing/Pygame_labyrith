
import random
from Enemies.Enemies_Features.explorerChecker import *
from Enemies.Enemies_Features.explorerDecision import *
from Enemies.Enemies_Features.miscellaneous import SupprBoxes

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
        directionsChecker(self.pos, self.createNewMap.currentMap, self.wallNumber, self.newBox, self.walkableBox, self.walkedBox, self.deadEndBox)
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
        SupprBoxes(self.boxToSuppr, self.walkableBox)

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

            SupprBoxes(self.boxToSuppr, self.walkableBox)

            if len(self.walkableBox) > 0 :
                boxNumber = random.randint(0, len(self.walkableBox) - 1)
                self.casePos[0] = self.walkableBox[boxNumber][0]
                self.casePos[1] = self.walkableBox[boxNumber][1]
                self.pos = self.walkableBox[boxNumber]
            else : 
                print("Can't move 😢")



    def refreshVars(self) :  #add to miscellaneous if I find how         
        self.pos = (self.casePos[0], self.casePos[1])
        self.wallNumber = 0
        self.index = 0
        self.walkableBox.clear()
        self.tempWalkableBox.clear()
   

