from os import system

from player import *
from createNewMap import *
from variables import *
import pygame
import random

player = Player(ecran)
variables = Variables()

pygame.display.set_caption("Labyrinth_2D")

ecran = pygame.display.set_mode(variables.windowSize)
loop = True

mapInit()
print(map)

while loop : 
    ecran.fill((0, 0, 0))
    mapDisplay()
    # print(random.randint(0, 4))
    rect = pygame.draw.rect(ecran, (0, 0, 255), (pygame.Rect(player.pos[0], player.pos[1], (variables.caseSize - 1), (variables.caseSize - 1))))
    for event in pygame.event.get() : 
        if event.type == pygame.KEYDOWN :
            player.move(event)
            print("x = " + str(player.casepos[0]) + " " + "y = " + str(player.casepos[1]))
            if event.key == pygame.K_ESCAPE :
                loop = False
        if event.type == pygame.QUIT : 
            loop = False
    
    pygame.display.flip()

pygame.quit()


