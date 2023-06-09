import random
from Enemies.Enemy import Enemy
from Npcs.Merchant import Merchant
from Player.Archer import Archer
from Player.Knight import Knight
from Player.Mage import Mage
from Player.Player import Player
from Story.Dialog import Dialog
import time

dialog = Dialog()
dialog.intro()
gameLength = random.randint(20, 50)
classes = ["knight", "mage", "archer"]
attackList = ["basic", "light", "heavy"]
enemyList = []
chooseClass = str(input("Choose your class: Knight, Mage, Archer:  ")).lower()

while chooseClass not in classes:
    print("Not a Class")
    chooseClass = input("Choose your class: Knight, Mage, Archer: ").lower()

match chooseClass:
    case "knight":
        player = Knight("knight")
    case "mage":
        player = Mage("mage")
    case "archer":
        player = Archer("archer")

merchant = Merchant(chooseClass)


def enemyGenerator():
    names = ["rat", "skeleton", "spider", "zombie"]
    for i in range(random.randint(1, 3)):
        enemyList.append(Enemy(names[random.randint(0, 3)]))


dialog.gameRule()
time.sleep(0)  # Change to 2 later
print("Type help to see all your options as a Player")


while True:
    dialog.actions()
    action = str(input()).lower()

    if action == "help":
        dialog.help()

    elif action == "game rules":
        dialog.gameRule()

    elif action == "stats":
        print(player.showPlayerStats())

    elif action == "inv":
        print(player.inventory.showInventory())

    elif action == "w":
        print("You walked forward")
        enemyGenerator()
        print("You have encountered")
        for i in range(len(enemyList)):
            print(enemyList[i].showEnemy())
        print("You are now in combat")
        print("Which mob do you want to attack? Use the number of the Mob to target ")
        target = int(input())
        print("What kind of attack do you want to use?")
        attack = input()
        if attack in attackList:
            damageDone = player.attack(attack)
        else:
            while attack not in attackList:
                print("Attack does not exist try again")
                attack = input()
        if target == enemyList[target].showEnemy("id"):
            print(player.showPlayerStats())
            enemyList[target].takeDamage(damageDone)
            print(player.showPlayerStats("end"))
            print(f"""You dealt {damageDone} damage!
{enemyList[target].showEnemy("name")} has {enemyList[target].showEnemy("hp")} HP left! 
            """)

        else:
            print("target out of range")

    elif action == "a":
        print("You walked left")
        fe = True
    elif action == "s":
        print("You walked backwards")

    elif action == "d":
        print("You walked right")

    elif action == "stop":
        print("Thansk for playing and goodbye")
        break
    else:
        print("Wrong input")
        dialog.actions()
        action = str(input())
