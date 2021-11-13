from Enemies.Enemies_Features.miscellaneous import whatsInMyBox, directionToPosition

def directionsChecker(pos, currentMap, wallNumber, newBox, walkableBox, walkedBox, deadEndBox) :
    x, y = directionToPosition(pos, "North")
    boxChecker(currentMap, x, y, wallNumber, newBox, walkableBox, walkedBox, deadEndBox)

    x, y = directionToPosition(pos, "South")
    boxChecker(currentMap, x, y, wallNumber, newBox, walkableBox, walkedBox, deadEndBox)


    x, y = directionToPosition(pos, "East")
    boxChecker(currentMap, x, y, wallNumber, newBox, walkableBox, walkedBox, deadEndBox)

    x, y = directionToPosition(pos, "West")
    boxChecker(currentMap, x, y, wallNumber, newBox, walkableBox, walkedBox, deadEndBox)

    whatsInMyBox(wallNumber, deadEndBox, walkedBox ,pos)


def boxChecker(currentMap, x, y, wallNumber, newBoxes, walkableBox, walkedBoxes, deadEndBoxes):
        if x < len(currentMap) and x >= 0 and y < len(currentMap) and y >= 0 :
            if currentMap[x][y] == 2 :
                return

            if currentMap[x][y] == 1 :
                wallNumber += 1
                return

            if currentMap[x][y] == 0 :
                for newBox in newBoxes :
                    if newBox[0] == x and newBox[1] == y :
                        walkableBox.append((x, y))
                        return
                if walkedBoxes :
                    for walkedBox in walkedBoxes :
                        if walkedBox[0] == x and walkedBox[1] == y :
                            walkableBox.append((x, y))
                            return
                if deadEndBoxes :
                    for deadEndBox in deadEndBoxes :
                        if deadEndBox[0] == x and deadEndBox[1] == y :
                            walkableBox.append((x, y))
                            return
                newBoxes.append((x, y))
                walkableBox.append((x, y))
                return
        else :
            wallNumber += 1
            return