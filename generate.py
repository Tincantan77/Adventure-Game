import random

def randomArea(x):
    Areas = {
        1:"woodland",
        2:"grassland",
        3:"crags",
        4:"ice plains"
    }
    return Areas.get(x)

def generate():
    world = []
    for i in range (5):
        newRow = []
        for j in range (5):
            x = random.randint(1,4)
            newRow.append(randomArea(x))
        world.append(newRow)

    return world

def generateCoords():
    grid = []
    for i in range (5):
        newCoord = []
        for j in range (5):
            newCoord.append(str(j)+str(i))
        grid.append(newCoord)

    return grid