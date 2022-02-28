import random
worldSize = 10

#Map
def randomArea(x):
    Areas = {
        1:"woodland",
        2:"grassland",
        3:"crags",
        4:"ice plains"
    }
    return Areas.get(x)

def generateWorld():
    world = {}
    for i in range (worldSize):
        for j in range (worldSize):
            x = random.randint(1,4)
            world[str(j)+str(i)] = randomArea(x)
    return world

#Enemies
def randomEnemy(x):
    Enemies = {
        1:"wild boar",
        2:"lion",
        3:"troll",
        4:"goblin",
    }
    return Enemies.get(x)

def generateEnemies():
    enemiesLocations = {}
    for i in range (worldSize):
        for j in range(worldSize):
            x = random.randint(1,8)
            if x <= 4:
                enemiesLocations[str(j)+str(i)] = randomEnemy(x)
    return enemiesLocations

#Structures
def generateStructures():
    structuresGrid = {}
    coords = []
    for i in range (worldSize):
        for j in range (worldSize):
            coords.append(str(j)+str(i))
    
    for i in range (len(coords)):
        structuresGrid[coords[i]] = None

    for i in range(2):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "castle"
    for i in range (2):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "camp"
    for i in range (2):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "monastery"
    for i in range (2):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "cave"
    return structuresGrid