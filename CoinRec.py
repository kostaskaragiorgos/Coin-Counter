"""
Coin Counter  project
"""
from tkinter import Menu, Tk
from tkinter import messagebox as msg
from tkinter import filedialog

def helpmenu():
    """ help menu """
    msg.showinfo("HELP", "HELP")
def aboutmenu():
    """ about """
    msg.showinfo("About", "About \nVersion 1.0")
class CoinCounter():
    """
    Coin Counter recognition class
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Coin Counter")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

    def exitmenu(self):
        """ exit menu"""
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    CoinCounter(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
