from os import system
from player import *
from createNewMap import *
from variables import *
from mapChecker import *
from time import sleep
import pygame

variables = Variables()
ecran = pygame.display.set_mode(variables.windowSize)
map = Map(variables)
player = Player(ecran, variables, map)
mapChecker = MapChecker(map, variables)

pygame.display.set_caption("Labyrinth_2D")

loop = True

while loop : 
    ecran.fill((0, 0, 0))
    
    while mapChecker.keyNumber != 0 :
        player = Player(ecran, variables, map)
        variables.keyNumber = variables.keyInitial
        map.mapInit()
        mapChecker.mapChecker()
        sleep(1)

    if player.win == True:
        variables.keyColor = (0, 0, 255)
        map.mapDisplay(ecran)
        print("Now, it will restart forever...")
        sleep(1)
        variables.keyNumber = variables.keyInitial
        variables.keyColor = (255, 0, 0)
        player = Player(ecran, variables, map)

    for event in pygame.event.get() : 
        if event.type == pygame.KEYDOWN :
            player.move(event)
            print("x = " + str(player.casepos[0]) + " " + "y = " + str(player.casepos[1]))
            if event.key == pygame.K_ESCAPE :
                loop = False
        if event.type == pygame.K_r : 
            player.win = True
        if event.type == pygame.QUIT : 
            loop = False
    map.mapDisplay(ecran)
    rect = pygame.draw.rect(ecran, (0, 0, 255), (pygame.Rect(player.pos[0], player.pos[1], (variables.caseSize - 1), (variables.caseSize - 1))))

    pygame.display.flip()

pygame.quit()


