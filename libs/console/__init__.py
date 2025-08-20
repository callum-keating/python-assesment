import os

class Console:
    def __init__(self):
        self.fgColours = {
            'black': '\033[30m',
            'white': '\033[37m',
            'console': '\033[39m',
        }
        self.bgColours = {
            'black': '\033[40m',
            'white': '\033[47m',
            'console': '\033[49m',
        }
    def clear(self):
        print("\033[H\033[2J\033[3J\033[H")
        pass
    def setCursor(self, x: int, y: int):
        print(f"\033[{y};{x}H")
    def change_buffer(self):
        pass
    def getXY(self):
        xy = [ os.get_terminal_size().lines, os.get_terminal_size().columns ]
        return xy
    def print(self,text:str, fg:str='console', bg:str='console'):
        if isinstance(fg, list):
            fg = fg[0]
        if isinstance(bg, list):
            bg = bg[0]

        print(f"{self.fgColours.get(fg)}{self.bgColours.get(bg)}{text}\033[0m")
class selectableTable:
    def __init__(self):
        self.rows = []
        self.position = "left" # can be left right or center
        self.selectedRow = 0
        self.neededRows = 0
        self.title = "testing"
    def refresh(self):
        for i in range(len(self.rows)):
            self.neededRows += len(self.rows[i]) + 2
        self.neededRows -= 1
        print(self.neededRows)
        for i in range(int(self.neededRows/2 - len(self.title)/2)):
            print(" ", end='')
        print(self.title)
        for i in range(self.neededRows):
            print('—',end='')
        print('')
        for i in range(len(self.rows)):
            print(f"|{self.rows[i]}", end='')
        print('|')
        for i in range(self.neededRows):
            print('—',end='')
        print('')
    def addRow(self, name:str):
        self.rows.append(name)