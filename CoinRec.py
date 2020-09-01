"""
Coin Counter  project
"""
from tkinter import Menu, Tk
from tkinter import messagebox as msg
from tkinter import filedialog

import cv2
import numpy as np

def imagemod(imagefile):
    coins = cv2.imread(imagefile)
    coins = cv2.resize(coins, (740, 740))
    gr = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gr, 5)
    rows = img.shape[0]
    circles = cv2.HoughCircles(img , cv2.HOUGH_GRADIENT,1, rows/8, param1=100, param2=30, minRadius=0, maxRadius=60)
    return circles, coins

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
        self.file_menu.add_command(label="Insert image", accelerator='Ctrl+0', command=self.addimage)
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
    


    def addimage(self):
        imgfile = filedialog.askopenfilename(initialdir="/", title="Select an image file",
                                             filetypes=(("image files", "*.jpg"),
                                                        ("all files", "*.*")))
        if ".jpg" in imgfile:
            circles, coins = imagemod(imgfile)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    center = (i[0], i[1])
                    # circle center
                    cv2.circle(coins, center, 1, (0, 100, 100), 3)
                    # circle outline
                    radius = i[2]
                    cv2.circle(coins, center, radius, (255, 0, 255), 3)

            cv2.imshow("Cir", coins)
            cv2.waitKey()
            cv2.destroyAllWindows()

        else:
            msg.showerror("Abort", "Abort")

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
