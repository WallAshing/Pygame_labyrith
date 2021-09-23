import pygame
import random
import math

ecran = pygame.display.set_mode((500, 500))
class Map :
	
	# mapColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	def __init__(self, variable):
		self.variable = variable
		self.probability = (self.variable.mapSize * 10)
		self.currentMap = []

	def mapInit(self) :
		self.currentMap.clear()
		for i in range(self.variable.mapSize) :
			self.currentMap.append([])
			for j in range(self.variable.mapSize) :
				oneToFour = random.randint(1, (self.probability))
				if i == 0 and j == 0 :
					self.currentMap[i].append(0)
					print("Spawn created !")
				elif i == (self.variable.mapSize - 1) and j == (self.variable.mapSize - 1) and self.variable.keyNumber > 0 :
					self.currentMap[i].append(2)
					self.variable.keyNumber -= 1
				elif oneToFour < math.floor(self.probability * 0.35) :
					self.currentMap[i].append(1)
				elif oneToFour == 150 and self.variable.keyNumber > 0 :
					self.currentMap[i].append(2)
					self.variable.keyNumber -= 1
				else :
					self.currentMap[i].append(0)


	def mapDisplay(self, ecran) :
		x = 0
		for i in self.currentMap :
			y = 0
			for j in i :
				if self.currentMap[x][y] == 1 :
					pygame.draw.rect(ecran, (95, 97, 80), pygame.Rect((x*self.variable.caseSize) + 1, (y*self.variable.caseSize) + 1, (self.variable.caseSize - 1), (self.variable.caseSize - 1)))
				elif self.currentMap[x][y] == 2 :
					pygame.draw.rect(ecran, self.variable.keyColor, pygame.Rect((x*self.variable.caseSize) + 1, (y*self.variable.caseSize) + 1, (self.variable.caseSize - 1), (self.variable.caseSize - 1)))
				else :
					pygame.draw.rect(ecran, (218, 227, 150), pygame.Rect((x*self.variable.caseSize) + 1, (y*self.variable.caseSize) + 1, (self.variable.caseSize - 1), (self.variable.caseSize - 1)))
				y += 1
			x += 1






