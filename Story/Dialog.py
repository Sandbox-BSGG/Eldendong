
class Dialog:
    def tutorial(self):
        print("""You can perform the following actions """)

    def intro(self):
        print(
            """
EEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLL             DDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNDDDDDDDDDDDDD             OOOOOOOOO     NNNNNNNN        NNNNNNNN        GGGGGGGGGGGGG
E::::::::::::::::::::EL:::::::::L             D::::::::::::DDD   E::::::::::::::::::::EN:::::::N       N::::::ND::::::::::::DDD        OO:::::::::OO   N:::::::N       N::::::N     GGG::::::::::::G
E::::::::::::::::::::EL:::::::::L             D:::::::::::::::DD E::::::::::::::::::::EN::::::::N      N::::::ND:::::::::::::::DD    OO:::::::::::::OO N::::::::N      N::::::N   GG:::::::::::::::G
EE::::::EEEEEEEEE::::ELL:::::::LL             DDD:::::DDDDD:::::DEE::::::EEEEEEEEE::::EN:::::::::N     N::::::NDDD:::::DDDDD:::::D  O:::::::OOO:::::::ON:::::::::N     N::::::N  G:::::GGGGGGGG::::G
  E:::::E       EEEEEE  L:::::L                 D:::::D    D:::::D E:::::E       EEEEEEN::::::::::N    N::::::N  D:::::D    D:::::D O::::::O   O::::::ON::::::::::N    N::::::N G:::::G       GGGGGG
  E:::::E               L:::::L                 D:::::D     D:::::DE:::::E             N:::::::::::N   N::::::N  D:::::D     D:::::DO:::::O     O:::::ON:::::::::::N   N::::::NG:::::G
  E::::::EEEEEEEEEE     L:::::L                 D:::::D     D:::::DE::::::EEEEEEEEEE   N:::::::N::::N  N::::::N  D:::::D     D:::::DO:::::O     O:::::ON:::::::N::::N  N::::::NG:::::G
  E:::::::::::::::E     L:::::L                 D:::::D     D:::::DE:::::::::::::::E   N::::::N N::::N N::::::N  D:::::D     D:::::DO:::::O     O:::::ON::::::N N::::N N::::::NG:::::G    GGGGGGGGGG
  E:::::::::::::::E     L:::::L                 D:::::D     D:::::DE:::::::::::::::E   N::::::N  N::::N:::::::N  D:::::D     D:::::DO:::::O     O:::::ON::::::N  N::::N:::::::NG:::::G    G::::::::G
  E::::::EEEEEEEEEE     L:::::L                 D:::::D     D:::::DE::::::EEEEEEEEEE   N::::::N   N:::::::::::N  D:::::D     D:::::DO:::::O     O:::::ON::::::N   N:::::::::::NG:::::G    GGGGG::::G
  E:::::E               L:::::L                 D:::::D     D:::::DE:::::E             N::::::N    N::::::::::N  D:::::D     D:::::DO:::::O     O:::::ON::::::N    N::::::::::NG:::::G        G::::G
  E:::::E       EEEEEE  L:::::L         LLLLLL  D:::::D    D:::::D E:::::E       EEEEEEN::::::N     N:::::::::N  D:::::D    D:::::D O::::::O   O::::::ON::::::N     N:::::::::N G:::::G       G::::G
EE::::::EEEEEEEE:::::ELL:::::::LLLLLLLLL:::::LDDD:::::DDDDD:::::DEE::::::EEEEEEEE:::::EN::::::N      N::::::::NDDD:::::DDDDD:::::D  O:::::::OOO:::::::ON::::::N      N::::::::N  G:::::GGGGGGGG::::G
E::::::::::::::::::::EL::::::::::::::::::::::LD:::::::::::::::DD E::::::::::::::::::::EN::::::N       N:::::::ND:::::::::::::::DD    OO:::::::::::::OO N::::::N       N:::::::N   GG:::::::::::::::G
E::::::::::::::::::::EL::::::::::::::::::::::LD::::::::::::DDD   E::::::::::::::::::::EN::::::N        N::::::ND::::::::::::DDD        OO:::::::::OO   N::::::N        N::::::N     GGG::::::GGG:::G
EEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNNDDDDDDDDDDDDD             OOOOOOOOO     NNNNNNNN         NNNNNNN        GGGGGG   GGGG
""")  # http://www.network-science.de/ascii/ , font: doh

    def notifyHelp(self):
        print("Type help to see all your options as a Player")

    def help(self):
        print("""
        As the player you have the following commands:
        General commands:

        game rules / Shows you the game rules,
        stats / Shows your currents statistics,
        inv / Shows your inventory,
        buy / buy an item from the merchant with gold
        sell / sell an item to the merchant for gold

        switch / switch out your current weapon
        stop / ends the game

        Combat:
        light / attack deals light damage
        basic / attack deals moderate damage
        heavy / attack deals heavy damage
        heal / use healing potion form inventory


        """)

    def actions(self):
        print("Where do yo want to walk? W A S D / or type help: ")

    def gameRule(self):
        print("""
        Welcome to Elden Dong.
        This game is a hardcore turn based game,
        Death means everything is lost,
        There are no savefiles,
        Everytime you move the map changes!
        Walking back will result in a new room or a new encounter
    
        Your objective is to reach the boss room and to beat it.
        On your journey to the last boss you will encounter other enemies,
        when fighting these enemies you always start first,
        you can do actions until your endurance is 0 or you wish to end your turn
        """)

    def actionW(self):
        print("You walked forward")
        
    def actionA(self):
        print("You walked left")

    def actionS(self):
        print("You walked backwards")

    def actionD(self):
        print("You walked right")

    def stop(self):
        print("Thanks for playing and goodbye")

    def inCombat(self):
        print("You are now in combat")

    def encounter(self):
        print("You have encountered")

    def chooseMob(self):
        print("Which mob do you want to attack? Use the number of the Mob to target ")

    def chooseAttack(self):
        print("What kind of attack do you want to use? / help")

    def Nan(self):
        print("Not a number or out of range")

    def attackInvalid(self):
        print("Attack does not exist try again")

    def allDead(self):
        print("You have killed every enemy!")

    def noEnd(self):
        print("Not enough Endurance!")

    def turnOver(self):
        print("No Endurance turn ended")

    def dead(self):
        print("YOU DIED")

    def merchantShop(self):
        print("You have encountered a Merchants shop!")
        print("IMPORTANT: This Merchant will disappear if you leave his shop")

    def merchantAction(self):
        print("Do you want to buy or sell something? buy / sell / leave / help")

    def merchantBuy(self):
        print("What do you want to buy? weapons / potions")

    def merchantSell(self):
        print("What do you want to sell? weapons / potions")

    def idToBuy(self):
        print("Type in the ID of the Item you want to buy")

    def idToSell(self):
        print("Type in the ID of the Item you want to sell")

    def weaponEqiupped(self):
        print("Your new Weapon is now equipped")

    def noGold(self):
        print("Not enough gold!")

    def somethingWentWrong(self):
        print("Something went wrong try again!")

    def yourWeapons(self):
        print("These are your weapons")
        
    def WeaponNotShownInShop(self):
        print("Your currently equipped weapon wont be shown in the list")

    def nothingToSell(self):
        print("You have nothing to sell")

    def yourPotions(self):
        print("These are your potions")

    def equipWeapon(self):
        print("Type in the id of the weapon you want to equip!")

    def enterBoss(self):
        print("You can now enter the boss arena!")
        print("Type boss to enter the boss arena")

    def noEncounter(self):
        print("This place seems to be empty, keep walking")

    def lineBreak(self):
        print("\n")