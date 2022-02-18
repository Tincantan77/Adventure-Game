from area import *
from generate import *

areas = generate()
grid = generateCoords()
world = {}

def createWorldDictionary():
    # for i in range (len(areas)):
    #     print(areas[i])

    for i in range (len(areas)):
        for j in range (len(areas[i])):
            a = grid[j][i]
            b = areas[j][i]

            if b == "woodland":
                c = Woodland()
            elif b == "grassland":
                c = Grassland()
            elif b == "crags":
                c = Crags()
            else:
                c = Ice_Plains()

            world[a] = c
    return world


def createLinks(world):
    for i in range (len(areas)):
        for j in range (len(areas[i])):
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

world = createWorldDictionary()
createLinks(world)

current_area = world["22"]
while True:
    print("\n")
    current_area.getDetails()
    
    command = input("> ")
    current_area = current_area.move(command)
    print("this is to test the repository")