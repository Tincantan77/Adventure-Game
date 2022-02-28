import random
import time
import keyboard

from area import *
from generate import *
from structure import *
from character import *
from descriptions import *

world = generateWorld()
enemiesGrid = generateEnemies()
structuresGrid = generateStructures()

#Change the names in the world dictionary to objects
def addObjectsToDict():

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
            else:
                c = Area("Ice Plains",icePlainsDescription,a)
            world[a] = c

    return world

#Create links between areas on the map
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

#Add the enemies to random areas
def addEnemiesToWorld(world):
    for i in range(worldSize):
        for j in range(worldSize):
            a = str(j)+str(i)
            try:
                b = enemiesGrid[a]
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


#Create Structures, add rooms to the structures and create the links
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
def addStructuresToWorld(world):

    for i in range(worldSize):
        for j in range(worldSize):
            a = str(j)+str(i)
            try:
                b = structuresGrid[a]
                if b == "castle":
                    castle = initiateCastle(a)
                    world[a].setStructure(castle)
                    print("Castle at: "+a)
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



#Enemy
def checkEnemy(current_area,upDateLives):
    inhabitant = current_area.getCharacter()
    if inhabitant != None:
        inhabitant.printDetails()
        if inhabitant.getIsEnemy() == True:
            fight = input("Would you like to fight?: ")
            if fight == "Yes" or fight == "yes":
                upDateLives = fightEnemy(inhabitant,current_area,upDateLives)
    else:
        upDateLives = Lives
    return upDateLives, inhabitant


def fightEnemy(inhabitant,current_area,upDateLives):
    print()
    time.sleep(0.5)
    print("You have chosen to fight it")
    print()
    time.sleep(0.5)
    battleStrength = (Strength)+(random.randint(1,6))
    enemyBattleStrength = (inhabitant.getStrength())+(random.randint(1,6))
    print("Your battle strength: ",battleStrength)
    time.sleep(1.0)
    print("The "+inhabitant.getName()+"'s battle strength: "+str(enemyBattleStrength))
    print()
    time.sleep(0.5)
    if battleStrength > enemyBattleStrength:
        print("You defeated the "+inhabitant.getName())
        current_area.setCharacter(None)
        upDateLives = Lives
    elif battleStrength == enemyBattleStrength:
        print("You didn't manage to defeat the "+inhabitant.getName()+" but you got away unharmed")
        upDateLives = Lives
    else:
        upDateLives -= 1
        if upDateLives == 0:
            print("You were killed by the "+inhabitant.getName())
        else:
            print("The "+inhabitant.getName()+" bested you in battle")
            print("You managed to get away before it could do any further harm")

    return upDateLives


#Structure
def checkStructure(current_area):
    structure_here = current_area.getStructure()
    if structure_here != None:
        structure_here.printDetails()
        enter = input("Would you like to enter?: ")
        if enter == "Yes" or enter == "yes":
            canLeave = False
            enter = insideStructure(structure_here,canLeave)

def insideStructure(structure_here,canLeave):
    print("You enter")
    print()
    current_room = structure_here.getFirstRoom()
    roomCommand = "not_exit"
    while True:
        print()
        current_room.printDetails()
        current_room.printLinks()
        canLeave = current_room.getExit()
        roomCommand = input("move > ")
        if canLeave == True and roomCommand == "exit":
            print("leaving")
            break
        else:
            print("Moving Room")
            current_room = current_room.move(roomCommand)
    print()
    current_area.printDetails()



world = addObjectsToDict()
createLinks(world)
addEnemiesToWorld(world)
addStructuresToWorld(world)

current_area = world[str(worldSize//2)+str(worldSize//2)]
current_area = world["00"]

Lives = 3
Strength = 2

while Lives > 0:
    print("===============")
    print("Strength: "+str(Strength))
    print("Lives: "+str(Lives))
    print("===============")
    current_area.printDetails()
    print()
    Lives, inhabitant = checkEnemy(current_area,Lives)
    checkStructure(current_area)
    print()
    current_area.printLinks()
    
    keyboard.add_hotkey('up', lambda: keyboard.write("north", 0.1))
    keyboard.add_hotkey('down', lambda: keyboard.write("south",0.1))
    keyboard.add_hotkey('right', lambda: keyboard.write("east",0.1))
    keyboard.add_hotkey('left', lambda: keyboard.write("west",0.1))
    
    command = input("> ")
    current_area = current_area.move(command,current_area,world)