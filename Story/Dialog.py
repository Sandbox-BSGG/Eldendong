
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
        
    def help(self):
        print("""
        As the player you have the following commands:
        General commands:

        game rules / Shows you the game rules,
        stats / Shows your currents statistics,
        inv / Shows your inventory,
        sell / sell an item to the merchant for gold
        buy / buy an item from the merchant with gold
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
        Welcome to Eldendong.
        This game is a hardocre turned based game,
        Death means everything is lost,
        There are no savefiles,
    
        Your objective is to defeat the last boss to win the game.
        On your journey to the last boss you will encounter other enemies,
        when fighting these enemies you always start first,
        you can do actions until your endurance is 0 or you wish to end your turn
        """)