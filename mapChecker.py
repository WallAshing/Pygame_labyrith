class MapChecker : 
    def __init__(self, createNewMap) :
        self.createNewMap = createNewMap
        self.boxToCheck = self.createNewMap.currentMap
        self.checkedBox = []

    # def findBoxToCheck(self) :
    #     for x in self.createNewMap.currentMap :
    #         for y in x :
    #             if y != 1 :
    #                 self.boxToCheck.append((x, y))
    #     print(self.boxToCheck)


    def checkerInit(self) :
        self.findBoxToCheck()



# Faire 2 listes 
# Liste n°1 => contient les blocs tester
# Liste n°2 => contient les blocs à tester
# Tester les cases une par une si il est possible de se déplacer sur les cases adjacentes
# Si le bloc à tester est vide et que je suis pas passer au-dessus de la clé c'est qu'il faut reset
# Si je trouve la clé, le niveau est bon
# Le test de déplacement fait les 4 directions à chaque fois
# Si la position est déjà dans la liste des blocs tester on skip sinon on check si c'est accessible si oui on met dans tester sinon on la met pas
# C'est clairement une réaction en chaine.