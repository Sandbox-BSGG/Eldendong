from Items.Healpotion import HealthPotion
from Player.Inventory import Inventory
from Items.Weapon import Weapon


class Knight:
    attributes = {"hp": 50, "end": 10, "dps": 0, "lvl": 1}

    def __init__(self):
        self.starterPotion = HealthPotion(1)
        self.starterWeapon = Weapon("sword", 10)
        self.inventory = Inventory()
        self.inventory.addItem("weapons", self.starterWeapon.showWeaponStats())
        self.inventory.addItem("potions", self.starterPotion.showPotion())
        self.updateDps(1)

    def usePotion(self, id):
        getPotion = self.inventory.showInventory("potions")
        for potion in getPotion:
            if potion.get("id") == id:
                healing = potion.get("healing") + self.attributes["hp"]
                self.attributes.update({"hp": healing})
                result = f"healing {potion.get('healing')}"
                self.inventory.deleteItem("potions", 0)

                return result

    def updateDps(self, id):
        getWeapon = self.inventory.showInventory("weapons")
        for weapon in getWeapon:
            if weapon.get("id") == id:
                newDps = weapon["str"]
                self.attributes.update({"dps": newDps})

    def showPlayerStats(self, type=None):
        if type == "" or type == None:
            print(
                f"HP: {self.attributes['hp']}\nEndurance: {self.attributes['end']}\nDPS: {self.attributes['dps']}\n"
            )
        else:
            return self.attributes[type]

    def playerAttack(self, type: str):
        match type:
            case "basic":
                damageDone = 10
                newEnd = self.attributes["end"] - 5
                self.attributes.update({"end": newEnd})
                return damageDone
            case "light":
                damageDone = 3
                newEnd = self.attributes["end"] - 2
                self.attributes.update({"end": newEnd})
                return damageDone
            case "heavy":
                damageDone = 30
                newEnd = self.attributes["end"] - 10
                self.attributes.update({"end": newEnd})
                return damageDone

    def takeDamage(self, damage: int):
        newHp = self.attributes["hp"] - damage
        self.attributes.update({"hp": newHp})

    def sellItem(self, id):
        None

    def changeWeapon(self, id):
        None
