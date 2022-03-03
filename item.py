class Item():

    def __init__(self,item_name,item_description,item_location):

        self.Name = item_name
        self.Description = item_description
        self.Location = item_location

    
    def printDetails(self):
        print(self.Name)
        print("===============")
        print(self.Description)

class Potion(Item):

    def __init__(self,item_name,item_description,potion_effect,potion_power,item_location):
        super().__init__(item_name,item_description,item_location)
        self.Effect = potion_effect
        self.Power = potion_power
        self.Type = "Potion"

    def getEffect(self):
        return self.Effect

    def getPower(self):
        return self.Power

    
    def printDetails(self):
        print(self.Name)
        print("===============")
        print(self.Description)
        print("Restores: "+str(self.Power)+" "+self.Effect)
