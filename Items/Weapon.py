import random

class Weapon:
    usedIds=[0]
    idCounter = 0
    attributes = {
        "id": idCounter,
        "name": "",
        "end": 0
    }
    def idGenerator(self):
        newId=random.randint(1,999)
        if newId not in self.usedIds:
            self.idCounter=newId
        self.usedIds.append(newId)

    def showWeaponStats(self):
        stats=self.attributes
        self.deleteObject()
        return stats

    def initializeWeapon(self, type: str, value: int, endurance: int):
        self.idGenerator()
        match type:
            case "bow":
                self.attributes.update({"ar": value})
            case "sword":
                self.attributes.update({"str": value})
            case "staff":
                self.attributes.update({"int": value})

        self.attributes.update({"name": type})
        self.attributes.update({"end": endurance})


    def deleteObject(self):
        self.attributes=({
            "id": self.idCounter,
            "name": "",
            "end": 0
        })
