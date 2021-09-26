from os import system
from player import *
from createNewMap import *
from variables import *
from mapChecker import *
from ennemis import *
import pygame

variables = Variables()
ennemi = Ennemis(variables)
ecran = pygame.display.set_mode(variables.windowSize)
map = Map(variables)
player = Player(ecran, variables, map)
mapChecker = MapChecker(map, variables)

pygame.display.set_caption("Labyrinth_2D")
pygame.font.init()

loop = True

font = pygame.font.SysFont('Arial', 30)

while loop : 
    ecran.fill((0, 0, 0))
    yourScore = font.render("Score : " + str(variables.winNumber), True, (255, 255, 255))
    scoreRect = yourScore.get_rect()
    scoreRect.center = (variables.windowSize[0] // 2, 20)


    while mapChecker.keyNumber != 0 :
        variables.keyNumber = variables.keyInitial
        map.mapInit()
        ennemi.ennemiInit()
        player = Player(ecran, variables, map)
        mapChecker.mapChecker()

    if player.win == True:
        variables.keyColor = (0, 255, 0)
        map.mapDisplay(ecran)
        variables.keyNumber = variables.keyInitial
        variables.keyColor = (0, 0, 255)
        mapChecker.keyNumber = variables.keyInitial
        player = Player(ecran, variables, map)

    for event in pygame.event.get() : 
        if event.type == pygame.KEYDOWN :
            player.move(event)
            if event.key == pygame.K_ESCAPE :
                loop = False
        if event.type == pygame.K_r : 
            player.win = True
        if event.type == pygame.QUIT : 
            loop = False
    
    map.mapDisplay(ecran)
    rect = pygame.draw.rect(ecran, (0, 255, 0), (pygame.Rect(player.pos[0], player.pos[1], (variables.caseSize - 1), (variables.caseSize - 1))))
    # Fait apparaître les ennemis
    # ennemi.ennemiDisplay(ecran) 
    # ennemi.ennemiMove()
    ecran.blit(yourScore, scoreRect)
    pygame.display.flip()

pygame.quit()


