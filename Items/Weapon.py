class Weapon:
    idCounter = 0
    attributes = {
        "id": idCounter,
        "name": "",
        "end": 0
    }

    def showWeaponStats(self):
        return self.attributes

    def initializeWeapon(self, type: str, value: int, endurance: int):
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
        self.attributes.update({
            "id": self.idCounter,
            "name": "",
            "end": 0
        })
