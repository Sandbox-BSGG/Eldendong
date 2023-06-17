import random


class Enemy:

    usedIds = []
    idCounter = 0

    def __init__(self, name=""):
        self.attributes = {
            "id": self.idCounter,
            "hp": 10,
            "end": 10,
            }

        self.idGenerator()
        self.attributes.update({"name": f"{name} {self.idCounter}"})

    def idGenerator(self): # Generates id
        newId = len(self.usedIds)
        while newId in self.usedIds:
            newId = len(self.usedIds) + 1
        self.idCounter = newId
        self.usedIds.append(newId)
        self.attributes["id"] = newId

    def showEnemy(self, type=None): # returns enemy attributes
        if type == "" or type == None:
            return (self.attributes)
        else:
            return (self.attributes[type])

    def takeDamage(self, damage: int): # enemy takes damage
        newHP = self.attributes["hp"] - damage
        if damage> newHP:
            return self.attributes.update({"hp": 0}) 
        return self.attributes.update({"hp": newHP})

    def randInt(self, start=0, end=10): # random number
        return random.randint(start, end)