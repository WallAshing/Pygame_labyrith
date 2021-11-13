def directionToPosition(pos, direction) :
    x, y = (pos[0], pos[1])
    if direction == "North":
        y = pos[1] - 1
        return x, y
    if direction == "South":
        y = pos[1] + 1
        return x, y
    if direction == "East":
        x = pos[0] + 1
        return x, y
    if direction == "West":
        x = pos[0] - 1
        return x, y

def SupprBoxes(boxesToSuppr, boxList) :
    for boxToSuppr in boxesToSuppr :
        boxList.remove(boxToSuppr)
    boxesToSuppr.clear()

def whatsInMyBox(wallNumber, deadEndBoxes, walkedBoxes, pos) :
    if wallNumber >= 3 :
        for deadEndBox in deadEndBoxes :
            if deadEndBox == pos :
                return
        deadEndBoxes.append(pos)
    else :
        for walkedBox in walkedBoxes :
            if walkedBox == pos :
                return
        walkedBoxes.append(pos)
