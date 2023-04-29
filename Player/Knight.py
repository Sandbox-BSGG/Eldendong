from Items.Healpotion import HealthPotion
from Player.Inventory import Inventory
from Items.Weapon import Weapon


class Knight():
    attributes = {
        "hp": 50,
        "end": 10,
        "dps": 0

    }

    def __init__(self):
        self.starterPotion = HealthPotion(1)
        self.starterWeapon = Weapon("sword", 10)
        self.inventory = Inventory()
        self.inventory.addItem("weapons", self.starterWeapon.showWeaponStats())
        self.inventory.addItem("potions", self.starterPotion.showPotion())
        self.updateDps(0)

    def usePotion(self, id):
        getPotion = self.inventory.showInventory("potions")
        for potion in getPotion:
            if potion.get("id") == id:
                healing = potion.get('healing')+self.attributes["hp"]
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
                f"HP: {self.attributes['hp']}\nEndurance: {self.attributes['end']}\nDPS: {self.attributes['dps']}\n")
        else:
            return self.attributes[type]

    def playerAttack(self,type:str):
        None

    def takeDamage(self, damage: int):
        newHp = self.attributes["hp"]-damage
        self.attributes.update({"hp": newHp})


Player = Knight()
for i in range(10):
    Weapons=Weapon("sword",100)
    pots=HealthPotion(1)
    Player.inventory.addItem("weapons", Weapons.showWeaponStats())
    Player.inventory.addItem("potions", pots.showPotion())

print(Player.inventory.showInventory())
