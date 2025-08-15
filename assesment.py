characters = ["Knight", "King", "Queen"]

def panic(msg:str):
    print("panic: ", msg)
    quit()
def softPanic(msg:str):
    print("soft panic: ", msg)
i = 1
while i - 1 < len(characters):
    print(i, ": ", characters[i - 1])
    i += 1
option = input("what is your choice: ")
if not option.isdigit():
    panic("Please enter a number DON'T enter character name")

option = int(option) - 1

if option > len(characters) - 1:
    panic("Number is greater than options")

optionCharacter = characters[option]

print("you have selected: ", optionCharacter)