class Woodland():

    def __init__(self):
        self.LinkedAreas = {}
        self.Name = "Woodland"
        self.Description = "A dense, dark forest with huge gnarled trees\n"
        self.Structure = None

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
        if self.Structure != None:
            print("There is a "+self.Structure+" here\n")
            enter = input("Would you like to enter?")
            if enter == "Yes" or enter == "yes":
                return True
        for direction in self.LinkedAreas:
            area = self.LinkedAreas[direction]
            checkNamePlural = area.getName()
            if checkNamePlural[len(checkNamePlural)-1] != "s":
                print("The "+area.getName()+" is "+direction)
            else:
                print("The "+area.getName()+" are "+direction)

    #Setters
    def linkArea(self,area_to_link,direction):
        self.LinkedAreas[direction] = area_to_link

    def setStructure(self,newStructure):
        self.Structure = newStructure

    #Game Play
    def move(self,direction):
        compass = ["north","south","east","west"]
        if direction in self.LinkedAreas:
            return self.LinkedAreas[direction]
        elif direction not in compass:
            print("That is not a valid direction")
        else:
            print("You have reached the end of the world, there is nothing out there but void")
        return self

class Crags():

    def __init__(self):
        self.LinkedAreas = {}
        self.Name = "Crags"
        self.Description = "A large collection of jagged rocks sticking up towards the sky\n"
        self.Structure = None

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
        if self.Structure != None:
            print("There is a "+self.Structure+" here\n")
            enter = input("Would you like to enter?")
            if enter == "Yes" or enter == "yes":
                return True
        for direction in self.LinkedAreas:
            area = self.LinkedAreas[direction]
            checkNamePlural = area.getName()
            if checkNamePlural[len(checkNamePlural)-1] != "s":
                print("The "+area.getName()+" is "+direction)
            else:
                print("The "+area.getName()+" are "+direction)

    #Setters
    def linkArea(self,area_to_link,direction):
        self.LinkedAreas[direction] = area_to_link

    def setStructure(self,newStructure):
        self.Structure = newStructure

    #Game Play
    def move(self,direction):
        compass = ["north","south","east","west"]
        if direction in self.LinkedAreas:
            return self.LinkedAreas[direction]
        elif direction not in compass:
            print("That is not a valid direction")
        else:
            print("You have reached the end of the world, there is nothing out there but void")
        return self

class Ice_Plains():

    def __init__(self):
        self.LinkedAreas = {}
        self.Name = "Ice Plains"
        self.Description = "Bitter wastelands of snow and ice\n"
        self.Structure = None

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
        if self.Structure != None:
            print("There is a "+self.Structure+" here\n")
            enter = input("Would you like to enter?")
            if enter == "Yes" or enter == "yes":
                return True
        for direction in self.LinkedAreas:
            area = self.LinkedAreas[direction]
            checkNamePlural = area.getName()
            if checkNamePlural[len(checkNamePlural)-1] != "s":
                print("The "+area.getName()+" is "+direction)
            else:
                print("The "+area.getName()+" are "+direction)

    #Setters
    def linkArea(self,area_to_link,direction):
        self.LinkedAreas[direction] = area_to_link

    def setStructure(self,newStructure):
        self.Structure = newStructure

    #Game Play
    def move(self,direction):
        compass = ["north","south","east","west"]
        if direction in self.LinkedAreas:
            return self.LinkedAreas[direction]
        elif direction not in compass:
            print("That is not a valid direction")
        else:
            print("You have reached the end of the world, there is nothing out there but void")
        return self

class Grassland():

    def __init__(self):
        self.LinkedAreas = {}
        self.Name = "Grassland"
        self.Description = "A barren plain of golden yellow grass\n"
        self.Structure = None

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
        if self.Structure != None:
            print("There is a "+self.Structure+" here\n")
            enter = input("Would you like to enter?")
            if enter == "Yes" or enter == "yes":
                return True
        for direction in self.LinkedAreas:
            area = self.LinkedAreas[direction]
            checkNamePlural = area.getName()
            if checkNamePlural[len(checkNamePlural)-1] != "s":
                print("The "+area.getName()+" is "+direction)
            else:
                print("The "+area.getName()+" are "+direction)

    #Setters
    def linkArea(self,area_to_link,direction):
        self.LinkedAreas[direction] = area_to_link

    def setStructure(self,newStructure):
        self.Structure = newStructure

    #Game Play
    def move(self,direction):
        compass = ["north","south","east","west"]
        if direction in self.LinkedAreas:
            return self.LinkedAreas[direction]
        elif direction not in compass:
            print("That is not a valid direction")
        else:
            print("You have reached the end of the world, there is nothing out there but void")
        return self

class Area():

    def __init__(self,area_name,area_description,area_location):
        self.LinkedAreas = {}
        self.Name = area_name
        self.Description = area_description
        self.Structure = None
        self.Character = None
        self.Location = area_location

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getCharacter(self):
        return(self.Character)

    def getStructure(self):
        return(self.Structure)

    def printDetails(self):
        print(self.Name)
        print("===============")
        print(self.Description)

    def printLinks(self):
        # if self.Structure != None:
        #     print("There is a "+self.Structure+" here\n")
        #     enter = input("Would you like to enter?")
        #     print()
        #     if enter == "Yes" or enter == "yes":
        #         return True
        for direction in self.LinkedAreas:
            area = self.LinkedAreas[direction]
            checkNamePlural = area.getName()
            if checkNamePlural[len(checkNamePlural)-1] != "s":
                print("The "+area.getName()+" is "+direction)
            else:
                print("The "+area.getName()+" are "+direction)

    #Setters
    def linkArea(self,area_to_link,direction):
        self.LinkedAreas[direction] = area_to_link

    def setStructure(self,newStructure):
        self.Structure = newStructure

    def setCharacter(self,newCharacter):
        self.Character = newCharacter

    #Game Play
    def move(self,direction,current_area,world):
        compass = ["north","south","east","west"]
        if direction in self.LinkedAreas:
            return self.LinkedAreas[str(direction)]
        elif direction not in compass:
            try:
                current_area = world[direction]
            except:
                print("That is not a valid direction")
        else:
            print("You have reached the end of the world, there is nothing out there but void")
        return self