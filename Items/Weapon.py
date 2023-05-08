class Weapon:
    usedIds = []
    idCounter = 0
    attributes = {"id": idCounter, "name": "", "value": 0}

    def __init__(self, type: str, value: int):
        self.idGenerator()
        match type:
            case "bow":
                self.attributes.update({"ar": value})
            case "sword":
                self.attributes.update({"str": value})
            case "staff":
                self.attributes.update({"int": value})

        return self.attributes.update({"name": type})

    def idGenerator(self):
        newId = len(self.usedIds) + 1
        while newId in self.usedIds:
            newId = len(self.usedIds) + 1
        self.idCounter = newId
        self.usedIds.append(newId)
        self.attributes["id"] = newId

    def showWeaponStats(self):
        stats = self.attributes
        self.deleteObject()
        return stats

    def deleteObject(self):
        self.attributes = {"id": self.idCounter, "name": "", "end": 0}

    def updateGoldValue(self, goldValue=0):
        self.attributes.update({"value": goldValue})
