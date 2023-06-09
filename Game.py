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
boolTarget = True

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


def combatEncounter():
    boolTarget = True
    inCombat = True
    enemyGenerator()

    print("You are now in combat")
    while inCombat:
        print("You have encountered")
        for i in range(len(enemyList)):
            print(enemyList[i].showEnemy("name"))
        print("Which mob do you want to attack? Use the number of the Mob to target ")
        while boolTarget:
            target = input("Player: ")
            try:
                target = int(target)
                for enemy in enemyList:
                    if target == enemy.showEnemy("id"):
                        boolTarget = False
                    else:
                        continue
            except (ValueError, IndexError):
                print("Not a number or out of range")
        boolTarget = True
        print("What kind of attack do you want to use? / help")
        attack = ""
        while attack not in attackList:
            attack = input("Player First: ")
            if attack == "help":
                dialog.help()
                attack = input("Player Second: ")
            elif attack == "heal":
                print(player.inventory.showInventory("potions"))
                while True:
                    potion = input("Choose your potion: ")
                    try:
                        int(potion)
                        player.usePotion(potion)
                        break

                    except (ValueError, IndexError):
                        continue
            else:
                print("Attack does not exist try again")
                attack = input("Player Third: ")
        damageDone = player.attack(attack)
        for enemy in enemyList:
            if target == enemy.showEnemy("id"):
                enemy.takeDamage(damageDone)
                print(f"""You dealt {damageDone} damage!
{enemy.showEnemy("name")} has {enemy.showEnemy("hp")} HP left! 
                """)
                if enemy.showEnemy("hp") == 0:
                    enemyList.remove(enemy)
        if len(enemyList) == 0:
            print("You have killed every enemy!")
            inCombat = False


dialog.gameRule()
time.sleep(0)  # Change to 2 later
dialog.notifyHelp()


while True:
    dialog.actions()
    action = str(input("Player: ")).lower()

    if action == "help":
        dialog.help()

    elif action == "game rules":
        dialog.gameRule()

    elif action == "stats":
        print(player.showPlayerStats())

    elif action == "inv":
        print(player.inventory.showInventory())

    elif action == "w":
        dialog.actionW()
        combatEncounter()

    elif action == "a":
        dialog.actionA()
    elif action == "s":
        dialog.actionS()
    elif action == "d":
        dialog.actionD()
    elif action == "stop":
        dialog.stop()
        break
