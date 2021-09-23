from time import sleep
class MapChecker : 
    def __init__(self, createNewMap, variable) :
        self.createNewMap = createNewMap
        self.variable = variable
        self.boxToCheck = [(0, 0)]
        self.checkedBox = []
        self.keyNumber = 1


    def mapChecker(self) :
        self.boxToCheck.append((0, 0))
        while len(self.boxToCheck) != 0 :
            
            boxToCheck = self.boxToCheck[0]

            #North
            tempBoxToCheckX = boxToCheck[0]
            tempBoxToCheckY = boxToCheck[1] - 1
            print(tempBoxToCheckX)
            print(tempBoxToCheckY)
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)           
            print("North done")

            if self.keyNumber == 0 :
                self.boxToCheck.clear()
                return

            #South
            tempBoxToCheckY = boxToCheck[1] + 1
            print(tempBoxToCheckX)
            print(tempBoxToCheckY)
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)
            print("South done")

            if self.keyNumber == 0 :
                self.boxToCheck.clear()
                return

            #East
            tempBoxToCheckX = boxToCheck[0] + 1
            tempBoxToCheckY = boxToCheck[1]
            print(tempBoxToCheckX)
            print(tempBoxToCheckY)
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)
            print("East done")

            if self.keyNumber == 0 :
                self.boxToCheck.clear()
                return

            #West
            tempBoxToCheckX = boxToCheck[0] - 1
            print(tempBoxToCheckX)
            print(tempBoxToCheckY)
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)
            print("West done")
            
            if self.keyNumber == 0 :
                self.boxToCheck.clear()
                return

            print(self.boxToCheck)

            self.checkedBox.append(boxToCheck)
            if self.keyNumber != 0 :
                del self.boxToCheck[0]

        self.checkedBox.clear()

        if self.keyNumber == 0 :
            print("You can clear the level.")
        else :
            print("You need to reset.")

        


    def boxChecker(self, x, y, checkedBox) :
        if x >= 0 and x <= (self.variable.mapSize - 1) and y >= 0 and y <= (self.variable.mapSize - 1) :
            for box in checkedBox :
                if box == (x, y) :
                    return
            if self.createNewMap.currentMap[x][y] == 2 :
                print("I found the key ! x : " + str(x) + " " + "y : " + str(y))
                print("I will finally stop hitting walls 😳 !")
                self.keyNumber -= 1
                

            if self.createNewMap.currentMap[x][y] == 1 :
                print("OUCH... that's a wall here -> x : " + str(x) + " "  + "y : " + str(y))

            if self.createNewMap.currentMap[x][y] == 0 :
                print("Nothing to report here -> x : " + str(x)  + " " + "y : " + str(y))
                # sleep(0.1)
                self.boxToCheck.append((x, y))
                
        else :
            print("It's out of the map... -> x : " + str(x) + " " + "y : " + str(y))

        


            # del self.boxToCheck[0]



    # def checkerInit(self) :
    #     self.findBoxToCheck()



# Faire 2 listes 
# Liste n°1 => contient les blocs tester
# Liste n°2 => contient les blocs à tester
# Tester les cases une par une si il est possible de se déplacer sur les cases adjacentes
# Si le bloc à tester est vide et que je suis pas passer au-dessus de la clé c'est qu'il faut reset
# Si je trouve la clé, le niveau est bon
# Le test de déplacement fait les 4 directions à chaque fois
# Si la position est déjà dans la liste des blocs tester on skip sinon on check si c'est accessible si oui on met dans tester sinon on la met pas
# C'est clairement une réaction en chaine.