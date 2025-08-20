import os, sys
characters = ["Scavenger", "Medic", "Technition"]
def panic(errorMsg:str):
    print("panic: ", errorMsg)
    quit()
def main():
    os.system("clear")
    print("characters: ", characters)
    char = input("select a character 1-" + str(len(characters)) + " number only: ")
    if not char.isnumeric():
        panic("Input is not an integer. make sure you type a number not character name!")
    char = int(char)
    if char < 1:
        panic("Number can not be less than 1")
    if char > len(characters):
        panic("character doesn't exist, was your number to large")
if __name__ == "__main__":
    os.write(sys.stdout.fileno(), b"\033[?1049h")
    main()
    os.write(sys.stdout.fileno(), b"\033[?1049l")