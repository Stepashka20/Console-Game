from ctypes import *
import os,random,time,sys
from ctypes import *
import msvcrt
from threading import Thread
clear = lambda: os.system('cls')
clear()
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


def xprint_color(x, y, color, text):
	windll.Kernel32.SetConsoleTextAttribute(h, color)
	print_at(4, 33, text.format(color))


def print_color(color, text):
	windll.Kernel32.SetConsoleTextAttribute(h, color)
	print(text.format(color))


STD_OUTPUT_HANDLE = -11


class COORD(Structure): pass

xM=5
yM=7
class MyThread(Thread):
    """
    A threading example
    """
    
    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        """Запуск потока"""
        
COORD._fields_ = [("X", c_short), ("Y", c_short)]
def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

    c = s.encode("cp866")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
def printMatrix ( matrix ): 
	for i in range ( len(matrix) ): 
		str=""
		for j in range ( len(matrix[i]) ): 
			str=str+matrix[i][j]
		print_color(15,str) 
		# print()
matrix = [
	["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"], 
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    ]
printMatrix(matrix)

# xprint_color(4,10,10,"$\n")
windll.Kernel32.SetConsoleTextAttribute(h, 10)
y=2
x=2
print_at(y,x, "$".format(10))
keys = {
    0x48: 'Up',
    0x50: 'Down',
    0x4b: 'Left',
    0x4d: 'Right'}
 
while True:
    prefix = ord(msvcrt.getch())
    if prefix == 0xe0:
        # arrow keys
        keycode = ord(msvcrt.getch())
        symbol = keys.get(keycode, 'unexpected')
        if symbol=="Up":
        	if matrix[y-1][x]!="_":
        		print_at(y, x, " ".format(10))
        		y=y-1
        		print_at(y, x, "$".format(10))
        elif symbol=="Down":
        	if matrix[y+1][x]!="_":
        		print_at(y, x, " ".format(10))
        		y=y+1
        		print_at(y, x, "$".format(10))
        elif symbol=="Left":
        	if matrix[y][x-1]!="|":
        		print_at(y, x, " ".format(10))
        		x=x-1
        		print_at(y, x, "$".format(10))
        elif symbol=="Right":
        	if matrix[y][x+1]!="|":
        		print_at(y, x, " ".format(10))
        		x=x+1
        		print_at(y, x, "$".format(10))

