from tkinter import *
from tkinter import messagebox
import random
import string
 
def printRandomInt():
    r_int = random.randint(1,10000000)
    messagebox.showinfo("information","Random integer number: "+str(r_int))
 
def printRandomFloat():
    r_float = random.random()
    messagebox.showinfo("information","Random float number: "+str(r_float))
 
def printRandomSmall():
    r_small = random.choice(string.ascii_lowercase)
    messagebox.showinfo("information","Random lowercase character: "+r_small)
 
def printRandomCap():
    r_float = random.choice(string.ascii_uppercase)
    messagebox.showinfo("information","Random uppercase character: "+r_float)
 
 
class Window(Frame):
 
    def __init__(self, master=None):
        Frame.__init__(self, master)                
        self.master = master
        self.init_window()
 
    def init_window(self):
        #self.pack(fill=BOTH, expand=1)
        self.pack()
        button1 = Button(self, text = "Print Random Integer", fg = "Black", bg = "White", command = printRandomInt)
        button2 = Button(self, text = "Print Random Float", fg = "Black", bg = "White", command = printRandomFloat)
        button3 = Button(self, text = "Print Random Small", fg = "Black", bg = "White", command = printRandomSmall)
        button4 = Button(self, text = "Print Random Cap", fg = "Black", bg = "White", command = printRandomCap)
        button1.grid(row = 1, column = 1,padx=10,pady=250)
        button2.grid(row = 1, column = 2,padx=10,pady=250)
        button3.grid(row = 1, column = 3,padx=10,pady=250)
        button4.grid(row = 1, column = 4,padx=10,pady=250)
 
root = Tk()
#root.configure(background = "light blue")
root.title("Random Generator")
root.geometry("700x300")
 
app = Window(root)
root.mainloop()
