# Pour installer le jeu :
Il faut installer python :
https://www.python.org

Puis installer pygame :
```Bash
pip install pygame
```

## Pour jouer :
Pour lancer le jeu vous devez ouvrir un terminal à la racine du projet.

En suite la commande pour lancer le jeu est :
```Bash
python main.py
```

Votre joueur est un carré vert et son but et de récupérer la clé de fin de niveau (le carré bleu) afin de s'échapper de se térrible labirinth. Mais malheuresement le labyrinth n'est qu'un test élaboré par des extraterrestes sournois qui ne vous laisserons jamais sortir.

---

# Pour le code :
## Player :

Il n'y a que le fichier **player.py** pour l'instant qui s'occupe donc des movements du joueurs, de son affichage, de récupérer la position du joueur et de l'évènement "Niveau terminé". 

## Map :

Il y a 2 fichiers :
 - **createNewMap** qui s'occupe de créé des cartes aléatoire avec la clé à l'opposé du joueur et d'afficher la carte
 - **mapChecker** qui s'occuper de vérifier si la carte créé est gagnable, sinon demande à **createNewMap** de re-créé une carte.

## Ennemis :

Il y a 3 fichiers :
- **\__init__.py** qui permet au fichier **main.py** d'appeller les fichiers du dossier ennemis.
- **ennemi.py** qui regroupe toutes les actions et comportements d'un ennemi.
- **ennemis.py** qui appelle autant d'ennemis que necessaire, les affiches, initialise leurs premières positions et liste leurs positions actuels.



## Variables :

Variables changeable :
- self.mapSize (default=25)
- self.windowSize (default=(500, 500))
- self.keyColor (default=(0, 0, 255))
- self.ennemiNumber (default=1)
