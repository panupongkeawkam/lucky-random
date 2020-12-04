import random
import string
import tkinter as tk

def get_random_alphanumeric_string():
    """รับเลขมาแรนด้อม เอาโค้ดวิธีการสุ่มมาจาก https://pynative.com/python-generate-random-string/
        ส่วนการปรับแก้ดูเทียบกับ https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app"""
    all_lenght = ent_lenght.get()
    letters_count = int(all_lenght)//2
    digits_count = int(all_lenght)-letters_count
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    lbl_result["text"] = final_string

"""ตรง tkinter เอามาจากโปรแกรมเปลี่ยนอุณหภูมิที่เว็บ https://realpython.com/python-gui-tkinter/#building-a-temperature-converter-example-app มาแปลง"""
window = tk.Tk()
window.title("Random Password")
frm_entry = tk.Frame(master=window)
lbl_lenght = tk.Label(master=frm_entry, text="Password Lenght")
ent_lenght = tk.Entry(master=frm_entry, width=10)
lbl_lenght.grid(row=0, column=0, sticky="e")
ent_lenght.grid(row=0, column=1, sticky="w")
btn_gen = tk.Button(
    master=window,
    text="Generate",
    command=get_random_alphanumeric_string
)
lbl_result = tk.Label(master=window, text="Your Password")
frm_entry.grid(row=0, column=0, padx=10)
btn_gen.grid(row=1, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
window.mainloop()


