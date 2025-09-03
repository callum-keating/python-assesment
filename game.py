import os, sys, msvcrt, random
import uiCode

characters = ["Scavenger", "Medic", "Veteran", "Hunter", "Illusionist"]
def getChar(msg:str, printChar:bool = True):
    print(msg, end='', flush=True)
    char = msvcrt.getch()
    if char == b'\x03':
        os.write(sys.stdout.fileno(), b"\033[?1049l")
        os.write(sys.stdout.fileno(), b"\033[?25h")
        quit()
    try:
        char = char.decode("utf-8")
    except:
        char = ""
    if printChar:
        print(char)
    
    return char
class Scavenger:
    def __init__(self):
        self.hp = 100
        self.originalHp = self.hp
        self.attacks = [
            {"name": "Makeshift Blade", "damage": 7, "accuracy": 90},
            {"name": "Rock Throw", "damage": 5, "accuracy": 80},
            {"name": "Tripwire", "damage": 8, "accuracy": 75},
            {"name": "Molotov", "damage": 10, "accuracy": 65},
            {"name": "Slingshot", "damage": 6, "accuracy": 85},
            {"name": "Explosive Barrel", "damage": 20, "accuracy": 60, "backfire": {"chance": 40}}
        ]

class Medic:
    def __init__(self):
        self.hp = 90
        self.originalHp = self.hp
        self.attacks = [
            {"name": "Syringe Stab", "damage": 7, "accuracy": 85},
            {"name": "Medical Saw", "damage": 9, "accuracy": 80},
            {"name": "Poison Dart", "damage": 8, "accuracy": 75},
            {"name": "Defibrillator Shock", "damage": 12, "accuracy": 60},
            {"name": "Adrenaline Rush", "damage": 10, "accuracy": 70},
            {"name": "Toxic Overdose", "damage": 20, "accuracy": 60, "backfire": {"chance": 40}}
        ]

class Veteran:
    def __init__(self):
        self.hp = 120
        self.originalHp = self.hp
        self.attacks = [
            {"name": "Shoot", "damage": 10, "accuracy": 95},
            {"name": "Grenade", "damage": 11, "accuracy": 70},
            {"name": "Bayonet Charge", "damage": 8, "accuracy": 80},
            {"name": "Knife Throw", "damage": 9, "accuracy": 75},
            {"name": "Rifle Bash", "damage": 7, "accuracy": 90},
            {"name": "Airstrike", "damage": 20, "accuracy": 60, "backfire": {"chance": 40}}
        ]

class Hunter:
    def __init__(self):
        self.hp = 110
        self.originalHp = self.hp
        self.attacks = [
            {"name": "Track", "damage": 6, "accuracy": 85},
            {"name": "Ambush", "damage": 12, "accuracy": 70},
            {"name": "Trap", "damage": 9, "accuracy": 80},
            {"name": "Snipe", "damage": 14, "accuracy": 60},
            {"name": "Camouflage", "damage": 8, "accuracy": 75},
            {"name": "Beast Lure", "damage": 20, "accuracy": 60, "backfire": {"chance": 40}}
        ]

class Illusionist:
    def __init__(self):
        self.hp = 95
        self.originalHp = self.hp
        self.attacks = [
            {"name": "Phantom Strike", "damage": 10, "accuracy": 75},
            {"name": "Mind Twist", "damage": 7, "accuracy": 85},
            {"name": "Spectral Slash", "damage": 8, "accuracy": 80},
            {"name": "Ethereal Blast", "damage": 12, "accuracy": 65},
            {"name": "Hallucination", "damage": 9, "accuracy": 70},
            {"name": "Shadow Rend", "damage": 20, "accuracy": 75, "backfire": {"chance": 40}},
        ]

class Enemy:
    def __init__(self,player):
        self.play = player
    def takeDamage(self, damage):
        self.play.hp -= damage
    def getHp(self):
        return self.play.hp
    def getInstanceType(self):
        return self.play
    def getAttacks(self):
        return self.play.attacks
    def getOriginalHp(self):
        return self.play.originalHp
    def zeroHp(self):
        self.play.hp = 0

class Player:
    def __init__(self,player):
        self.play = player
    def takeDamage(self, damage):
        self.play.hp -= damage
    def getHp(self):
        return self.play.hp
    def getInstanceType(self):
        return self.play
    def getAttacks(self):
        return self.play.attacks
    def getOriginalHp(self):
        return self.play.originalHp
    def zeroHp(self):
       self.play.hp = 0


def enemyAttack(enemy:Enemy,player:Player):
    attack = random.choice(enemy.getAttacks())
    if random.randint(1, 100) <= attack['accuracy']:
        player.takeDamage(attack['damage'])
        if player.getHp() <= 50:
            if player.getHp() < 0:
                player.zeroHp()
            print(f"Enemy uses {attack['name']} your health is now \033[31m{player.getHp()}\033[0m", flush=True)
        else:
            print(f"Enemy uses {attack['name']} your health is now {player.getHp()}", flush=True)
    else:
        if 'backfire' in attack:
            enemy.takeDamage(attack['damage'])
            print(f"Enemys attack backfired enemy took {attack['damage']} damage.", flush=True)
        else:
            print(f"Enemy missed attack with {attack['name']}", flush=True)

def main():
    os.system("cls")
    os.write(sys.stdout.fileno(), b"\033[?25l")
    characterOptions = random.sample(characters, 4)
    print("choose a character")
    char = uiCode.makeList(characterOptions, showInfo=True) + 1
    character_name = characterOptions[char - 1]

    os.system("cls")
    print(f"You selected: \033[32m{character_name}\033[0m")

    char_class_map = {
        "Scavenger": Scavenger,
        "Medic": Medic,
        "Veteran": Veteran,
        "Hunter": Hunter,
        "Illusionist": Illusionist
    }
    player = Player(char_class_map[character_name]())

    enemy_choices = [c for c in characterOptions if c != character_name]
    enemy_character_name = random.choice(enemy_choices)
    enemyPlayer = Enemy(char_class_map[enemy_character_name]())
    print(f"Your enemy is: \033[31m{enemy_character_name}\033[0m")
    getChar("press any key to continue")


    while True:
        os.system("cls")
        attacks = random.sample(player.getAttacks(), 3)
        print("Your attack options:")
        attacksList = []
        for attack_number, attack in enumerate(attacks, 1):
            attack_str = f"{attack['name']} (Damage: \033[31m{attack['damage']}\033[0m, Accuracy: \033[32m{attack['accuracy']}%\033[0m)"
            if 'backfire' in attack:
                attack_str += f" \033[1m\033[31m[{attack['backfire']['chance']}% chance to backfire]\033[0m"
            attacksList.append(attack_str)
        selected = uiCode.makeList(attacksList, highlight=False) + 1

        chosen_attack = attacks[selected - 1]
        print(f"You selected: {chosen_attack['name']}")
        accuracy = chosen_attack['accuracy']
        if random.randint(1, 100) <= accuracy:
            enemyPlayer.takeDamage(chosen_attack['damage'])
            if enemyPlayer.getHp() <= 50:
                if enemyPlayer.getHp() < 0:
                    enemyPlayer.zeroHp()
                print(f"enemys health is now at \033[31m{enemyPlayer.getHp()}\033[0m")
            else:
                print(f"enemys health is now at {enemyPlayer.getHp()}")
        else:
            print("attack missed ", end="")
            if 'backfire' in chosen_attack:
                player.takeDamage(chosen_attack['damage'])
                print(f"\033[31mYour attack backfired!, your health is now at: \033[1m{player.getHp()}\033[0m")
            else:
                print("")

        if player.getHp() == 0:
            return
        enemyAttack(enemyPlayer, player)

        originalHp = player.getOriginalHp()
        currentHp = player.getHp()

        remaining = "\033[32m" + "." * currentHp

        lost = "\033[31m" + "." * (originalHp - currentHp)

        print_str = remaining + lost + "\033[0m"
        print(" " * int(len(print_str) / 2 - 11) + "your health")
        print(print_str)

        originalHp = enemyPlayer.getOriginalHp()
        currentHp = enemyPlayer.getHp()

        remaining = "\033[32m" + "." * currentHp

        lost = "\033[31m" + "." * (originalHp - currentHp)

        print_str = remaining + lost + "\033[0m"
        print(" " * int(len(print_str) / 2 - len("enemys health")) + "enemys health")
        print(print_str)
        sys.stdout.flush()
        getChar("press any key to enter next round")
        if player.getHp() <= 0:
            uiCode.looseScreen()
            break
        elif enemyPlayer.getHp() <= 0:
            uiCode.winScreen()
            break


if __name__ == "__main__":
    os.write(sys.stdout.fileno(), b"\033[?1049h")
    main()
    getChar('press any key to quit')
    os.write(sys.stdout.fileno(), b"\033[?1049l")
    os.write(sys.stdout.fileno(), b"\033[?25h")
