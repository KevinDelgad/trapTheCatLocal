from tkinter import *
from tkinter import ttk
from cat import Cat
#create Window
root = Tk()

#Set Window size
root.geometry('1000x1000')

freeSpaces = {}
gameFrames = {}
gameRows = [0,1,2,3,4,5,6,7,8,9,10]
validSpaces = []

#Create buttons for gameboard
def createBoard():
    x,y = 11 , 11
    for a in range(0, y):
        for b in range(0,x):
            validSpaces.append((str(a) + "x" + str(b)))
        
    for rows in gameRows:
        gameFrames[rows] = ttk.Frame()
        gameFrames[rows].pack(side = LEFT)

    for elem in validSpaces:
        if(elem[1] == 'x'):
            freeSpaces[elem] = ttk.Button(gameFrames.get(int(elem[0])), text = "", command = lambda m = elem: deleteTile(m))
            freeSpaces[elem].pack()
        else:
            freeSpaces[elem] = ttk.Button(gameFrames.get(int(elem[0:2])), text = "", command = lambda m = elem: deleteTile(m))
            freeSpaces[elem].pack()


def deleteTile(button_press):
    validSpaces.remove(button_press)
    theCat.calculateNextMove(validSpaces)

theCat = Cat()

createBoard()

root.mainloop()
