from tkinter import *
from tkinter import messagebox
import random, string, webbrowser

def Random2Digit(): # unused
    """2 digit number random function"""
    r_2digit = random.randint(1, 100) # สุ่มเลข 01 ถึง 99
    messagebox.showinfo(title="Good luck", message="Good Luck Bro! %02d" %(r_2digit))

def Randon3Digit(): # unused
    """3 digit number random function"""
    r_3digit = random.randint(1, 1000) # สุ่มเลข 001 ถึง 999
    messagebox.showinfo(title="Good luck", message="Have a good day! %03d " %(r_3digit))

def Random6Digit():
    """6 digit number random function"""
    r_6digit = random.randint(1, 1000000) # สุ่มเลข 000001 ถึง 999999
    messagebox.showinfo(title="Good luck", message="Have a beautiful day! %06d" %(r_6digit))

def RandomTossCoin():
    """Toss coin heads or tails function"""
    r_coin = random.choice(["Heads", "Tails"]) # สุ่มหัว, ก้อย
    messagebox.showinfo(title="Good luck", message="toss coins : " + r_coin)

def RandomPassword():
    """Password random function"""
    character = "abdcefghijklmnopqrstuvwxyz012345678970ABDCEFGHIJKLMNOPQRSTUVWXYZ_" # string อักขระสำหรับสุ่ม
    r_lenght = random.randint(8, 13) # len ของ password เป็นสุ่ม
    password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    while not password.isidentifier():
        password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    condition = messagebox.askyesnocancel(title='Your password', message='Press "Yes" to print password'.center(45) + '\n' + 'Press "No" to try a new one'.center(45) + '\n' + '\n' + f'{password}'.center(45))
    if condition == True:
        print('This is your password >>>>>>>>', (password + " ").ljust(20, "<")) # กด "Yes" เพื่อ print ข้อมูลมาใช้
        # RandomPassword()
    elif condition == False:
        RandomPassword() # กด "No" เพื่อสุ่ม password ใหม่อีกรอบ

def RandomMenu():
    """Food random function"""
    menu_ls = ['Stewed pork leg', 'Pork panang curry', 'Fried rice', 'Beef curry', 'Papaya salad',\
            'Chicken wings', 'Chicken legs', 'Grilled pork neck', 'Pan fried seafood', 'Thai Basil Chicken ',\
            'Fried pork with garlic', 'Fermented fish spicy dip', 'Steamed egg', 'Stuffed egg', 'Son-in-law Eggs',\
            'Red pork over rice', 'Chicken rice', 'American fried rice', 'Pad thai', 'Dried noodles', 'Noodles soup',\
            'Egg noodles', 'American fried rice', 'Minced pork omelet', 'Fried egg', 'omelet', 'Stir fried vegetables',\
            'Seafood salad', 'Curry-fried fish', 'Chicken curry', 'Pork curry'] # รายการอาหารที่จะสุ่ม
    menu_select = random.choice(menu_ls) # สุ่มอาหารจาก menu_ls มาหนึ่งรายการ
    select = messagebox.askretrycancel(title="Menu", message="Menu for your meal: %s" %(menu_select))
    if select == True:
        RandomMenu() # กด retry เพื่อสุ่มอาหารใหม่อีกรอบ

def RandomMusicPlaylist():
    """Music playlist random function (YouTube URL)"""
    r_music = ["https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10"\
            , "https://www.youtube.com/watch?v=Nj2U6rhnucI&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=11"\
            , "https://www.youtube.com/watch?v=dqRZDebPIGs&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=12"\
            , "https://www.youtube.com/watch?v=VF-r5TtlT9w&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=15"\
            , "https://www.youtube.com/watch?v=9HDEHj2yzew&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=17"] # ลิงค์ของรายการเพลง (YouTube)
    webbrowser.open_new_tab(random.choice(r_music)) # สุ่มรายการเพลงใน browser ของผู้ใช้โดยเปิด Tab ใหม่

def RandomMiniGames():
    """Mini games random function (.IO)"""
    r_games = ["https://agar.io/"\
            , "https://krunker.io/"\
            , "https://paper-io.com/?referer=paper.io&channel=11"\
            , "http://slither.io/"\
            , "https://diep.io/"\
            , "https://surviv.io/"] # ลิงค์ของมินิเกมส์ .io
    webbrowser.open_new_tab(random.choice(r_games)) # สุ่มมินิเกมส์ใน browser ของผู้ใช้โดยเปิด Tab ใหม่

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # self.pack(fill=BOTH, expand=1)
        self.pack(expand=True)
        button1 = Button(self, text="Buy a Thai Lottery", font="72", fg="#000000", bg="#ffb3ba", borderwidth="5", height=5, width=20, command=Random6Digit) # ปุ่มสุ่มเลข6หลัก
        button2 = Button(self, text="Select your meal", font="72", fg="#000000", bg="#ffdfba", borderwidth="5", height=5, width=20, command=RandomMenu) # ปุ่มสุ่มอาหาร
        button3 = Button(self, text="Password random", font="72", fg="#000000", bg="#ffffba", borderwidth="5", height=5, width=20, command=RandomPassword) # ปุ่มสุ่ม Password
        button4 = Button(self, text="Listen to music", font="72", fg="#000000", bg="#baffc9", borderwidth="5", height=5, width=20, command=RandomMusicPlaylist) # ปุ่มสุ่มเพลง
        button5 = Button(self, text="Play a minigame", font="72", fg="#000000", bg="#957dad", borderwidth="5", height=5, width=20, command=RandomMiniGames) # ปุ่มสุ่มมินิเกมส์
        # ตำแหน่งของปุ่ม
        button1.grid(row=1, column=1, padx=30, pady=30)
        button2.grid(row=1, column=2, padx=30, pady=30)
        button3.grid(row=2, column=1, padx=30, pady=30)
        button4.grid(row=2, column=2, padx=30, pady=30)
        button5.grid(row=3, column=1, padx=30, pady=30)

root = Tk()
root.configure(background="light blue")
root.title("Let's me decide for your...")
root.geometry("680x640")

app = Window(root)
root.mainloop()
