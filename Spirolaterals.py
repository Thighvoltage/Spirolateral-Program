from tkinter import *
import turtle

class Spirolateral:
    def __init__(self, name, segment, angle):
        self.name = name
        self.segment = segment
        self.angle = angle

spiros = []
options = ["Add a spirolateral",
           "Remove a spirolateral",
           "Draw a spirolateral",
           "Save spirolateral list",
           "Load spirolateral list",
           "Quit"]

root = Tk()
root.title("Spirolateral Program")
#root.geometry("300x100")

MAX_SPIRO = 10
MIN_CHOICE = 1

def spiro_add():
    if len(spiros) == MAX_SPIRO:
       label3.configure(text = "You can only lend funds to up to {} people at once.".format(MAX_SPIRO))
    else:
        clear()

        label1.configure(text = "What's the name of your spirolateral?")
        label2.configure(text = "")
        label1.grid(row = 1, sticky = W)
        entry1.grid(row = 2, sticky = W, padx = 3)
        label2.grid(row = 3, sticky = W)

        label3.configure(text = "How many segments does your spirolateral have? Please enter an integer with no symbols.")
        label4.configure(text = "")
        label3.grid(row = 4, sticky = W)
        entry2.grid(row = 5, sticky = W, padx = 3)
        label4.grid(row = 6, sticky = W)

        label5.configure(text = "What's the angle of your spirolateral? Please enter an integer with no symbols.")
        label6.configure(text = "")
        label5.grid(row = 7, sticky = W)
        entry3.grid(row = 8, sticky = W, padx = 3)
        label6.grid(row = 9, sticky = W)

        button1.configure(command = check_add)
        button1.grid(row = 10, sticky = N)
        button2.grid(row = 10, sticky = W)

def check_add():
    name = entry1.get()
    if name == "":
        label2.configure(text = "Please enter a name.")
    for index in range(len(spiros)):
        if name == spiros[index].name:
            label2.configure(text = "There is already a spirolateral called {}.".format(name))
            name = ""
    segment = check_num(entry2, label4, "You can't 0 or less segments.", MIN_CHOICE, float('inf'), int)
    angle = check_num(entry3, label6, "You can't have an angle of 0 or less degrees, or an angle of above 360 degrees.", MIN_CHOICE, 360, int)
    if name != "" and segment != -1 and angle != -1:
        spiros.append(Spirolateral(name, segment, angle))
        entry1.delete(0, 99)
        entry2.delete(0, 99)
        entry3.delete(0, 99)
        menu()

def spiro_remove():
    if len(spiros) == 0:
        label3.configure(text = "There are no spirolaterals for you to remove.")

    else:
        clear()
        label1.configure(text = "Enter the integer to the left of the spirolateral you'd like to remove.")
        label2.configure(text = "")
        label1.grid(row = 1, sticky = W)
        entry1.grid(row = 2, sticky = W, padx = 3)
        label2.grid(row = 3, sticky = W)

        button1.configure(command = check_remove)
        button1.grid(row = 4, sticky = N)
        button2.grid(row = 4, sticky = W)

        spiro_print(1, 2)

def check_remove():
    choice = check_num(entry1, label2, "That integer doesn't correspond to anything.", MIN_CHOICE, len(spiros), int)
    if choice != -1:
        del spiros[choice - 1]
        entry1.delete(0, 99)
        menu()

def spiro_draw():
    global turt
    clear()

    canvas = Canvas(root, width = 500, height = 500)
    canvas.grid(row = 1, column = 1)

    turt = turtle.RawTurtle(canvas)
    turt.speed(10)
    label1.configure(text = "Enter the integer to the left of the spirolateral you want to draw.")

    spiro_print(2, 2)

    label1.grid(row = 2, column = 1)
    label2.grid(row = 5, column = 1)
    entry1.grid(row = 3, column = 1)
    button2.grid(row = 4, column = 1, sticky = W)
    button5.grid(row = 4, column = 1)
    button6.grid(row = 4, column = 1, sticky = E)

def start_draw():
    global in_motion
    choice = check_num(entry1, label2, "That integer doesn't correspond to anything.", MIN_CHOICE, len(spiros), int)
    turt.reset()
    in_motion = True
    if choice != -1:
        xpos, ypos = -1, -1
        while  round(xpos) != 0 and round(ypos) != 0:
            x = 20
            for segment in range(spiros[choice - 1].segment):
                    turt.rt(180 + spiros[choice - 1].angle)
                    turt.fd(x)
                    x += 20
                    if in_motion == False:
                        return

            xpos, ypos = turt.pos()

def stop_draw():
    global in_motion
    in_motion = False

def save():
    print(4)

def load():
    print(5)

def Quit():
    clear()
    quit_label = Label(text = "Are you sure you want to quit?")
    quit_label.grid(row = 1)

    button3 = Button(root, text = "Yes", command = root.destroy)
    button4 = Button(root, text = "No", command = menu)
    button3.grid(row = 2, sticky = N)
    button4.grid(row = 2, sticky = W)

function_list = [spiro_add, spiro_remove, spiro_draw, save, load, Quit]

def check_num(entry, label, response, lower_limit, upper_limit, integer):
    try:
        choice = integer(entry.get())
        if choice < lower_limit or choice > upper_limit:
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

def spiro_print(row, column):
    spiro_label = Label(text = "Spirolaterals:")
    spiro_label.grid(row = row, column = column, sticky = W)

    for index in range(len(spiros)):
        Spiroindex = Label(text = "{}) {} - {} segments {}°".format(index + 1, spiros[index].name, spiros[index].segment, spiros[index].angle))
        Spiroindex.grid(row = index + row + 1, column = column, sticky = W)

def clear():
    for widget in root.winfo_children():
        widget.grid_forget()

def menu():
    clear()
    label1 = Label(text = "")
    label1.grid(row = 1, sticky = W)

    x = 1
    for option in options:
        x += 1
        buttonx = Button(root, text = option, command = function_list[x-2])
        buttonx.grid(row = x, sticky = W)

    spiro_print(1, 2)

label1, label2, label3, label4, label5, label6 = (Label(root, text = "") for i in range (6))
button1, button2 = Button(root, text = "Enter"), Button(root, text = "Back", command = menu)
button3, button4 = Button(root, text = "Yes", command = root.destroy), Button(root, text = "No", command = menu)
button5, button6 = Button(root, text = "Draw", command = start_draw), Button(root, text = "Stop", command = stop_draw)
entry1, entry2, entry3 = (Entry(root) for i in range(3))

menu()
root.mainloop()
