from tkinter import *
from tkinter import messagebox
import random
import string
 
def printRandomInt():
    r_int = random.randint(1,1000000)
    messagebox.showinfo(title="Good luck", message="Have a beautiful day! %06d" %(r_int))
 
def printRandomFloat():
    r_float = random.randint(1,1000)
    messagebox.showinfo(title="Good luck", message="Have a good day! %03d " %(r_float))

'''สุ่มเลข 2 หลัก #function เก่า'''
# def printRandomSmall():
#     r_small = random.randint(1,100)
#     messagebox.showinfo(title="Good luck",message="Good Luck Bro! %02d" %(r_small))
 
def printRandomCap():
    r_string = random.choice(["Heads", "Tails"])
    messagebox.showinfo(title="Good luck",message="toss coin : "+r_string)

def printRandomPassword():
    s="abcdefghijklmnopqrstuvwxyz012345678970ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&"
    ranlen = random.randint(7, 13)
    password =  "".join(random.sample(s,ranlen))
    messagebox.showinfo(title='Your password', message='Good luck!: %s' %password)
 
 
class Window(Frame):
 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
 
    def init_window(self):
        #self.pack(fill=BOTH, expand=1)
        self.pack()
        button1 = Button(self, text = "Lottery 1st prize", fg = "Black", bg = "White", command = printRandomInt)
        button2 = Button(self, text = "Lottery the three digit prize ", fg = "Black", bg = "white", command = printRandomFloat)
        button3 = Button(self, text = "Random Password", fg = "Black", bg = "white", command = printRandomPassword)
        button4 = Button(self, text = "Toss a coin heads/tails", fg = "Black", bg = "White", command = printRandomCap)
        button1.grid(row = 1, column = 1,padx=30,pady=50)
        button2.grid(row = 1, column = 2,padx=30,pady=50)
        button3.grid(row = 2, column = 1,padx=30,pady=30)
        button4.grid(row = 2, column = 2,padx=30,pady=30)
 
root = Tk()
root.configure(background = "white")
root.title("Random Generate")
root.geometry("400x250")

app = Window(root)
root.mainloop()