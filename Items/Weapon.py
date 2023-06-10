class Weapon:
    usedIds = []
    idCounter = 0
    attributes = {"id": idCounter, "name": "", "value": 0}

    def __init__(self, type: str, value: int):
        self.idGenerator()
        self.attributes.update({"dps": value})
        if value-30 <= 0:
            self.attributes.update({"value": 0})
        else:
            self.attributes.update({"value": value-30})

        return self.attributes.update({"name": type})

    def idGenerator(self):
        newId = len(self.usedIds) + 1
        while newId in self.usedIds:
            newId = len(self.usedIds) + 1
        self.idCounter = newId
        self.usedIds.append(newId)
        self.attributes["id"] = newId

    def showWeaponStats(self, type=None):
        stats = self.attributes
        self.deleteObject()
        if type == None:
            return stats
        elif type == "id":
            return stats["id"]

    def deleteObject(self):
        self.attributes = {"id": self.idCounter, "name": "", "end": 0}

    def updateGoldValue(self, goldValue=0):
        self.attributes.update({"value": goldValue})
