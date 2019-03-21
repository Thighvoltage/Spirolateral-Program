from tkinter import *

class Spirolateral():
    def __init__(self, name, segment, angle):
        self.name = name
        self.segment = segment
        self.angle = angle


class GUI:
    def __init__(self, master):

        COLOUR_BG = "pale green"
        COLOUR_FG = "orchid"
        PAD_LX = 20
        PAD_LY = 10
        PAD_BX = 3
        PAD_BY = 3

        self.master = master
        self.frame_menu = Frame(master, bg = COLOUR_BG)
        self.frame_menu.grid(row = 0, column = 0, columnspan = 2,
                             sticky = 'nesw')

        self.label_menu = Label(self.frame_menu, text = "Menu", bg = COLOUR_BG)

        self.button_add = Button(self.frame_menu, text = "Add a spirolateral",
                                 command = self.spiro_add)
        self.button_remove = Button(self.frame_menu, text = "Remove a spiro"
                                    + "lateral", command = self.spiro_remove)
        self.button_draw = Button(self.frame_menu, text = "Draw a spirolateral"
                                  , command = self.spiro_draw)
        self.button_save = Button(self.frame_menu, text = "Save spirolateral "
                                  + "list", command = self.save)
        self.button_load = Button(self.frame_menu, text = "Load spirolateral "
                                  + "list", command = self.load)
        self.button_quit = Button(self.frame_menu, text = "Quit",
                                  command = self.quit)

        self.label_menu.grid(row = 0, column = 0, rowspan = 2, padx = PAD_LX)

        self.button_add.grid(row = 0, column = 1, padx = PAD_BX, pady = PAD_BY,
                             sticky = EW)
        self.button_remove.grid(row = 1, column = 1, padx = PAD_BX,
                                pady = PAD_BY, sticky = EW)
        self.button_draw.grid(row = 1, column = 2, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_save.grid(row = 0, column = 2, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_load.grid(row = 0, column = 3, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)
        self.button_quit.grid(row = 1, column = 3, padx = PAD_BX,
                              pady = PAD_BY, sticky = EW)

        self.frame_secondary = Frame(master)
        self.frame_secondary.grid(row = 1, column = 1, sticky = NW)

        self.label_prompt1 = Label(self.frame_secondary, pady = PAD_LY)
        self.label_prompt2 = Label(self.frame_secondary, pady = PAD_LY)
        self.label_prompt3 = Label(self.frame_secondary, pady = PAD_LY)

        self.label_response1 = Label(self.frame_secondary, padx = PAD_LX)
        self.label_response2 = Label(self.frame_secondary, padx = PAD_LX)
        self.label_response3 = Label(self.frame_secondary, padx = PAD_LX)

        self.button_enter = Button(self.frame_secondary, text = "Enter",
                                   width = 10, padx = PAD_BX, pady = PAD_BY)
        self.button_yes = Button(self.frame_secondary, text = "Yes")
        self.button_no = Button(self.frame_secondary, text = "No")

        self.entry1 = Entry(self.frame_secondary)
        self.entry2 = Entry(self.frame_secondary)
        self.entry3 = Entry(self.frame_secondary)

        self.frame_spiro = Frame(master)
        self.frame_spiro.grid(row = 1, column = 0, sticky = NW)

        self.label_spiro = Label(self.frame_spiro, text = "Spirolaterals:")
        self.label_spiro.grid(row = 0, column = 0, padx = PAD_LX,
                              pady = PAD_LY, sticky = NW)

    def spiro_add(self):
        if len(spiros) == MAX_SPIRO:
           label3.configure(text = "You can only have {} spirolaterals."
                            .format(MAX_SPIRO))
        else:
            self.label_prompt1.configure(text = "Name:")
            self.label_prompt2.configure(text = "Segments:")
            self.label_prompt3.configure(text = "Angle:")

            self.label_prompt1.grid(row = 1, column = 0, sticky = W)
            self.label_prompt2.grid(row = 2, column = 0, sticky = W)
            self.label_prompt3.grid(row = 3, column = 0, sticky = W)

            self.label_response1.grid(row = 1, column = 2, sticky = W)
            self.label_response2.grid(row = 2, column = 2, sticky = W)
            self.label_response3.grid(row = 3, column = 2, sticky = W)

            self.entry1.grid(row = 1, column = 1)
            self.entry2.grid(row = 2, column = 1)
            self.entry3.grid(row = 3, column = 1)

            self.button_enter.configure(command = self.check_add)

            self.button_enter.grid(row = 6, column = 0, sticky = W)

            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)

    def check_add(self):
        name = self.entry1.get()
        if name == "":
            self.label_response1.configure(text = "Enter a name.")

        for index in range(len(spiros)):
            if name == spiros[index].name:
                label2.configure(text = "There's already a spirolateral called"
                                 + "{}.".format(name))
                name = ""

        segment = check_num(self.entry2, self.label_response2,
                            "Can't have 0 or less segments.",
                            MIN_CHOICE, float('inf'), int)
        angle = check_num(self.entry3, self.label_response3,
                          "Angle can't be less than 0° or greater than 360°.",
                          MIN_CHOICE, 360, int)

        if name != "" and segment != -1 and angle != -1:
            spiros.append(Spirolateral(name, segment, angle))

    def spiro_remove(self):
        self.label_prompt1.configure(text = "Integer:")

        self.label_prompt1.grid(row = 1, column = 0, sticky = W)

        self.entry1.grid(row = 1, column = 1)

        self.button_enter.configure(command = self.check_remove)

    def check_remove(self):
        choice = check_num("That integer doesn't correspond to anything.")
        if choice != -1:
            del spiros[choice - 1]

    def spiro_draw(self):
        print(3)

    def save(self):
        print(4)

    def load(self):
        print(5)

    def quit(self):
        print(6)

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
            label.configure(text = "Not a valid integer.")
        elif integer == float:
            label.configure(text = "Not a valid number.")
        return -1

def spiro_print():
    print(5)

spiros = []
MAX_SPIRO = 10
MIN_CHOICE = 1

def main():
    root = Tk()
    root.title("Spirolateral Program")
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
