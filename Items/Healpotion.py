import random


class Potion:

    usedIds = [0]
    idCounter = 0
    attributes = {
        "id": idCounter,
        "name": "potion",
        "healing": 0
    }

    def idGenerator(self):
        newId = random.randint(1, 999)
        if newId not in self.usedIds:
            self.idCounter = newId
        self.usedIds.append(newId)

    def showPotion(self):
        stats = self.attributes
        self.deleteObject()
        return stats

    def newPotion(self, level):
        self.idGenerator()
        match level:
            case 1:
                self.attributes.update({"healing": 30})
                self.attributes.update({"name": "Potion LVL 1"})
            case 2:
                self.attributes.update({"healing": 60})
                self.attributes.update({"name": "Potion LVL 2"})

            case 3:
                self.attributes.update({"healing": 100})
                self.attributes.update({"name": "Potion LVL 3"})

    def deleteObject(self):
        self.attributes = ({
            "id": self.idCounter,
            "name": "potion",
            "healing": 0
        })
