characters = ["Knight", "Mage", "Rogue", "Archer",]

# name/damage pair
knightAttacks = {"Swing sword": 20, "Lance": 40}

def genAttacks(Character):
    if Character == "Knight":
        pass

class Knight:
    def __init__(self) -> None:
        self.hp = 200
        self.attacks = characters.get("Knight")
        self.isDead = False
    def takeDamage(self, damage):
        self.hp -= damage
    def useAttack():
        pass
    


# if wrong file is opened
if __name__ == "__main__":
    print("Run game.py")

