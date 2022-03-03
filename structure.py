class Structure():

    def __init__(self,structure_name,structure_description,structure_location):
        self.Name = structure_name
        self.Description = structure_description
        self.Rooms = []
        self.Location = structure_location
    
    #Getters
    def getName(self):
        return (self.Name)

    def getDescription(self):
        return (self.Description)

    def getFirstRoom(self):
        return (self.Rooms)[0]

    def getLocation(self):
        return self.Location

    def printDetails(self):
        print("You find a "+self.Name)
        print("===============")
        print(self.Description)
        print()

    #Setters
    def setRooms(self,newRoom):
        (self.Rooms).append(newRoom)

class Room():

    def __init__(self,room_name,room_description):
        self.Name = room_name
        self.Description = room_description
        self.LinkedRooms = {}
        self.Item = None
        self.Character = None
        self.Exit = False

    #Getters
    def getCharacter(self):
        return (self.Character)

    def getItem(self):
        return (self.Item)

    def getName(self):
        return (self.Name)

    def getExit(self):
        return (self.Exit)

    def printDetails(self):
        print(self.Name)
        print("===============")
        print(self.Description)

    def printLinks(self):
        for direction in self.LinkedRooms:
            room = self.LinkedRooms[direction]
            checkNamePlural = room.getName()
            if checkNamePlural[len(checkNamePlural)-1] != "s":
                print("The "+room.getName()+" is "+direction)
            else:
                print("The "+room.getName()+" are "+direction)
        if self.Exit == True:
            print("Type 'exit' to leave")

    #Setters
    def setItem(self,newItem):
        self.Item = newItem

    def setCharacter(self,newCharacter):
        self.Character = newCharacter

    def linkRoom(self,new_linked_room,direction):
        self.LinkedRooms[direction] = new_linked_room

    def setExit(self,new_exit):
        self.Exit = new_exit

    #Gameplay
    def move(self,direction):
        compass = ["north","south","east","west"]
        if direction in self.LinkedRooms:
            return self.LinkedRooms[direction]
        elif direction not in compass:
            print("That is not a valid direction")
        else:
            print("That is a wall, you are not a ghost")
        return self