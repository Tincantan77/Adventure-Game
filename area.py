class Woodland():

    def __init__(self):
        self.LinkedAreas = {}
        self.Name = "Woodland"
        self.Description = "A dense, dark forest with huge gnarled trees\n"

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
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

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
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

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
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

    def getName(self):
        return self.Name

    def getDescription(self):
        return self.Description

    def getDetails(self):
        print(self.Name)
        print("=============")
        print(self.Description)
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