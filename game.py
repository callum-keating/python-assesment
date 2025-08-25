import os, sys, msvcrt, random

def select_random_attacks(character):
    return random.sample(character.attacks, 3)

characters = ["Scavenger", "Medic", "Veteran", "Hunter", "Illusionist"]
def getChar(msg:str):
    print(msg, end='', flush=True)
    char = msvcrt.getch()
    try:
        char = char.decode("utf-8")
    except:
        char = ""
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
            {"name": "Explosive Barrel", "damage": 20, "accuracy": 80, "backfire": {"chance": 20}}
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
            {"name": "Toxic Overdose", "damage": 20, "accuracy": 80, "backfire": {"chance": 20}}
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
            {"name": "Airstrike", "damage": 20, "accuracy": 80, "backfire": {"chance": 20}}
        ]

class Hunter:
    def __init__(self):
        self.hp = 110
        self.attacks = [
            {"name": "Track", "damage": 6, "accuracy": 85},
            {"name": "Ambush", "damage": 12, "accuracy": 70},
            {"name": "Trap", "damage": 9, "accuracy": 80},
            {"name": "Snipe", "damage": 14, "accuracy": 60},
            {"name": "Camouflage", "damage": 0, "accuracy": 100},
            {"name": "Beast Lure", "damage": 20, "accuracy": 80, "backfire": {"chance": 20}}
        ]

class Illusionist:
    def __init__(self):
        self.hp = 95
        self.attacks = [
            {"name": "Mirror Image", "damage": 0, "accuracy": 100, "effect": "create clone to absorb next hit"},
            {"name": "Phantom Strike", "damage": 10, "accuracy": 75},
            {"name": "Mind Twist", "damage": 7, "accuracy": 85, "effect": "confuse enemy, chance to miss next attack"},
            {"name": "False Reality", "damage": 0, "accuracy": 100, "effect": "force enemy to attack themselves (low chance)"},
            {"name": "Vanishing Veil", "damage": 0, "accuracy": 100, "effect": "dodge next attack if timed well"},
        ]



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
    if char > len(characters):
        panic("character doesn't exist, was your number to large")
    character_name = characterOptions[char - 1]

    os.system("cls")
    print("you selected ", character_name)

    char_class_map = {
        "Scavenger": Scavenger,
        "Medic": Medic,
        "Veteran": Veteran,
        "Hunter": Hunter,
        "Illusionist": Illusionist
    }
    player = char_class_map[character_name]()

    enemy_choices = [c for c in characterOptions if c != character_name]
    enemy_character_name = random.choice(enemy_choices)
    enemy = char_class_map[enemy_character_name]()
    print(f"Your enemy is: {enemy_character_name}\n")

    attacks = select_random_attacks(player)

    print("Your attack options:")
    for attack_number, attack in enumerate(attacks, 1):
        attack_str = f"{attack['name']} (Damage: {attack['damage']}, Accuracy: {attack['accuracy']}%)"
        if 'backfire' in attack:
            attack_str += f" [{attack['backfire']['chance']}% chance to backfire]"
        print(f"{attack_number}. {attack_str}")

    while True:
        selected = getChar(f"Select your attack (1-{len(attacks)}): ")
        if selected.isnumeric():
            selected = int(selected)
            if 1 <= selected <= len(attacks):
                chosen_attack = attacks[selected - 1]
                print(f"You selected: {chosen_attack['name']}")
                if random.randint(1, chosen_attack['accuracy']) > chosen_attack['accuracy']:
                    print("attack missed")
                else:
                    print(f"attack hit enemy health at,")
                break
        print("Invalid selection. Please try again.")


if __name__ == "__main__":
    os.write(sys.stdout.fileno(), b"\033[?1049h")
    main()
    getChar('press any key to quit')
    os.write(sys.stdout.fileno(), b"\033[?1049l")
    os.write(sys.stdout.fileno(), b"\033[?25h")
