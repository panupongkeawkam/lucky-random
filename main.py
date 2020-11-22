from tkinter import *
from tkinter import messagebox
import tkinter.messagebox


# ****** GLOBAL VARIABLES ******

objects = []
window = Tk()
window.withdraw()
window.title('Email Storage')

class popupWindow(object):

    loop = False
    attempts = 0

    def __init__(self, master):
        '''Password windows'''
        top = self.top = Toplevel(master)
        top.title('Password input') #สำหรับใส่ Title
        top.geometry('{}x{}'.format(250, 100)) #ปรับขนาด windows
        top.resizable(width=False, height=False) #ล็อคขนาดของ windows
        self.l = Label(top, text=" Password: ", font=('Courier', 14), justify=CENTER) #ปรับข้อความ
        self.l.pack()
        self.e = Entry(top, show='*', width=30) #password text
        self.e.pack(pady=7)
        self.b = Button(top, text='Enter', command=self.cleanup, font=('Courier', 14))#ปรับปุ่ม Submit
        self.b.pack()

    def cleanup(self):
        '''Password Process'''
        self.value = self.e.get()
        access = '000' #password

        if self.value == access: #กรณีใส่ถูก
            self.loop = True
            self.top.destroy() #ลบ input windows
            window.deiconify()#เด้ง info input windows
        else: #กรณีใส่ผิด
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts)) #ข้อความกรณีใส่ผิด

class entity_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):
        '''Encrypted process'''
        f = open('emails.txt', "a") #ตัวแปรสำหรับเปิดไฟล์ email.txt เพื่อเขียนข้อมูล
        n = self.name #ตัวแปรสำหรับ name
        e = self.email # ,,     email
        p = self.password # ,,  password

        encryptedN = "" #ตัวแปรสำหรับ encrypted name
        encryptedE = "" #         , ,       email
        encryptedP = "" #         , ,       password
        for letter in n: #เข้ารหัส name
            if letter == ' ': #กรณีมีช่องว่าง
                encryptedN += ' ' #ก็ใส่ช่องว่าง ไม่เข้ารหัส
            else:
                encryptedN += chr(ord(letter) + 5) #ขยับตัวอักษรในเลขฐานไป 5 หน่วย

        for letter in e: #เข้ารหัส email
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p: #เข้ารหัส password
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n') #เขียนข้อมูลที่เข้ารหัสแล้วลงในไฟล์ email.txt
        f.close() #ปิดไฟล์ email.txt


class entity_display:

    def __init__(self, master, n, e, p, i):
        '''ถอดรหัสและแสดงผลข้อมูล'''
        self.password = p #password
        self.name = n #name
        self.email = e #email
        self.window = master #หน้าต่าง
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name: #ถอดรหัส name
            if letter == ' ': #ถ้าเป็นช่องว่าง
                dencryptedN += ' ' #ก็ใส่ช่องว่างไม่ต้องเปลี่ยน
            else:
                dencryptedN += chr(ord(letter) - 5) #ขยับตัวอักษรในเลขฐานกลับมา 5 หน่วย

        for letter in self.email: #ถอดรหัส email
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password: #ถอดรหัส password
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)
        '''แสดงผลออกหน้าจอ'''

        self.label_name = Label(self.window, text=dencryptedN, font=('Courier', 14)) #ปรับ name
        self.label_email = Label(self.window, text=dencryptedE, font=('Courier', 14)) #ปรับ email
        self.label_pass = Label(self.window, text=dencryptedP, font=('Courier', 14)) #ปรับ password
        self.deleteButton = Button(self.window, text='X', fg='red', command=self.delete) #ปรับปุ่มลบ

    def display(self):
        '''แสดงชนิดข้อมูล'''
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=1)
        self.label_pass.grid(row=6 + self.i, column=2, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        '''Delete Process'''
        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?') #เด้งหน้าต่างใหม่
        '''Decision'''

        if answer == 'yes': #กรณีตอบ yes
            pass
            for i in objects: #ลบข้อมูลแสดงผล
                i.destroy()

            f = open('emails.txt', 'r') #เปิดไฟล์เพื่ออ่าน
            lines = f.readlines() #ตัวแปรสำหรับอ่านไฟล์
            f.close() #ปิดไฟล์

            f = open('emails.txt', "w") #เปิดไฟล์เพื่อเขียน
            count = 0

            for line in lines: #scan หาข้อมูลที่ต้องการทีละบรรทัด
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        '''ลบข้อมูลใน display'''
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


# ******* FUNCTIONS *********


def onsubmit():
    '''หน้าต่างsubmit'''
    m = email.get() #ดึง email
    p = password.get() #ดึง password
    n = name.get() #ดึง name
    e = entity_add(window, n, p, m) #หน้าต่างใหม่
    e.write() #เขียนข้อมูล
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + n + '\nEmail: ' + m + '\nPassword: ' + p) #แสดงผลในหน้าต่าง submit
    readfile()


def clearfile():
    f = open('emails.txt', "w")
    f.close()


def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


# ******* GRAPHICS *********

m = popupWindow(window)

entity_label = Label(window, text='Add Entity', font=('Courier', 18))
name_label = Label(window, text='Name: ', font=('Courier', 14))
email_label = Label(window, text='Email: ', font=('Courier', 14))
pass_label = Label(window, text='Password: ', font=('Courier', 14))
name = Entry(window, font=('Courier', 14))
email = Entry(window, font=('Courier', 14))
password = Entry(window, show='*', font=('Courier', 14))
submit = Button(window, text='Add Email', command=onsubmit, font=('Courier', 14))

entity_label.grid(columnspan=3, row=0)
name_label.grid(row=1, sticky=E, padx=3)
email_label.grid(row=2, sticky=E, padx=3)
pass_label.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

name_label2 = Label(window, text='Name: ', font=('Courier', 14))
email_label2 = Label(window, text='Email: ', font=('Courier', 14))
pass_label2 = Label(window, text='Password: ', font=('Courier', 14))

name_label2.grid(row=5)
email_label2.grid(row=5, column=1)
pass_label2.grid(row=5, column=2)

readfile()

window.mainloop()
