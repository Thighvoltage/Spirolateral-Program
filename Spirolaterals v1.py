import sys
from tkinter import *

class Spirolateral():
    def __init__(self, name, segment, angle):
        self.name = name
        self.segment = segment
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

MAX_SPIRO = 10
MIN_CHOICE = 1

def spiroAdd():
    if len(spiroList) == MAX_SPIRO:
       Label3.configure(text = "You can only lend funds to up to {} people at once.".format(MAX_SPIRO))
    else:
        clear()

        Label1.configure(text = "What's the name of your spirolateral?")
        Label2.configure(text = "")
        Label1.grid(row = 1, sticky = W)
        Entry1.grid(row = 2, sticky = W, padx = 3)
        Label2.grid(row = 3, sticky = W)

        Label3.configure(text = "How many segments does your spirolateral have? Please enter an integer with no symbols.")
        Label4.configure(text = "")
        Label3.grid(row = 4, sticky = W)
        Entry2.grid(row = 5, sticky = W, padx = 3)
        Label4.grid(row = 6, sticky = W)

        Label5.configure(text = "What's the angle of your spirolateral? Please enter an integer with no symbols.")
        Label6.configure(text = "")
        Label5.grid(row = 7, sticky = W)
        Entry3.grid(row = 8, sticky = W, padx = 3)
        Label6.grid(row = 9, sticky = W)

        Button1.configure(command = checkAdd)
        Button1.grid(row = 10, sticky = N)
        Button2.grid(row = 10, sticky = W)

def checkAdd():
    name = Entry1.get()
    if name == "":
        Label2.configure(text = "Please enter a name.")
    for index in range(len(spiroList)):
        if name == spiroList[index].name:
            Label2.configure(text = "There is already a spirolateral called {}.".format(name))
    segment = checkNum(Entry2, Label4, "You can't 0 or less segments.", MIN_CHOICE, float('inf'), int)
    angle = checkNum(Entry3, Label6, "You can't have an angle of 0 or less degrees, or an angle of above 360 degrees.", MIN_CHOICE, 360, int)
    if name != "" and segment != -1 and angle != -1:
        spiroObj = Spirolateral(name, segment, angle)
        spiroList.append(spiroObj)
        Entry1.delete(0, 99)
        Entry2.delete(0, 99)
        Entry3.delete(0, 99)
        menu()

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
        Spiroindex = Label(text = "{}) {} - {} segments {}°".format(index + 1, spiroList[index].name, spiroList[index].segment, spiroList[index].angle))
        Spiroindex.grid(row = index + 2, column = 2, sticky = W)

def clear():
    for widget in root.winfo_children():
        widget.grid_forget()

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

Label1, Label2, Label3, Label4, Label5, Label6 = (Label(root, text = "") for i in range (6))
Button1, Button2 = Button(root, text = "Enter"), Button(root, text = "Back", command = menu)
Entry1, Entry2, Entry3 = (Entry(root) for i in range(3))

menu()
root.mainloop()
