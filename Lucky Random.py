from tkinter import *
from tkinter import messagebox
import random, string, webbrowser
 
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
    messagebox.showinfo(title="Good luck",message="toss coins : "+r_string)

def printRandomPassword(): #สุ่ม Password
    s="abcdefghijklmnopqrstuvwxyz012345678970ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&_" #stringสำหรับสุ่ม
    ranlen = random.randint(8, 13) #len ของpassword เป็นสุ่ม
    password =  "".join(random.sample(s,ranlen))
    condition = messagebox.askyesnocancel(title='Your password', message='Yes to print password'.center(45) + '\n' + 'No to try a new one'.center(45) + '\n' + f'{password}'.center(45))
    if condition == True:
        print('This is your password >>>>>>>> %s <<<<<<<<<' %password)
    elif condition == False:
        printRandomPassword()
    
def printRandomMenu():
    menu_ls = ['Stewed pork leg', 'Pork panang curry', 'Fried rice', 'Beef curry', 'Papaya salad',\
            'Chicken wings', 'Chicken legs', 'Grilled pork neck', 'Pan fried seafood', 'Thai Basil Chicken ',\
            'Fried pork with garlic', 'Fermented fish spicy dip', 'Steamed egg', 'Stuffed egg', 'Son-in-law Eggs',\
            'Red pork over rice', 'Chicken rice', 'American fried rice', 'Pad thai', 'Dried noodles', 'Noodles soup',\
            'Egg noodles', 'American fried rice', 'Minced pork omelet', 'Fried egg', 'omelet', 'Stir fried vegetables',\
            'Seafood salad', 'Curry-fried fish', 'Chicken curry', 'Pork curry']
    menu_select = random.choice(menu_ls)
    select = messagebox.askretrycancel(title="Menu", message="Menu for your meal: %s" %(menu_select))
    if select == True:
        printRandomMenu()

def gotolink():
    url = ["https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10",\
       "https://www.youtube.com/watch?v=Nj2U6rhnucI&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=11",\
       "https://www.youtube.com/watch?v=dqRZDebPIGs&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=12",\
        "https://www.youtube.com/watch?v=VF-r5TtlT9w&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=15",\
        "https://www.youtube.com/watch?v=9HDEHj2yzew&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=17"]
    webbrowser.open_new_tab(random.choice(url))
 
class Window(Frame):
 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
 
    def init_window(self):
        #self.pack(fill=BOTH, expand=1)
        self.pack()
        button1 = Button(self, text = "Lottery 1st prize", fg = "Black", bg = "White", command = printRandomInt)
        button2 = Button(self, text = "Random Menu ", fg = "Black", bg = "white", command = printRandomMenu)
        button3 = Button(self, text = "Random Password", fg = "Black", bg = "white", command = printRandomPassword)
        button4 = Button(self, text = "Listen music playlist", fg = "Black", bg = "White", command = gotolink)
        button1.grid(row = 1, column = 1,padx=10,pady=50)
        button2.grid(row = 1, column = 2,padx=10,pady=50)
        button3.grid(row = 2, column = 1,padx=10,pady=30)
        button4.grid(row = 2, column = 2,padx=10,pady=30)
 
root = Tk()
# root.configure(background = "light blue")
root.title("Random Generate")
root.geometry("450x250")

app = Window(root)
root.mainloop()