from tkinter import *
from tkinter import messagebox
import random, webbrowser

def Random6Digit():
    """สุ่มเลข 6 หลัก"""
    r_6digit = random.randint(1, 1000000) # สุ่มเลข 000001 ถึง 999999
    condition = messagebox.askretrycancel(title="Lottery", \
    message="Have a beautiful day!\n\n" + " "*12 + "%06d" %(r_6digit)) #แสดง messagebox
    if condition == True: #ปุ่ม retry
        Random6Digit()

def RandomMenu():
    """สุ่มเมนูอาหาร"""
    menu_ls = ['Stewed pork leg', 'Pork panang curry', 'Fried rice', 'Beef curry', 'Papaya salad',\
            'Chicken wings', 'Chicken legs', 'Grilled pork neck', 'Pan fried seafood', 'Thai Basil Chicken ',\
            'Fried pork with garlic', 'Fermented fish spicy dip', 'Steamed egg', 'Stuffed egg', 'Son-in-law Eggs',\
            'Red pork over rice', 'Chicken rice', 'American fried rice', 'Pad thai', 'Dried noodles', 'Noodles soup',\
            'Egg noodles', 'American fried rice', 'Minced pork omelet', 'Fried egg', 'omelet', 'Stir fried vegetables',\
            'Seafood salad', 'Curry-fried fish', 'Chicken curry', 'Pork curry', 'Sliced grilled beef salad',\
            'Congee', 'Tom Yum Kung', 'Fried mussel pancakes', 'Crisp fried calamari', 'Spicy noodle salad'] # รายการอาหารที่จะสุ่ม
    menu_select = random.choice(menu_ls) # สุ่มอาหารจาก menu_ls มาหนึ่งรายการ
    select = messagebox.askretrycancel(title="Menu", \
        message="Menu for your meal\n\n" + f"{menu_select}".center(21))
    if select == True: #ปุ่ม retry
        RandomMenu()

def RandomPassword():
    """สุ่ม password"""
    character = "abdcefghijklmnopqrstuvwxyz012345678970ABDCEFGHIJKLMNOPQRSTUVWXYZ_" # string อักขระสำหรับสุ่ม
    r_lenght = random.randint(8, 13) # len ของ password เป็นสุ่ม
    password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    while not password.isidentifier():
        password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    condition = messagebox.askyesnocancel(title='Password', \
        message='Press "Yes" to print password'.center(45) + '\n' + \
        'Press "No" to try a new one'.center(45) + '\n' + '\n' + f'{password}'.center(45))
    if condition == True:
        print('>>>>>>>', (password + " ").ljust(20, "<")) # กด "Yes" เพื่อ print ข้อมูลมาใช้
        RandomPassword()
    elif condition == False: #ปุ่ม no
        RandomPassword()

def RandomMusicPlaylist():
    """สุ่มเพลง (YouTube URL)"""
    r_music = ["https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10"\
            , "https://www.youtube.com/watch?v=Nj2U6rhnucI&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=11"\
            , "https://www.youtube.com/watch?v=dqRZDebPIGs&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=12"\
            , "https://www.youtube.com/watch?v=VF-r5TtlT9w&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=15"\
            , "https://www.youtube.com/watch?v=9HDEHj2yzew&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=17"\
            , "https://www.youtube.com/watch?v=8EJ3zbKTWQ8&list=PL9NY5axt700EWfbbdSadvbBxqHUMsl6Nr"\
            , "https://www.youtube.com/watch?v=v2AC41dglnM&list=PLQlc99hV-nkGWDaG-gJxwOfqp8jxyHaaQ"\
            , "https://www.youtube.com/watch?v=PDSkFeMVNFs&list=PL0y9YRP4fumshMtovIvlgynR5ZMojDNPv"] # ลิงค์ของรายการเพลง (YouTube)
    webbrowser.open_new_tab(random.choice(r_music)) # สุ่มรายการเพลงใน browser ของผู้ใช้โดยเปิด Tab ใหม่

def RandomMiniGames():
    """สุ่ม Minigame"""
    r_games = ["https://agar.io/"\
            , "https://krunker.io/"\
            , "https://paper-io.com/?referer=paper.io&channel=11"\
            , "http://slither.io/"\
            , "https://diep.io/"\
            , "https://surviv.io/"] # ลิงค์ของมินิเกมส์ .io
    webbrowser.open_new_tab(random.choice(r_games)) # สุ่มมินิเกมส์ใน browser ของผู้ใช้โดยเปิด Tab ใหม่

def RandomStudents():
    '''สุ่มรหัสนักศึกษา'''
    def FunctionStudents():
        ''' ฟังก์ชันสุ่มรหัสนักศึกษา'''
        times = ent_lenght.get() # Input range
        lst_result = set() # ตัวแปรเพือนำมาเก็บคำตอบ
        if times in [str(i) for i in range(1, 11)]: # ดัก test case
            while len(lst_result) < int(times): # วิธีการที่ใช้ สุ่ม
                charge = ("63070%03d" %random.randint(1, 193))
                lst_result.add(charge)
            lst_result = sorted(lst_result)
            if int(times) >= 6:
                lst_result.insert(5, "\n")
            answer["text"] = "  ".join(lst_result)
        else: # ดัก Error
            messagebox.showerror(title="Error", message="Must be integer 1-10")

    '''Student IDs Window setup'''
    root2 = Tk()# เรียกใช้ import tkinter
    root2.title("Students ID")# ชื่อของ tkinter
    frm_entry = Frame(master=root2)
    ent_lenght = Entry(master=frm_entry, width=5)#ขนาดของช่องรับ Input
    btn_rando = Button(master=root2, bg="#21618C", fg="#EAECEE", height=1, width=16, font=8, text='Radomize', \
        command=FunctionStudents)#ปุ่มที่ใช้ในการเรียกฟังก์ชัน
    lbl_lenght = Label(master=frm_entry, text="How many students you want to randomize? (1-10)  ")# format input
    answer = Label(master=root2, text="Lucky guys is...") # ตำแหน่งที่ คำตอบจะออกมา
    '''ขนาดและตำแหน่ง'''
    lbl_lenght.grid(row=1, column=0,) # ตำแหน่งของ format input
    ent_lenght.grid(row=1, column=1,) # ตำแหน่งของ ช่องรับ Input
    frm_entry.grid(row=1, column=0, pady=8, padx=12)
    btn_rando.grid(row=2, column=0, pady=8, padx=12)#ตำแหน่งและขนาดชองปุ่มกดเริ่มการสุ่ม
    answer.grid(row=3, column=0, pady=8, padx=16)#ตำแหน่งและขนาดช่องของคำตอบ
    root2.mainloop() # ทำให้ Tkinter แสดงผล

class Window(Frame):
    '''GUI'''

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        #คุณสมบัติของปุ่ม
        self.pack(expand=True)
        label = Label(self, text="👀 RANDOM 👀", font=72, fg="#fe6612")
        button1 = Button(self, text="Lottery", font=16, \
        fg="#EAECEE", bg="#21618C", activebackground="#fe6612", activeforeground="#fe6612", \
        height=2, width=12, command=Random6Digit) # ปุ่มสุ่มเลข6หลัก
        button2 = Button(self, text="Menu", font=16, fg="#2C2C2C", bg="#85C1E9", activebackground="#fe6612", activeforeground="#fe6612", height=2, width=12, command=RandomMenu) # ปุ่มสุ่มเมนูอาหาร
        button3 = Button(self, text="Password", font=16, fg="#EAECEE", bg="#3498DB", activebackground="#fe6612", activeforeground="#fe6612", height=2, width=12, command=RandomPassword) # ปุ่มสุ่มPassword
        button4 = Button(self, text="Song", font=16, fg="#424242", bg="#5DADE2", activebackground="#fe6612", activeforeground="#fe6612", height=2, width=12, command=RandomMusicPlaylist) # ปุ่มสุ่มเพลง
        button5 = Button(self, text="Minigame", font=16, fg="#343434", bg="#3498DB", activebackground="#fe6612", activeforeground="#fe6612", height=2, width=12, command=RandomMiniGames) # ปุ่มสุ่มมินิเกม
        button6 = Button(self, text="Students ID", font=16, fg="#E0E0E0", bg="#2E86C1", activebackground="#fe6612", activeforeground="#fe6612", height=2, width=12, command=RandomStudents) # ปุ่มสุ่มรหัสนักศึกษา
        # ตำแหน่งของปุ่ม
        label.grid(row=0, column=2, pady=12)
        button1.grid(row=1, column=1, padx=16, pady=16)
        button2.grid(row=1, column=2, padx=16, pady=16)
        button3.grid(row=1, column=3, padx=16, pady=16)
        button4.grid(row=2, column=1, padx=16, pady=16)
        button5.grid(row=2, column=2, padx=16, pady=16)
        button6.grid(row=2, column=3, padx=16, pady=16)

root = Tk()
root.configure(background="#f0f0f0") #background
root.title("Let's me decide for your...") #title
root.geometry("540x250") #resolution
app = Window(root) #เรียก class
root.mainloop() #คำสั่งเพื่อใช้ run ขึ้นหน้า Tkinter
