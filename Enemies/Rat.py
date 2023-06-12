from Enemies.Enemy import Enemy


class Rat(Enemy):

    def attack(self, type: str):
        match type:
            case "basic":
                damageDone = self.randInt(3, 10)
                return damageDone
            case "light":
                damageDone = self.randInt(3, 5)
                return damageDone
            case "heavy":
                damageDone = self.randInt(15, 30)
                return damageDone
