class Character():

    def __init__(self,char_name,char_description):
        self.Name = char_name
        self.Description = char_description
        self.Conversation = None
        self.IsEnemy = False

    def getIsEnemy(self):
        return(self.IsEnemy)

    def getName(self):
        return(self.Name)
    
    def getDescription(self):
        return(self.Description)


class Enemy(Character):

    def __init__(self,char_name,char_description,enemy_strength):
        super().__init__(char_name,char_description)
        self.Strength = enemy_strength
        self.IsEnemy = True

    def getStrength(self):
        return(self.Strength)

    def printDetails(self):
        print("There is a "+self.Name+" here")
        print(self.Description)
        print("It has a strength of: "+str(self.Strength))
        print("It is aggressive")