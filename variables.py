class Variables :
    def __init__(self) :
        self.mapSize = 25
        self.windowSizeSetting = 500
        self.windowSize = (self.windowSizeSetting // self.mapSize * self.mapSize, self.windowSizeSetting // self.mapSize * self.mapSize)
        self.caseSize = self.windowSize[0] / self.mapSize
        self.keyInitial = 1 
        self.keyNumber = 1
        self.keyColor = (0, 0, 255)
        self.winNumber = 0
        self.ennemiNumber = 1
        self.itemsNumber = {
            "item1" : 1,
            "item2" : 1,
            "item3" : 1,
            "item4" : 1,
        }
