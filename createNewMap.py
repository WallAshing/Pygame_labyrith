from variables import *

import pygame
import random

ecran = pygame.display.set_mode((500, 500))

variables = Variables()

map = []
class Map :

	# mapColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	def mapInit(self) :
		for i in range(variables.mapSize) :
						map.append([])
						for j in range(variables.mapSize) :
							oneToFour = random.randint(1, 32)
							if i == 0 and j == 0 :
								map[i].append(0)
								print("Spawn created !")
							elif oneToFour < 9:
								map[i].append(1)
							elif oneToFour == 10 and variables.keyNumber > 0:
								map[i].append(2)
								variables.keyNumber -= 1
							else :
								map[i].append(0)

	def mapDisplay(self, ecran) :
		x = 0
		for i in map :
			y = 0
			for j in i :
				if map[x][y] == 1 :
					pygame.draw.rect(ecran, (95, 97, 80), pygame.Rect((x*variables.caseSize) + 1, (y*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
				elif map[x][y] == 2 :
					pygame.draw.rect(ecran, (255, 0, 0), pygame.Rect((x*variables.caseSize) + 1, (y*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
				else :
					pygame.draw.rect(ecran, (218, 227, 150), pygame.Rect((x*variables.caseSize) + 1, (y*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
				y += 1
			x += 1






