"""TkinterRandomSortTest"""
import tkinter as tk
import random as ra
#RandomTestSort
def randomtest():
    times = int(ent_lenght.get())
    ans = []
    lst = ['Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Quick Sort', 'Merge Sort', 'Linear Search', 'Binary Search']
    for _ in range(times):
        txt = ra.choice(lst)
        lst.remove(txt)
        ans.append(txt)
    lbl_result["text"] = " ".join(ans)

window = tk.Tk()
window.title("Sort Test Random")
frm_entry = tk.Frame(master=window)
ent_lenght = tk.Entry(master=frm_entry, width=10)
lbl_lenght = tk.Label(master=frm_entry, text="How many test you want to random?")
lbl_lenght.grid(row=0, column=0, sticky="e")
ent_lenght.grid(row=0, column=1, sticky="w")
btn_rando = tk.Button(master=window,
text='Generate Now!',
command=randomtest)
lbl_result = tk.Label(master=window, text="You need to do...")
frm_entry.grid(row=0, column=0, padx=10)
btn_rando.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
window.mainloop()


randomtest()