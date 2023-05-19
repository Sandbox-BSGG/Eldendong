import random


class Enemy:

    usedIds = [0]
    idCounter = 0
    attributes = {
        "id": idCounter,
        "hp": 10,
        "end": 10
    }

    def __init__(self, name=""):
        self.idGenerator()
        self.attributes.update({"name": f"{name} {len(self.usedIds)}"})

    def idGenerator(self):
        newId = len(self.usedIds) + 1
        while newId in self.usedIds:
            newId = len(self.usedIds) + 1
        self.idCounter = newId
        self.usedIds.append(newId)
        self.attributes["id"] = newId

    def showEnemy(self, type=None):
        if type == "" or type == None:
            return (self.attributes)
        else:
            return (self.attributes[type])

    def takeDamage(self, damage: int):
        newHP = self.attributes["hp"] - damage
        return self.attributes.update({"hp": newHP})

    def randInt(self, start=0, end=10):
        return random.randint(start, end)

    def nextRound(self):
        self.attributes.update({"end": 10})
