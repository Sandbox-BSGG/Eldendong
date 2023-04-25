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

    def showEnemy(self):
        print(self.attributes)

    def updateHP(self,damage: int):
        newHP= self.attributes["hp"] - damage
        return self.attributes.update({"hp":newHP})

    def attack(self,type:str):
        match type:
            case "basic":
                damageDone=10
                self.attributes.update({"end":5})
                return damageDone





crab=Crab()
crab.showEnemy()
crab.updateHP(5)
pr=crab.attack("basic")
print(pr)
crab.showEnemy()
