

class HealthPotion:

    usedIds = []
    idCounter = 0
    attributes = {
        "id": idCounter,
        "name": "potion",
        "healing": 0
    }

    def __init__(self, level=1):
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

    def idGenerator(self):
        newId = len(self.usedIds) + 1
        while newId in self.usedIds:
            newId = len(self.usedIds) + 1
        self.idCounter = newId
        self.usedIds.append(newId)
        self.attributes["id"] = newId

    def showPotion(self):
        stats = self.attributes
        return stats

    def deleteObject(self):
        self.attributes = ({
            "id": self.idCounter,
            "name": "potion",
            "healing": 0
        })
