from Items.Healpotion import Potion
from Items.Weapon import Weapon
from Player.Inventory import Inventory

inv = Inventory()
wp= Weapon()
stopper=input("Break!")
while True:
    wp.initializeWeapon("sword",10,100)
    inv.addItem("weapons",wp.showWeaponStats())
    wp.initializeWeapon("bow",10,100)
    inv.addItem("weapons",wp.showWeaponStats())
    wp.initializeWeapon("staff",10,100)
    inv.addItem("weapons",wp.showWeaponStats())
    inv.showInventory()
    stopper=input("Break!")
    if stopper=="del":
        inv.deleteItem("weapons",0)