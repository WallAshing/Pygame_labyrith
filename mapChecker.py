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
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)           

            #South
            tempBoxToCheckY = boxToCheck[1] + 1
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)

            #East
            tempBoxToCheckX = boxToCheck[0] + 1
            tempBoxToCheckY = boxToCheck[1]
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)

            #West
            tempBoxToCheckX = boxToCheck[0] - 1
            self.boxChecker(tempBoxToCheckX, tempBoxToCheckY, self.checkedBox)
            
            self.checkedBox.append(boxToCheck)

            if self.keyNumber != 0 :
                del self.boxToCheck[0]
                
            else :
                self.boxToCheck.clear()
                self.checkedBox.clear()
                return

        self.checkedBox.clear()

        


    def boxChecker(self, x, y, checkedBox) :
        if x >= 0 and x <= (self.variable.mapSize - 1) and y >= 0 and y <= (self.variable.mapSize - 1) :
            
            for box in checkedBox :
                if box == (x, y) :
                    return

            for box in self.boxToCheck :
                if box == (x, y) :
                    return

            if self.createNewMap.currentMap[x][y] == 2 :
                self.keyNumber -= 1

            if self.createNewMap.currentMap[x][y] == 1 :
                return

            if self.createNewMap.currentMap[x][y] == 0 :
                self.boxToCheck.append((x, y))
                
        else :
            return