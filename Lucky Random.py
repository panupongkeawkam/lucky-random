  
from tkinter import *
from tkinter import messagebox
import random, string, webbrowser


def Random6Digit():
    """สุ่มเลข 6 หลัก"""
    r_6digit = random.randint(1, 1000000) # สุ่มเลข 000001 ถึง 999999
    messagebox.showinfo(title="Lottery", message="Have a beautiful day! %06d" %(r_6digit)) #แสดง messagebox

def RandomPassword():
    """สุ่ม password"""
    character = "abdcefghijklmnopqrstuvwxyz012345678970ABDCEFGHIJKLMNOPQRSTUVWXYZ_" # string อักขระสำหรับสุ่ม
    r_lenght = random.randint(8, 13) # len ของ password เป็นสุ่ม
    password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    while not password.isidentifier():
        password = "".join(random.sample(character, r_lenght)) # สลับที่ตัวอักษรของ password เป็นสุ่ม
    condition = messagebox.askyesnocancel(title='Password', message='Press "Yes" to print password'.center(45) + '\n' + 'Press "No" to try a new one'.center(45) + '\n' + '\n' + f'{password}'.center(45))
    if condition == True:
        print('This is your password >>>>>>>>', (password + " ").ljust(20, "<")) # กด "Yes" เพื่อ print ข้อมูลมาใช้
        # RandomPassword()
    elif condition == False:
        RandomPassword() # กด "No" เพื่อสุ่ม password ใหม่อีกรอบ

def RandomMenu():
    """สุ่มเมนูอาหาร"""
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
    """สุ่มเพลง (YouTube URL)"""
    r_music = ["https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10"\
            , "https://www.youtube.com/watch?v=Nj2U6rhnucI&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=11"\
            , "https://www.youtube.com/watch?v=dqRZDebPIGs&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=12"\
            , "https://www.youtube.com/watch?v=VF-r5TtlT9w&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=15"\
            , "https://www.youtube.com/watch?v=9HDEHj2yzew&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=17"] # ลิงค์ของรายการเพลง (YouTube)
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
def RandomSort():
    '''สุ่มวิธีการ sort'''
    def FunctionSort():
        ''' ฟังก์ชัน sort'''
        times = ent_lenght.get()
        ans = []
        lst = ['Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Linear Search', 'Binary Search']
        if times in ['1' ,'2', '3', '4', '5', '6', '7']:
            for _ in range(int(times)):
                txt = random.choice(lst)
                lst.remove(txt)
                ans.append(txt)
            lbl_result["text"] = " , ".join(ans)
        else:
            messagebox.showerror(title="Error", message="Must be integer 1-7")

    window = Tk()
    window.title("Sort Test Random")
    frm_entry = Frame(master=window)
    ent_lenght = Entry(master=frm_entry, width=10)
    lbl_lenght = Label(master=frm_entry, text="How many test you want to randomize? (1-7)")
    lbl_lenght.grid(row=1, column=0, sticky="w")
    ent_lenght.grid(row=1, column=1, sticky="w")
    btn_rando = Button(master=window, text='Radomize', command=FunctionSort)
    lbl_result = Label(master=window, text="You need to do...")
    frm_entry.grid(row=1, column=0, padx=10)
    btn_rando.grid(row=1, column=1, pady=10)
    lbl_result.grid(row=2, column=0, padx=10)
    window.mainloop()


    FunctionSort()
class Window(Frame):
    '''GUI'''

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        #คุณสมบัติของปุ่ม
        self.pack(expand=True)
        button1 = Button(self, text="Lottery", font="20", fg="#EAECEE",activebackground="#fe6612", activeforeground="#fe6612", bg="#21618C", height=2, width=9, command=Random6Digit) # ปุ่มสุ่มเลข6หลัก
        button2 = Button(self, text="Menu", font="20", fg="#000000", activebackground="#fe6612", activeforeground="#fe6612", bg="#85C1E9", height=2, width=9, command=RandomMenu) # ปุ่มสุ่มเลข6หลัก
        button3 = Button(self, text="Password", font="20", fg="#EAECEE", activebackground="#fe6612", activeforeground="#fe6612", bg="#3498DB", height=2, width=9, command=RandomPassword) # ปุ่มสุ่มเลข6หลัก
        button4 = Button(self, text="Song", font="20", fg="#EAECEE", activebackground="#fe6612", activeforeground="#fe6612", bg="#5DADE2", height=2, width=9, command=RandomMusicPlaylist) # ปุ่มสุ่มเลข6หลัก
        button5 = Button(self, text="Minigame", font="20", fg="#000000", activebackground="#fe6612", activeforeground="#fe6612", bg="#3498DB", height=2, width=9, command=RandomMiniGames) # ปุ่มสุ่มเลข6หลัก
        button6 = Button(self, text="Sort", font="20", fg="#EAECEE", activebackground="#fe6612", activeforeground="#fe6612", bg="#2E86C1", height=2, width=9, command=RandomSort) # ปุ่มสุ่มเลข6หลัก
        # ตำแหน่งของปุ่ม
        button1.grid(row=1, column=1, padx=20, pady=20)
        button2.grid(row=1, column=2, padx=20, pady=20)
        button3.grid(row=1, column=3, padx=20, pady=20)
        button4.grid(row=2, column=1, padx=20, pady=20)
        button5.grid(row=2, column=2, padx=20, pady=20)
        button6.grid(row=2, column=3, padx=20, pady=20)
root = Tk() #???
root.configure(background="#f0f0f0") #background
root.title("Let's me decide for your...") #title
root.geometry("500x250") #resolution

app = Window(root) #เรียก class
root.mainloop() #???