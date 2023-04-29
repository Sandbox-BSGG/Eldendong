from Items.Healpotion import HealthPotion
from Player.Inventory import Inventory
from Items.Weapon import Weapon

class Knight:
    attributes = {
        "hp": 50,
        "end": 10,
        "dps": 0

    }

    def __init__(self):
        self.starterPotion= HealthPotion(3)
        self.starterWeapon= Weapon("sword",10)
        self.inventory = Inventory()
        self.inventory.addItem("weapons",self.starterWeapon.showWeaponStats())
        self.inventory.addItem("potions",self.starterPotion.showPotion())


    def usePotion(self):
        None
    
    def playerAttack(self):
        None
    
    def takeDamage(self):
        None

    def showPlayerInventory(self,type=None):
        return self.inventory.showInventory(type)

print("test")

k=Knight()

a=k.showPlayerInventory()
print(a)