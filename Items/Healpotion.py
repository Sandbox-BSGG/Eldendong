class HealthPotion:
    usedIds = []
    idCounter = 0

    def __init__(self, level=1):
        self.attributes = {"id": self.idCounter, "name": "potion", "healing": 0, "value": 0} # sets default values
        self.idGenerator()
        match level:
            case 1:
                self.attributes.update({"healing": 30})
                self.attributes.update({"name": "Potion LVL 1"})
                self.attributes.update({"value": 20})

            case 2:
                self.attributes.update({"healing": 60})
                self.attributes.update({"name": "Potion LVL 2"})
                self.attributes.update({"value": 50})

            case 3:
                self.attributes.update({"healing": 100})
                self.attributes.update({"name": "Potion LVL 3"})
                self.attributes.update({"value": 100})

    def idGenerator(self): # generates id
        newId = len(self.usedIds) + 1
        while newId in self.usedIds:
            newId = len(self.usedIds) + 1
        self.idCounter = newId
        self.usedIds.append(newId)
        self.attributes["id"] = newId

    def showPotion(self): # returns potion
        stats = self.attributes
        return stats

    def deleteObject(self): #deletes potion
        self.attributes = {"id": self.idCounter,
                           "name": "potion", "healing": 0}
