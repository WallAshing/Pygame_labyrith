from variables import *

import pygame
import random

ecran = pygame.display.set_mode((500, 500))

map = []

# mapColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

variables = Variables()

def mapInit() :
    for i in range(variables.mapSize) :
        for j in range(variables.mapSize) :
            # if random.randint(1, 4) != 1 :
            pygame.draw.rect(ecran, (218, 227, 150), pygame.Rect((i*variables.caseSize) + 1, (j*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
            # else :
            #     pygame.draw.rect(ecran, (95, 97, 80), pygame.Rect((i*variables.caseSize) - (variables.caseSize - 1), (j*variables.caseSize) - (variables.caseSize -1), (variables.caseSize - 1), (variables.caseSize - 1)))


# def mapDisplay() : 
#     for x in map :
#         for y in map[x] :
# 			if map[x][y] == 1 :
# 				pygame.draw.rect(ecran, (95, 97, 80), pygame.Rect((i*variables.caseSize) + 1, (j*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
#             else :
#                 pygame.draw.rect(ecran, (218, 227, 150), pygame.Rect((i*variables.caseSize) + 1, (j*variables.caseSize) + 1, (variables.caseSize - 1), (variables.caseSize - 1)))
                
        





