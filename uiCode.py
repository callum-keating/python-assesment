import msvcrt
import os, sys

def makeList(moves:list, highlight:bool=True, showInfo:bool=False):
    #creates a selected variable to store the currently highlighted value
    selected = 0
    while True:
        #clears every loop
        os.system('cls')
        #prints how to use it if specified
        if showInfo:
            print("\033[1m\033[33m*Use up and down arrow keys to navigate and Enter to select.*\033[0m")
        for loopNum, i in enumerate(moves):
            #show selected if the loop is currently on it
            if loopNum == selected:
                if highlight:
                    print("\033[34m> ", i, "\033[0m")
                else:
                    print("> ", i)

            #else print just i
            else:
                print(i)
            loopNum += 1
        #drops loopNum as it is unneeded
        del loopNum
        key = msvcrt.getch()
        if key == b'\x03':
            os.write(sys.stdout.fileno(), b"\033[?1049l")
            os.write(sys.stdout.fileno(), b"\033[?25h")
            quit()
        #if the key is an up or down arrow
        if key in {b'\x00', b'\xe0'}:
            key = msvcrt.getch()
            if key == b'P':
                selected += 1
            elif key == b'H':
                selected -= 1
            selected = max(0, min(selected, len(moves) - 1))

        elif key == b'\r':  # Enter key
            break
    return selected

def winScreen():
    os.system('cls')
    #show bold and coloured win
    print("\033[1m\033[32mYou win!\033[0m")
def looseScreen():
    os.system('cls')
    #show bold and coloured lose
    print("\033[1m\033[31myou loose!\033[0m")
def tieScreen():
    os.system('cls')
    #show bold and coloured tie
    print("\033[1m\033[33mIt's a tie!\033[0m")
def printImage(image: str):
    os.system('cls')  # Clear screen (Windows)
    try:
        with open(f"characters/{image}.txt", "r", encoding="utf-8") as f:
            # Read lines without newlines
            lines = [line.rstrip('\n') for line in f]
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"Error: File characters/{image}.txt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def startScreen(characters):
    os.system('cls')
    printImage(characters[0].lower())
    selected = 0
    print("currently selecting:\033[36m", characters[selected], "\033[0m")
    print("\033[1m\033[33m*Use left and right arrow keys to navigate and Enter to select.*\033[0m")
    while True:
        key = msvcrt.getch()
        if key in {b'\x00', b'\xe0'}:
            key = msvcrt.getch()
            if key == b'K':
                selected -= 1
            elif key == b'M':
                selected += 1
            selected = max(0, min(selected, len(characters) - 1))
        elif key == b'\x03':
            #exit alternate buffer and restore cursor before quitting
            os.write(sys.stdout.fileno(), b"\033[?1049l")
            os.write(sys.stdout.fileno(), b"\033[?25h")
            quit()
        elif key == b'\r':  # Enter key
            break
        os.system('cls')
        printImage(characters[selected].lower())
        print("currently selecting:\033[36m", characters[selected], "\033[0m")
        print("\033[1m\033[33m*Use left and right arrow keys to navigate and Enter to select.*\033[0m")
    return selected + 1