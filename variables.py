class Variables :
    def __init__(self) :
        self.mapSize = 20
        self.windowSize = (500 // self.mapSize * self.mapSize, 500 // self.mapSize * self.mapSize)
        self.caseSize = self.windowSize[0] / self.mapSize
        self.keyInitial = 1 
        self.keyNumber = 1
        self.keyColor = (255, 0, 0)

