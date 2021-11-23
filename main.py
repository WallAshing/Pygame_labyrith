from Player.player import *
from Map.createNewMap import *
from Map.mapChecker import *
from Map.items import *
from variables import *
from Enemies.enemies import *
import pygame

variables = Variables()
ecran = pygame.display.set_mode(variables.windowSize)
createMap = createNewMap(variables)
items = Items(ecran, variables, createMap)
player = Player(ecran, variables, createMap, items)
mapChecker = MapChecker(createMap, variables)
ennemies = Enemies(ecran, variables, createMap)
def init():
    pygame.font.init()
    pygame.display.set_caption("Labyrinth_2D")
    ennemies.ennemiesInit()
init()
font = pygame.font.SysFont('Arial', 30)
loop = True


while loop : 
    ecran.fill((0, 0, 0))
    yourScore = font.render("Score : " + str(variables.winNumber), True, (255, 255, 255))
    scoreRect = yourScore.get_rect()
    scoreRect.center = (variables.windowSize[0] // 2, 20)
    player.movingCooldown()

    while mapChecker.keyNumber != 0 :
        variables.keyNumber = variables.keyInitial
        createMap.mapInit()
        ennemies = Enemies(ecran, variables, createMap)
        ennemies.ennemiesInit()
        items = Items(ecran, variables, createMap)
        items.itemsInit()
        mapChecker.mapChecker()
        
        player = Player(ecran, variables, createMap, items)
        
    if player.win == True:
        variables.keyColor = (0, 255, 0)
        createMap.mapDisplay(ecran)
        variables.keyNumber = variables.keyInitial
        variables.keyColor = (0, 0, 255)
        mapChecker.keyNumber = variables.keyInitial
        player = Player(ecran, variables, createMap, items)

    if player.move(player) == False :
        loop = False

    createMap.mapDisplay(ecran)    
    player.playerDisplay()
    ennemies.ennemies()
    items.itemsDisplay()

    ecran.blit(yourScore, scoreRect)
    pygame.display.flip()

pygame.quit()


