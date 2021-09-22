from variables import *

import pygame
import random

ecran = pygame.display.set_mode((500, 500))

map = []

# mapColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

variables = Variables()

def mapInit() :
    for i in range(variables.mapSize) :
					map.append([])
					for j in range(variables.mapSize) :
						if i == 0 and j == 0 :
							map[i].append(0)
							print("Spawn created !")
						elif random.randint(1, 4) != 1 :
							map[i].append(0)
						else :
							map[i].append(1)

def mapDisplay() :

	x = 0
	for i in map :
		y = 0
		for j in i :
			if map[x][y] == 1 :
				pygame.draw.rect(ecran, (95, 97, 80), pygame.Rect((x*variables.caseSize) + 1, (y*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
			else :
				pygame.draw.rect(ecran, (218, 227, 150), pygame.Rect((x*variables.caseSize) + 1, (y*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
			y += 1
		x += 1






