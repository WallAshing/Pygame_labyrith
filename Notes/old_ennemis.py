import pygame
import random

class Old_Ennemis :
    def __init__(self, variable, createNewMap):
        self.variable = variable
        self.createNewMap = createNewMap
        self.ennemiColor = (255, 0, 0)
        self.ennemiCasePosList = []
        self.index = 0
        self.ennemiNewBox = []
        self.ennemiWalkedBox = [[24, 0]]
        self.ennemiDeadEndBox = []
        self.ennemiDirection = []
        self.ennemiWalkableBox = []
        self.wallNumber = 0


    def ennemiInit(self) :          
        for i in range(0, self.variable.ennemiNumber) :
            self.ennemiCasePosList.append([(self.variable.mapSize - 1), 0])

    def ennemiDisplay(self, ecran):
        for ennemi in self.ennemiCasePosList :
            pygame.draw.rect(ecran, (255, 0, 0), (pygame.Rect((ennemi[0] * self.variable.caseSize + 1), (ennemi[1] * self.variable.caseSize + 1), (self.variable.caseSize - 1), (self.variable.caseSize - 1))))   


    def ennemiMove(self) : 
        self.index += 1
        if self.index == 100 : #toute les 300 incrementations, fait un déplacement des ennemis
            print("-----------------------------------------------------------------------------------------")
            for ennemi in range(len(self.ennemiCasePosList)) : # pour tout les ennemi

                i = 0
                
                self.ennemiPathing(i) # lance la fonction ennemi pathing

                TempBox = []
                TempDirection = []

                for box1 in self.ennemiWalkableBox : # append toutes les box de ennemiWalkableBox dans une list temporaire
                   TempBox.append(box1)

                for direct1 in self.ennemiDirection : # append toutes les box de ennemiDirection dans une list temporaire
                    TempDirection.append(direct1)

                print("walkable box before : " + str(self.ennemiWalkableBox))
                print("Ennemi pos: " + str(self.ennemiCasePosList))
                print("Direction before : " + str(TempDirection))
                print("DeadEnd box before : " + str(self.ennemiDeadEndBox))

                for walkableBox in self.ennemiWalkableBox : # pour toutes les 
                    print("ever Walkable box : " + str(self.ennemiWalkableBox))
                    print(i)
                    print("Walkable box : " + str(walkableBox))
                    for deadEndbox in self.ennemiDeadEndBox :
                        # print(str(walkableBox) + "<= deadEndbox walked =>" + str(deadEndbox))
                        if walkableBox == deadEndbox :
                            print("deadend true")
                            del self.ennemiWalkableBox[i]
                            del self.ennemiDirection[i]
                            i -= 1
                            
                    for walkedBox in self.ennemiWalkedBox :
                        # print("test boucle")
                        print(str(walkableBox) + "<= walkable walked =>" + str(walkedBox))
                        if walkableBox == walkedBox :
                            print("walkable true")
                            # print("Walked box : " + str(walkedBox) + "his index is : " + i)
                            del self.ennemiWalkableBox[i]
                            del self.ennemiDirection[i]
                            i -= 1
                            break
                            
                    i += 1


                if not self.ennemiWalkableBox :
                    i = 0
                    print("need to reset walkableBox")
                    print(TempBox)
                    print(TempDirection)
                    for box in TempBox :
                        # print("the box is "+ str(box))
                        self.ennemiWalkableBox.append(box)
                    for direct in TempDirection :
                        self.ennemiDirection.append(direct)
                    for walkableBox in self.ennemiWalkableBox :
                        for deadEndbox in self.ennemiDeadEndBox :
                            if walkableBox == deadEndbox :
                                del self.ennemiWalkableBox[i]
                                del self.ennemiDirection[i]
                                i -= 1
                                break
                        i += 1
                    if not self.ennemiWalkableBox :
                        return
                    
                print("result walked box : " + str(self.ennemiWalkedBox))
                print("result walkable box : " + str(self.ennemiWalkableBox))


                direction = random.randint(0, ((len(self.ennemiWalkableBox)) - 1))   

                print(len(self.ennemiWalkableBox) - 1)
                print(direction)

                if self.ennemiDirection[direction] == "North":
                    self.ennemiCasePosList[ennemi][1] -= 1

                elif self.ennemiDirection[direction] == "South" :
                    self.ennemiCasePosList[ennemi][1] += 1

                elif self.ennemiDirection[direction] == "East" :
                    self.ennemiCasePosList[ennemi][0] += 1

                elif self.ennemiDirection[direction] == "West" :
                    self.ennemiCasePosList[ennemi][0] -= 1

                if self.ennemiWalkedBox :
                    for i in range(len(self.ennemiWalkedBox)) :
                        if self.ennemiWalkedBox[i] == self.ennemiCasePosList[ennemi] :
                            break
                        else :
                            if i == (len(self.ennemiWalkedBox) - 1) :
                                varX = self.ennemiCasePosList[ennemi][0]
                                varY = self.ennemiCasePosList[ennemi][1]
                                self.ennemiWalkedBox.append([varX, varY])
                else :
                    varX = self.ennemiCasePosList[ennemi][0]
                    varY = self.ennemiCasePosList[ennemi][1]
                    self.ennemiWalkedBox.append([varX, varY])


            self.index = 0
            self.ennemiDirection.clear()

    def ennemiPathing(self, ennemiNumber) : 
        self.ennemiWalkableBox.clear()
        self.wallNumber = 0
        ennemiBox = self.ennemiCasePosList[ennemiNumber]

        #North
        tempBoxToCheckX = ennemiBox[0]
        tempBoxToCheckY = ennemiBox[1] - 1
        print("---------")
        print("---------")
        print("ennemibox" + str(ennemiBox))
        print("---------")
        print("---------")

        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY, ennemiNumber, "North")  

        #South
        tempBoxToCheckY = ennemiBox[1] + 1
        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY, ennemiNumber, "South")

        #East
        tempBoxToCheckX = ennemiBox[0] + 1
        tempBoxToCheckY = ennemiBox[1]
        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY, ennemiNumber, "East")
        self.ennemiDirection

        #West
        tempBoxToCheckX = ennemiBox[0] - 1
        self.ennemiBoxChecker(tempBoxToCheckX, tempBoxToCheckY, ennemiNumber, "West")
        self.ennemiDirection

        print("wall number : " + str(self.wallNumber))

        if self.wallNumber == 3 :
            if not self.ennemiDeadEndBox :
                self.ennemiDeadEndBox.append([ennemiBox[0], ennemiBox[1]])
            else :
                for i in range(len(self.ennemiDeadEndBox)) :
                    if self.ennemiDeadEndBox[i] == [ennemiBox[0], ennemiBox[1]] :
                        break
                    else :
                        print("found a dead end")
                        if i == (len(self.ennemiDeadEndBox) - 1) :
                            self.ennemiDeadEndBox.append([ennemiBox[0], ennemiBox[1]])

        for toCheckBox in self.ennemiWalkableBox :
            for box in self.ennemiDeadEndBox :
                if box == toCheckBox :
                    break
            


    def ennemiBoxChecker(self, x, y, ennemiNumber, direction) :
        if x >= 0 and x <= (self.variable.mapSize - 1) and y >= 0 and y <= (self.variable.mapSize - 1) :
            
            if self.ennemiNewBox :
                for box in self.ennemiNewBox : #self.ennemiNewBox[ennemiNumber]
                    if box == (x, y) :
                        self.ennemiDirection.append(direction)
                        self.ennemiWalkableBox.append([x, y])
                        return

            if self.createNewMap.currentMap[x][y] == 2 :
                return

            if self.createNewMap.currentMap[x][y] == 1 :
                self.wallNumber += 1
                return

            if self.createNewMap.currentMap[x][y] == 0 :
                self.ennemiNewBox.append([x, y])
                self.ennemiWalkableBox.append([x, y])
                self.ennemiDirection.append(direction)
        else :
            self.wallNumber += 1
            return


                        



