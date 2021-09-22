
class Variables :
    def __init__(self) :
        self.mapSize = 10
        self.windowSize = (500 // self.mapSize * self.mapSize, 500 // self.mapSize * self.mapSize)
        self.caseSize = self.windowSize[0] / self.mapSize
        self.keyNumber = 1

# Faire 2 listes 
# Liste n°1 => contient les blocs tester
# Liste n°2 => contient les blocs à tester
# Tester les cases une par une si il est possible de se déplacer sur les cases adjacentes
# Si bloc à tester est vide et que je suis pas passer au dessus de la clé c'est qu'il faut reset
# Si je trouve la clé, le niveau est bon
# Le test de déplacement fait les 4 directions à chaque fois
# Si la position est déjà dans la liste des blocs tester on skip sinon on check si c'est accessible si oui on met dans tester sinon on la met pas
# C'est clairement une réaction en chaine.



