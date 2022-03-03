import random
import time

from area import *
from generate import *
from structure import *
from character import *
from descriptions import *
from item import *


def ending(x):
    print()
    time.sleep(x)

#GamePlay
#Enemy
def checkEnemy(current_area,upDateLives):
    inhabitant = current_area.getCharacter()
    if inhabitant != None:
        print()
        inhabitant.printDetails()
        if inhabitant.getIsEnemy() == True:
            fight = input("Would you like to fight?: ")
            if fight == "Yes" or fight == "yes":
                upDateLives = fightEnemy(inhabitant,current_area,upDateLives)
                ending(0.1)
    else:
        upDateLives = Lives
    return upDateLives, inhabitant

def fightEnemy(inhabitant,current_area,upDateLives):
    ending(0.1)
    print("You have chosen to fight it")
    ending(0.5)
    battleStrength = (Strength)+(random.randint(1,6))
    enemyBattleStrength = (inhabitant.getStrength())+(random.randint(1,6))
    print("Your battle strength: ",battleStrength)
    ending(0.5)
    print("The "+inhabitant.getName()+"'s battle strength: "+str(enemyBattleStrength))
    ending(0.5)
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
    time.sleep(1)
    structure_here = current_area.getStructure()
    if structure_here != None:
        print()
        structure_here.printDetails()
        enter = input("Would you like to enter?: ")
        if enter == "Yes" or enter == "yes":
            canLeave = False
            enter = insideStructure(structure_here,canLeave)
        ending(0.1)
    return structure_here

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


#Item
def checkItem(current_area,upDateLives,upDateStrength):
    item_here = current_area.getItem()
    upDateLives = Lives
    upDateStrength = Strength
    if item_here != None:
        print()
        item_here.printDetails()
        use = input("Would you like to use it?: ")
        if use == "Yes" or use == "yes":
            upDateLives, upDateStrength = useItem(item_here,upDateStrength)
            ending(0.1)
    return item_here, upDateLives, upDateStrength

def useItem(item_here,upDateStrength):
    if item_here.Type == "Potion":
        print("You drink the potion")
        ending(0.1)
        if item_here.getEffect() == "strength":
            upDateStrength += item_here.getPower()
        elif item_here.getEffect() == "lives":
            upDateLives += item_here.getPower()
    return Lives, upDateStrength



current_area = world[str(worldSize//2)+str(worldSize//2)]
current_area = world["55"]

print(world)

Lives = 3
Strength = 2
inventory = 5

while Lives > 0:
    print()
    print("\n===============")
    print("Strength: "+str(Strength))
    print("Lives: "+str(Lives))
    print("===============")
    current_area.printDetails()

    Lives, inhabitant = checkEnemy(current_area,Lives)
    item_here, Lives, Strength = checkItem(current_area,Lives,Strength)
    structure_here = checkStructure(current_area)

    current_area.printLinks()
    command = input("> ")
    current_area = current_area.move(command,current_area,world)
    time.sleep(0.2)