import msvcrt
import os

def makeList(moves:list, highlight:bool=True):
    selected = 0
    while True:
        os.system('cls')
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
        if key in {b'\x00', b'\xe0'}:  # special key prefix
            key = msvcrt.getch()  # actual key
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
