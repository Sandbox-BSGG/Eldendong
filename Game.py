import random
from Enemies.Rat import Rat
from Enemies.Skeleton import Skeleton
from Enemies.Spider import Spider
from Enemies.Zombie import Zombie
from Npcs.Merchant import Merchant
from Player.Archer import Archer
from Player.Knight import Knight
from Player.Mage import Mage
from Story.Dialog import Dialog
import time


def choosePlayer(chooseClass):  # Chooses class
    match chooseClass:
        case "knight":
            return Knight("knight")
        case "mage":
            return Mage("mage")
        case "archer":
            return Archer("archer")


def randomNumber(start, end):
    return random.randint(start, end)


def enemyGenerator(mobsMin=None, mobsMax=None):  # Generates enemies
    names = ["rat", "skeleton", "spider", "zombie"]
    xp = 0
    gold = 0

    scaling = 0
    currentLvl = player.showPlayerStats("lvl")
    for lvl in range(int(currentLvl)):  # Scales enemies with player lvl
        scaling += 1

    if mobsMin == None and mobsMax == None:
        mobsMin = 2 + scaling
        mobsMax = 5 + scaling

    # Random ammount of enemies, and random names
    for i in range(randomNumber(mobsMin, mobsMax)):
        randonName = names[randomNumber(0, 3)]
        match randonName:
            case "rat":
                ratNames = ["squeaky rat", "nimble rodent", "cheeky vermin"]
                enemyList.append(Rat(ratNames[randomNumber(0, 2)]))
            case "skeleton":
                skeletonNames = ["creepy skeleton",
                                 "bone rattler", "undead warrior"]
                enemyList.append(Skeleton(skeletonNames[randomNumber(0, 2)]))
            case "spider":
                spiderNames = ["venomous spider",
                               "web weaver", "eight-legged menace"]
                enemyList.append(Spider(spiderNames[randomNumber(0, 2)]))
            case "zombie":
                zombieNames = ["rotting corpse",
                               "flesh eater", "undead monstrosity"]
                enemyList.append(Zombie(zombieNames[randomNumber(0, 2)]))
        xp += 10
        gold += 20
    return xp, gold


def healing():  # uses potion and heals the player
    print(player.inventory.showInventory("potions"))
    while True:
        potion = input("Choose your potion: ").lower()
        try:
            int(potion)
            player.usePotion(potion)
            break

        except (ValueError, IndexError):
            continue


def loot(xpAndGold):  # reward for killing every enemy
    print(f"You received {xpAndGold[0]} XP")
    print(f"You received {xpAndGold[1]} Gold")
    player.addStat("xp", xpAndGold[0])
    player.inventory.addGold(xpAndGold[1])
    print(player.lvlUp())
    player.nextRound()
    player.addStat("hp", 200)


def combatEncounter(mobsMin=None, mobsMax=None):  # Combat systen of the game
    chooseTarget = True  # Bool for choosing the target
    inCombat = True  # bool combat
    nextTurn = False  # bool for turn of player and enemy
    notEnoughEnd = True  # bool for player when endurance hits 0
    xpAndGold = enemyGenerator(mobsMin, mobsMax)  # returns xp and gold

    dialog.inCombat()
    time.sleep(0.3)
    while inCombat:
        # Looks for player endurance
        if player.showPlayerStats("end") > 1 and nextTurn == False:
            dialog.encounter()
            dialog.lineBreak()
            for i in range(len(enemyList)):

                print(enemyList[i].showEnemy("name"))
                dialog.lineBreak()
            dialog.chooseMob()
            dialog.lineBreak()

            while chooseTarget:  # choosing target
                target = input("Player Combat: ").lower()
                try:
                    target = int(target)
                    for enemy in enemyList:
                        if target == enemy.showEnemy("id"):
                            chooseTarget = False
                        else:
                            continue
                except (ValueError, IndexError):
                    dialog.Nan()

            chooseTarget = True
            time.sleep(0.3)
            dialog.chooseAttack()
            dialog.lineBreak()
            attack = input("Player: ").lower()

            while attack not in attackList:  # choosing attack
                movementAction(attack)
                attack = input("Player: ").lower()

            while notEnoughEnd:  # looks for player endurance, checks if player has enough endurance for the attack
                if attack not in attackList:
                    dialog.attackInvalid()
                    attack = input("Player: ").lower()

                elif attack == "light" and player.showPlayerStats("end") < 2:
                    dialog.lineBreak()
                    dialog.noEnd()
                    attack = input("Player: ").lower()

                elif attack == "basic" and player.showPlayerStats("end") < 4:
                    dialog.lineBreak()
                    dialog.noEnd()
                    attack = input("Player: ").lower()

                elif attack == "heavy" and player.showPlayerStats("end") < 8:
                    dialog.lineBreak()
                    dialog.noEnd()
                    attack = input("Player: ").lower()

                else:
                    notEnoughEnd = False

            notEnoughEnd = True

            damageDone = player.attack(attack)
            damageDone += player.showPlayerStats("dps")
            print(
                f"You have {player.showPlayerStats('end')} endurance remaining")
            for enemy in enemyList:
                if target == enemy.showEnemy("id"):
                    enemy.takeDamage(damageDone)
                    print(
                        f"You dealt {damageDone} damage!\n{enemy.showEnemy('name')} has {enemy.showEnemy('hp')} HP left!")
                    dialog.lineBreak()
                    if enemy.showEnemy("hp") == 0:
                        enemyList.remove(enemy)

            if len(enemyList) == 0: # Reward after every enemy is dead
                dialog.lineBreak()  

                dialog.allDead()
                dialog.lineBreak()
                loot(xpAndGold)
                nextTurn = True
                inCombat = False
            else:  # Player can end turn
                if player.showPlayerStats("end") >= 1:
                    turn = input("Do you want to end turn? Y/N: ").lower()
                    if turn == "y" or turn == "yes":
                        nextTurn = True
                else:
                    dialog.turnOver()
                    nextTurn = True

        elif inCombat == True:  # Enemies now attack the player
            for enemy in enemyList:
                if player.showPlayerStats("hp") <= 0:  # Dead if 0
                    dialog.dead()
                    inCombat = False
                    break
                enemyDamage = enemy.attack(
                    attackList[randomNumber(0, 2)])  # Random attack
                player.takeDamage(enemyDamage)
                print(f"{enemy.showEnemy('name')} dealt {enemyDamage} to you!")
                dialog.lineBreak()
                print(f"You have {player.showPlayerStats('hp')} HP remaining")
                dialog.lineBreak()
                time.sleep(1)
            nextTurn = False  # Player turn next
            player.nextRound()


def merchantEncounter():  # Shop
    inShop = True

    while inShop:
        dialog.merchantShop()
        time.sleep(0.3)
        weapons = merchant.inventory.showInventory("weapons")
        potions = merchant.inventory.showInventory("potions")
        for weapon in weapons:  # prints weapons
            print(
                f"ID: {weapon['id']}  Name: {weapon['name']}  Gold value: {weapon['value']}  Damage: {weapon['dps']}"
            )
            time.sleep(0.1)
        print("\n")
        for potion in potions:  # prints potions
            print(
                f"ID: {potion['id']}  Name: {potion['name']}  Gold value: {potion['value']}  Healing: {potion['healing']}"
            )
            time.sleep(0.1)
        print("\n")
        dialog.merchantAction()
        buyOrSell = input("Shop action: ").lower()

        if buyOrSell == "buy":  # buy weapon or potions
            dialog.merchantBuy()
            dialog.lineBreak()
            category = input("Shop action: ").lower()
            while category not in shopCategories:  # checks category
                dialog.merchantBuy()
                dialog.lineBreak()
                category = input("Shop action: ").lower()
            dialog.idToBuy()
            item = input("Shop action: ").lower()
            try:  # Try to buy the item
                playerGold = player.inventory.showInventory("gold")
                newItem = merchant.itemBought(category, item, int(playerGold))
                if newItem == 0:  # Player has no gold
                    dialog.noGold()
                    time.sleep(0.4)
                else:  # buy item
                    player.inventory.addItem(category, newItem)
                    player.inventory.subtractGold(newItem["value"])
                    if category == "weapons":
                        print(
                            f"You bought a {newItem['name']} with {newItem['dps']} DPS! "
                        )
                        dialog.weaponEqiupped()
                        # equips the new weapon
                        player.updateDps(newItem["id"])
                        time.sleep(1)
                    elif category == "potions":
                        print(
                            f"You bought a {newItem['name']} with {newItem['healing']} healing! "
                        )

            except:  # throws error
                dialog.somethingWentWrong()

        elif buyOrSell == "sell":  # sell weapons or potions
            itemsToSell = False  # Bool if you have something to sell
            dialog.merchantSell()
            category = input("Shop action: ")
            forbiddenId = 0  # Currently equipped weapon
            if category == "weapons":
                dialog.WeaponNotShownInShop()

                for weapon in player.inventory.showInventory("weapons"):

                    # Checks for your current weapon
                    if weapon["dps"] == player.showPlayerStats("dps"):
                        forbiddenId = weapon["id"]

                    # Your other weapons
                    elif weapon["dps"] != player.showPlayerStats("dps"):
                        itemsToSell = True
                        print(weapon)

                if itemsToSell:
                    dialog.idToSell()
                    sellWeaponId = input("Shop action: ")
                    try:
                        if forbiddenId != sellWeaponId:
                            sellItem = player.inventory.showInventory(
                                "weapons", int(sellWeaponId))
                            player.inventory.addGold(sellItem["value"])
                            player.inventory.deleteItem(
                                "weapons", sellWeaponId)
                            print(
                                f"You now have {player.inventory.showInventory('gold')} Gold")
                    except:
                        dialog.somethingWentWrong()
                else:
                    dialog.nothingToSell()

            elif category == "potions":
                potionToSell = False
                potionIndex = 0  # Looks if you have more than 0 potions
                for i in player.inventory.showInventory("potions"):
                    potionIndex += 1
                dialog.yourPotions()
                for potion in player.inventory.showInventory("potions"):
                    if potionIndex > 0:
                        print(potion)
                        potionToSell = True
                if potionToSell:
                    dialog.idToSell()
                    sellPotionId = input("Shop action: ")

                    try:
                        sellPotion = player.inventory.showInventory(
                            "potions", int(sellPotionId))
                        player.inventory.addGold(sellPotion["value"])
                        player.inventory.deleteItem("potions", sellPotionId)
                        print(
                            f"You now have {player.inventory.showInventory('gold')} Gold")

                    except:
                        dialog.somethingWentWrong()
                else:
                    dialog.nothingToSell()

            else:
                dialog.somethingWentWrong()

        elif buyOrSell == "leave":
            inShop = False

        elif buyOrSell not in attackList:
            movementAction(buyOrSell)
            time.sleep(1)


def switchWeapon():  # Switch your weapon
    dialog.yourWeapons()
    for weapon in player.inventory.showInventory("weapons"):
        print(weapon)
    dialog.equipWeapon()
    equipWeapon = input("Action: ")
    try:
        player.updateDps(int(equipWeapon))
    except:
        dialog.somethingWentWrong()


def worldEncounter():  # Generates random world event
    worldAction = randomNumber(0, 20)
    if worldAction >= 0 and worldAction <= 6:
        combatEncounter()  # Combat encounter
    elif worldAction >= 18:
        merchantEncounter()  # Shop
    else:
        dialog.noEncounter()


def movementAction(action):  # Player movement
    if action == "help":
        dialog.help()

    elif action == "game rules":
        dialog.gameRule()

    elif action == "stats":
        print(player.showPlayerStats())

    elif action == "inv":
        print(player.inventory.showInventory())

    elif action == "help":
        dialog.help()

    elif action == "heal":
        healing()

    elif action == "switch":
        switchWeapon()

    elif action == "w":
        dialog.actionW()
        dialog.lineBreak()
        worldEncounter()

    elif action == "a":
        dialog.actionA()
        dialog.lineBreak()
        worldEncounter()

    elif action == "s":
        dialog.actionS()
        dialog.lineBreak()
        worldEncounter()

    elif action == "d":
        dialog.actionD()

        dialog.lineBreak()
        worldEncounter()


    elif action == "stop":
        dialog.stop()
        dialog.lineBreak()
        time.sleep(3)
        exit()


# Game
dialog = Dialog()
dialog.intro()
gameLength = randomNumber(20, 50)
stepper = 0
classes = ["knight", "mage", "archer"]
attackList = ["basic", "light", "heavy"]
enemyList = []
shopCategories = ["weapons", "potions"]
chooseClass = str(input("Choose your class: Knight, Mage, Archer:  ")).lower()
chooseTarget = True

while chooseClass not in classes:
    print("Not a Class")
    chooseClass = input("Choose your class: Knight, Mage, Archer: ").lower()

merchant = Merchant(chooseClass)
player = choosePlayer(chooseClass)
dialog.gameRule()
time.sleep(2)
dialog.notifyHelp()

while player.showPlayerStats("hp") > 0:
    dialog.actions()
    dialog.lineBreak()
    action = str(input("Player: ")).lower()
    movementAction(action)
    stepper += 1
    if stepper >= gameLength:
        dialog.enterBoss()
    if action == "boss":
        combatEncounter(20, 40)
        dialog.stop()
        time.sleep(3)
        exit()
