from Player.player import *
from Map.createNewMap import *
from variables import *
from Map.mapChecker import *
from Ennemis.ennemis import *
import pygame
import time

variables = Variables()
ecran = pygame.display.set_mode(variables.windowSize)
createMap = createNewMap(variables)
player = Player(ecran, variables, createMap)
mapChecker = MapChecker(createMap, variables)
ennemis = Ennemis(variables, createMap)

pygame.display.set_caption("Labyrinth_2D")
pygame.font.init()

loop = True

font = pygame.font.SysFont('Arial', 30)

# Fait apparaître les ennemis
ennemis.ennemisInit()

while loop : 
    ecran.fill((0, 0, 0))
    yourScore = font.render("Score : " + str(variables.winNumber), True, (255, 255, 255))
    scoreRect = yourScore.get_rect()
    scoreRect.center = (variables.windowSize[0] // 2, 20)
    # print(time.localtime()) la loop est lu 570 fois par secondes, pas mal les fps


    while mapChecker.keyNumber != 0 :
        variables.keyNumber = variables.keyInitial
        createMap.mapInit()
        ennemis = Ennemis(variables, createMap)
        ennemis.ennemisInit()
        player = Player(ecran, variables, createMap)
        mapChecker.mapChecker()

    if player.win == True:
        variables.keyColor = (0, 255, 0)
        createMap.mapDisplay(ecran)
        variables.keyNumber = variables.keyInitial
        variables.keyColor = (0, 0, 255)
        mapChecker.keyNumber = variables.keyInitial
        player = Player(ecran, variables, createMap)

    for event in pygame.event.get() : 
        if event.type == pygame.KEYDOWN :
            player.move(event)
            if event.key == pygame.K_ESCAPE :
                loop = False
            if event.key == pygame.K_r :
                player.win = True
            if event.key == pygame.K_p :
                time.sleep(100)
        if event.type == pygame.QUIT : 
            loop = False
    
    createMap.mapDisplay(ecran)
    rect = pygame.draw.rect(ecran, (0, 255, 0), (pygame.Rect(player.pos[0], player.pos[1], (variables.caseSize - 1), (variables.caseSize - 1))))

    ennemis.ennemisMove()
    ennemis.ennemisDisplay(ecran)

    ecran.blit(yourScore, scoreRect)
    pygame.display.flip()

pygame.quit()


