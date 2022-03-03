import random

from descriptions import *
from area import *
from character import *
from structure import *
from item import *

worldSize = 10

#Create the world
def createWorldDict_and_Coords():
    world = {}
    coords = []
    for i in range (worldSize):
        for j in range (worldSize):
            world[str(j)+str(i)] = None
            coords.append(str(j)+str(i))
    return world, coords


#Areas
#Text - Add the names of the areas to the world dictionary
def randomArea(x):
    Areas = {
        1:"woodland",
        2:"grassland",
        3:"crags",
        4:"ice plains",
        5:"desert"
    }
    return Areas.get(x)

def generateAreaGrid():
    world = {}
    for i in range (worldSize):
        for j in range (worldSize):
            x = random.randint(1,5)
            world[str(j)+str(i)] = randomArea(x)
    return world

#Objects - Change the areas on the world from string to object
def areaObjects():

    for i in range (worldSize):
        for j in range (worldSize):
            a = str(i)+str(j)
            b = world[a]

            if b == "woodland":
                c = Area("Woodland",woodlandDescription,a)
            elif b == "grassland":
                c = Area("Grassland",grasslandDescription,a)
            elif b == "crags":
                c = Area("Crags",cragsDescription,a)
            elif b == "ice plains":
                c = Area("Ice Plains",icePlainsDescription,a)
            else:
                c = Area("Desert",desertDescription,a)

    return world

def createLinks(world):
    for i in range (worldSize):
        for j in range (worldSize):
            key = str(j)+str(i)
            northKey = str(j-1)+str(i)
            eastKey = str(j)+str(i+1)
            southKey = str(j+1)+str(i)
            westKey = str(j)+str(i-1)
            try:
                world[key].linkArea(world[northKey],"north")
            except:
                pass
            try:
                world[key].linkArea(world[eastKey],"east")
            except:
                pass
            try:
                world[key].linkArea(world[southKey],"south")
            except:
                pass
            try:
                world[key].linkArea(world[westKey],"west")
            except:
                pass


#Enemies
#Text - Generate a dictionary with the coordinates and names of the enemies to add
def randomEnemy(x):
    Enemies = {
        1:"wild boar",
        2:"lion",
        3:"troll",
        4:"goblin",
    }
    return Enemies.get(x)

def generateEnemyGrid():
    enemyGrid = {}
    for i in range (worldSize):
        for j in range(worldSize):
            x = random.randint(1,8)
            if x <= 4:
                enemyGrid[str(j)+str(i)] = randomEnemy(x)
    return enemyGrid

#Objects
def enemyObjects(world):
    for i in range(worldSize):
        for j in range(worldSize):
            a = str(j)+str(i)
            try:
                b = enemyGrid[a]
                if b == "wild boar":
                    wild_boar = Enemy("Wild Boar",wildBoarDescription,3)
                    world[a].setCharacter(wild_boar)
                if b == "lion":
                    lion = Enemy("Lion",lionDescription,4)
                    world[a].setCharacter(lion)
                if b == "troll":
                    troll = Enemy("Troll",trollDescription,6)
                    world[a].setCharacter(troll)
                if b == "goblin":
                    goblin = Enemy("Goblin",goblinDescription,2)
                    world[a].setCharacter(goblin)
            except:
                pass


#Structures
#Text
def generateStructureGrid():

    structuresGrid = {}
    
    for i in range (len(coords)):
        structuresGrid[coords[i]] = None

    for i in range(1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "castle"
    for i in range (1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "camp"
    for i in range (1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "monastery"
    for i in range (1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if structuresGrid[key] == None:
                break
        structuresGrid[key] = "cave"
    return structuresGrid

#Objects
#Initiate structure types
#Castle
def initiateCastle(a):
    #Create Structure
    castle = Structure("Castle",castleDescription,a)
    #CreateRooms
    entranceCastle = Room("Entrance",castleEntranceDescription)
    corridorCastle = Room("Corridor",castleCorridorsDescription)
    dungeonCastle = Room("Dungeon",castleDungeonsDescription)
    #Set Exit
    entranceCastle.setExit(True)
    #Create links in rooms
    entranceCastle.linkRoom(corridorCastle,"north")
    corridorCastle.linkRoom(entranceCastle,"south")
    corridorCastle.linkRoom(dungeonCastle,"east")
    dungeonCastle.linkRoom(corridorCastle,"west")
    #Add rooms to castle
    castle.setRooms(entranceCastle)
    castle.setRooms(corridorCastle)
    castle.setRooms(dungeonCastle)
    return castle
#Camp
def initiateCamp(a):
    camp = Structure("Camp",campDescription,a)
    entranceCamp = Room("Entrance",campEntranceDescription)
    camp.setRoom(entranceCamp)
    return camp
#Monastery
def initiateMonastery(a):
    monastery = Structure("Monastery",monasteryDescription,a)
    entranceMonastery = Room("Entrance",monasteryEntranceDescription)
    monastery.setRoom(entranceMonastery)
    return monastery
#Cave
def initiateCave(a):
    cave = Structure("Dungeon Entrance",caveDescription,a)
    entranceCave = Room("Entrance",caveEntranceDescription)
    cave.setRoom(entranceCave)
    return cave

#Add structures to the world
def structureObjects(world,structuresGrid):

    for i in range(worldSize):
        for j in range(worldSize):
            a = str(j)+str(i)
            try:
                b = structuresGrid[a]
                if b == "castle":
                    castle = initiateCastle(a)
                    world[a].setStructure(castle)
                    #print("Castle at: "+a)
                if b == "camp":
                    camp = initiateCamp(a)
                    world[a].setStructure(camp)
                if b == "monastery":
                    monastery = initiateMonastery(a)
                    world[a].setStructure(monastery)
                if b == "cave":
                    cave = initiateCave(a)
                    world[a].setStructure(cave)
            except:
                pass


#Items
#Text
def generateItemsGrid():

    itemsGrid = {}
    
    for i in range (len(coords)):
        itemsGrid[coords[i]] = None

    for i in range(1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if itemsGrid[key] == None:
                break
        itemsGrid[key] = "strength_potion"
    for i in range (1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if itemsGrid[key] == None:
                break
        itemsGrid[key] = "sword"
    for i in range (1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if itemsGrid[key] == None:
                break
        itemsGrid[key] = "healing_potion"
    for i in range (1):
        while True:
            x = random.randint(0,len(coords)-1)
            key = coords[x]
            if itemsGrid[key] == None:
                break
        itemsGrid[key] = "club"
    return itemsGrid

#Objects
def itemObjects(world):
    double = 0
    for i in range(worldSize):
        for j in range(worldSize):
            a = str(j)+str(i)
            try:
                b = itemsGrid[a]
                if b == "strength_potion":
                    power = random.randint(1,3)
                    strengthPotion = Potion("Strength Potion",strengthPotionDescription,"strength",power,a)
                    world[a].setItem(strengthPotion)
                    #print("strength potion: "+a)
                if b == "sword":
                    sword = Item("Sword","It's a sword",a)
                    world[a].setItem(sword)
                if b == "health_potion":
                    healthPotion = Potion("Health Potion",healthPotionDescription,a)
                    world[a].setItem(healthPotion)
                if b == "club":
                    cave = Item("Club","It's a club",a)
                    world[a].setItem(cave)
            except:
                double += 1

#Text
world, coords = createWorldDict_and_Coords()
world = generateAreaGrid()
enemyGrid = generateEnemyGrid()
structuresGrid = generateStructureGrid()
itemsGrid = generateItemsGrid()

#Objects
world = areaObjects()
createLinks(world)
enemyObjects(world)
structureObjects(world,structuresGrid)
itemObjects(world)