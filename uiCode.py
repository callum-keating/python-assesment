import msvcrt
import os, sys

def makeList(moves:list, highlight:bool=True, showInfo:bool=False):
    selected = 0
    while True:
        os.system('cls')
        if showInfo:
            print("\033[1m\033[33m*Use up and down arrow keys to navigate and Enter to select.*\033[0m")
        loopNum = 0
        for i in moves:
            if loopNum == selected:
                if highlight:
                    print("\033[34m> ", i, "\033[0m")
                else:
                    print("> ", i)

            else:
                print("", i)
            loopNum += 1
        del loopNum
        key = msvcrt.getch()
        if key == b'\x03':
            os.write(sys.stdout.fileno(), b"\033[?1049l")
            os.write(sys.stdout.fileno(), b"\033[?25h")
            quit()
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
    print("\033[1m\033[32mYou win!\033[0m")
def looseScreen():
    os.system('cls')
    print("\033[1m\033[31mYou loose!\033[0m")
