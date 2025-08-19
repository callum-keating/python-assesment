import random
from rich.console import Console
from rich.table import Table
import rich
import readchar
import gameCharacters

def game():
    characterRandom = random.sample(gameCharacters.characters, 4)
    while True:
        console = Console()
        console.clear()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Character", style="dim", width=12)
        table.add_column("Health", justify="right", width=6)
        table.add_column("Attack", justify="right", width=6)
        table.add_column("Defense", justify="right", width=6)

        loopNum: int = 0
        for character in gameCharacters.characters:
            table.add_row(characterRandom[loopNum])
            loopNum += 1

        console.print(table, justify="center")
        key = readchar.readchar()
        if key == 'q':
            console.clear()
            break

if __name__ == "__main__":
    print("This module is not meant to be run directly. Please use the main game script game.py")

