import os, sys, msvcrt, random


characters = ["Scavenger", "Medic", "Veteran", "Hunter", "Illusionist"]
def getChar(msg:str, printChar:bool = True):
    print(msg, end='', flush=True)
    char = msvcrt.getch()
    try:
        char = char.decode("utf-8")
    except:
        char = ""
    if printChar:
        print(char)
    return char
def panic(errorMsg:str):
    print("panic: ", errorMsg)
    quit()

class Scavenger:
    def __init__(self):
        self.hp = 100
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
        self.attacks = [
            {"name": "Shoot", "damage": 10, "accuracy": 95},
            {"name": "Grenade", "damage": 13, "accuracy": 70},
            {"name": "Bayonet Charge", "damage": 8, "accuracy": 80},
            {"name": "Knife Throw", "damage": 9, "accuracy": 75},
            {"name": "Rifle Bash", "damage": 7, "accuracy": 90},
            {"name": "Airstrike", "damage": 20, "accuracy": 60, "backfire": {"chance": 40}}
        ]

class Hunter:
    def __init__(self):
        self.hp = 110
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
        self.attacks = [
            {"name": "Phantom Strike", "damage": 10, "accuracy": 75},
            {"name": "Mind Twist", "damage": 7, "accuracy": 85},
            {"name": "Spectral Slash", "damage": 8, "accuracy": 80},
            {"name": "Ethereal Blast", "damage": 12, "accuracy": 65},
            {"name": "Hallucination", "damage": 9, "accuracy": 70},
            {"name": "Shadow Rend", "damage": 11, "accuracy": 75},
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



def main():
    os.system("cls")
    os.write(sys.stdout.fileno(), b"\033[?25l")
    characterOptions = random.sample(characters, 4)
    print("characters: ", characterOptions)
    char = getChar("press Number 1-4: ")
    if not char.isnumeric():
        panic("Input is not an integer. make sure you type a number not character name!")
    char = int(char)
    if char < 1:
        panic("Number can not be less than 1")
    if char > 4:
        panic("character doesn't exist, was your number to large")
    character_name = characterOptions[char - 1]

    os.system("cls")
    print("You selected ", character_name)

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
    print(f"Your enemy is: {enemy_character_name}")
    getChar("press any key to continue")

    def enemyAttack(enemy,player:Player):
        attack = random.choice(enemy.getAttacks())
        if random.randint(1, 100) <= attack['accuracy']:
            player.takeDamage(attack['damage'])
            print(f"Enemy uses {attack['name']} your health is now {player.getHp()}", flush=True)
        else:
            if 'backfire' in attack:
                player.takeDamage(attack['damage'])
                print(f"Enemys attack backfired enemy took {attack['damage']} damage.", flush=True)
            else:
                print(f"Enemy missed attack with {attack['name']}", flush=True)

    while True:
        os.system("cls")
        attacks = random.sample(player.getAttacks(), 3)
        print("Your attack options:")
        for attack_number, attack in enumerate(attacks, 1):
            attack_str = f"{attack['name']} (Damage: {attack['damage']}, Accuracy: {attack['accuracy']}%)"
            if 'backfire' in attack:
                attack_str += f" [{attack['backfire']['chance']}% chance to backfire]"
            print(f"{attack_number}. {attack_str}")
        def selectAttack():
            selected = getChar(f"Select your attack (1-{len(attacks)}): ")
            if selected.isnumeric():
                selected = int(selected)
                if 1 <= selected <= len(attacks):
                    chosen_attack = attacks[selected - 1]
                    print(f"You selected: {chosen_attack['name']}")
                    accuracy = chosen_attack['accuracy']
                    if random.randint(1, 100) <= accuracy:
                        enemyPlayer.takeDamage(chosen_attack['damage'])
                    else:
                        print("attack missed ", end="")
                        if 'backfire' in chosen_attack:
                            print("your attack backfired!, your health is now at: ", player.getHp())
                        else:
                            print("")
                enemyAttack(enemyPlayer, player)
                sys.stdout.flush()
                getChar("press any key to enter next round")
            else:
                print("Invalid selection. Please try again.")
                selectAttack()
            print(f"attack hit enemy health at", enemyPlayer.getHp())
        selectAttack()
        if enemyPlayer.getHp() <= 0:
            print("You defeated the enemy!")
            break
        elif player.getHp() <= 0:
            print("You were defeated by the enemy!")


if __name__ == "__main__":
    os.write(sys.stdout.fileno(), b"\033[?1049h")
    main()
    getChar('press any key to quit')
    os.write(sys.stdout.fileno(), b"\033[?1049l")
    os.write(sys.stdout.fileno(), b"\033[?25h")
