import pygame

class Ennemis :
    def __init__(self, variable):
        self.variable = variable
        self.ennemiColor = (255, 0, 0)
        self.ennemiCasePosList = []
        self.index = 0

    def ennemiInit(self) :
        for ennemi in range(self.variable.ennemiNumber + 1) :
            self.ennemiCasePosList.append([14, 0])

    def ennemiDisplay(self, ecran):
        for ennemi in self.ennemiCasePosList :
            print("ennemi :" + str(ennemi[0]))
            print(self.variable.caseSize)
            print(ennemi[0] * self.variable.caseSize)
            print(ennemi[1] * self.variable.caseSize)
            pygame.draw.rect(ecran, (255, 0, 0), (pygame.Rect((ennemi[0] * self.variable.caseSize + 1), (ennemi[1] * self.variable.caseSize + 1), (self.variable.caseSize - 1), (self.variable.caseSize - 1))))   

    def ennemiMove(self) : 
        self.index += 1
        if self.index == 100 :
            self.ennemiCasePosList[0][1] += 1
            self.index = 0
        # for x in range(len(self.ennemiCasePosList)) :
            
            # tempCasePos = self.ennemiCasePosList[x]
            # self.ennemiCasePosList[x] = [tempCasePos[0], tempCasePos[1]]









