import sys
from tkinter import *

class Spirolateral():
    def __init__(self, segment, angle):
        self.segmant = segmant
        self.angle = angle

spiroList = []
optionList = ["Add a spirolateral",
              "Remove a spirolateral",
              "Save spirolateral list",
              "Load spirolateral list",
              "Quit"]

root = Tk()
root.title("Spirolateral Program")
#root.geometry("300x100")

MAX_LIST = 10
MIN_CHOICE = 1

def spiroAdd():
    print(1)

def spiroRemove():
    print(2)

def save():
    print(4)

def load():
    print(5)

def Quit():
    clear()
    quitLabel = Label(text = "Are you sure you want to quit?")
    quitLabel.grid(row = 1)

    Button3 = Button(root, text = "Yes", command = root.destroy)
    Button4 = Button(root, text = "No", command = menu)
    Button3.grid(row = 2, sticky = N)
    Button4.grid(row = 2, sticky = W)

functionList = [spiroAdd, spiroRemove, save, load, Quit]

def checkNum(entry, label, response, lowerLimit, upperLimit, integer):
    try:
        choice = integer(entry.get())
        if choice < lowerLimit or choice > upperLimit:
            label.configure(text = response)
            return -1
        else:
            return choice
    except ValueError:
        if integer == int:
            label.configure(text = "That's not a valid {}. Please re-enter it.".format("integer"))
        elif integer == float:
            label.configure(text = "That's not a valid {}. Please re-enter it.".format("number"))
        return -1

def spiroPrint():
    spiros = Label(text = "Spirolaterals:")
    spiros.grid(row = 1, column = 2, sticky = W)

    for index in range(len(spiroList)):
        Spiroindex = Label(text = "{}) {} - ${:0.2f}".format(index + 1, spiroList[index].name, spiroList[index].debt))
        Spirorindex.grid(row = index + 2, column = 2, sticky = W)

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def menu():
    clear()
    Label1 = Label(text = "")
    Label1.grid(row = 1, sticky = W)
        
    x = 1
    for option in optionList:
        x += 1
        Buttonx = Button(root, text = option, command = functionList[x-2])
        Buttonx.grid(row = x, sticky = W)

    spiroPrint()
menu()
