import os
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

from Player.Inventory import Inventory
from Items.Weapon import Weapon
import random


inv = Inventory()
wp = Weapon()
wp.initializeWeapon("bow",random.randint(1,100),10)
item=wp.showWeaponStats()
inv.addItem("weapons",item)
inv.showInventory()
wp.deleteObject()
inv.showInventory()