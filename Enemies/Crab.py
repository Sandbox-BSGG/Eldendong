import random

class Crab:

    usedIds=[0]
    idCounter = 0
    attributes = {
        "id": idCounter,
        "hp" : 10,
        "name": f"Generic Spider {len(usedIds)}",
        "end": 10
    }
    def __init__(self):
        self.idGenerator()


    def idGenerator(self):
        newId=random.randint(1,999)
        if newId not in self.usedIds:
            self.idCounter=newId
        self.usedIds.append(newId)

    def showEnemy(self,type=None):
        if type=="" or type == None:
            print(self.attributes)
        else:
            print(self.attributes[type])

    def updateHP(self,damage: int):
        newHP= self.attributes["hp"] - damage
        return self.attributes.update({"hp":newHP})

    def attack(self,type:str):
        match type:
            case "basic":
                damageDone=10
                newEnd=self.attributes["end"]-5
                self.attributes.update({"end":newEnd})
                return damageDone
            case "heavy":
                damageDone=30
                newEnd=self.attributes["end"]-10
                self.attributes.update({"end":newEnd})
                return damageDone
            case "light":
                damageDone=3
                newEnd=self.attributes["end"]-2
                self.attributes.update({"end":newEnd})
                return damageDone