import tkinter as tk
from tkinter import ttk

def add_project():
    name = name_entry.get()
    project_manager = manager_entry.get()  

    table.insert('','end', values=(name, project_manager))

window = tk.Tk()
window.title("My App")

window.geometry('800x250+300+100') #가로x세로+x좌표+y좌표
window.resizable(True, True)

name_label = tk.Label(window, text = "학원 이름")
name_label.grid(column = 1, row = 0)
name_entry = tk.Entry(window)
name_entry.grid(column = 2, row = 0)

manager_label = tk.Label(window, text="학원 시간")
manager_label.grid(column = 3, row = 0)
manager_entry = tk.Entry(window)
manager_entry.grid(column = 4, row = 0)

a_label = tk.Label(window, text="                             ")
a_label.grid(column = 6, row = 0)

add_button = tk.Button(window, text="스케쥴 추가", command=add_project)
add_button.grid(column = 5, row = 0)

Monday_label = tk.Label(window, text = "월요일",fg="gray")
Monday_label.grid(column = 0, row = 2)
Tuesday_label = tk.Label(window, text = "화요일",fg="gray")
Tuesday_label.grid(column = 1, row = 2)
Wednesday_label = tk.Label(window, text = "수요일",fg="gray")
Wednesday_label.grid(column = 2, row = 2)
Thursday_label = tk.Label(window, text = "목요일",fg="gray")
Thursday_label.grid(column = 3, row = 2)
Friday_label = tk.Label(window, text = "금요일",fg="gray")
Friday_label.grid(column = 4, row = 2)
Saturday_label = tk.Label(window, text = "토요일",fg="sky blue")
Saturday_label.grid(column = 5, row = 2)
Sunday_label = tk.Label(window, text = "일요일",fg="red")
Sunday_label.grid(column = 6, row = 2)

listbox = tk.Listbox(window, selectmode='extended', height=0)
listbox.insert(0,"월요일")
listbox.insert(1,"화요일")
listbox.insert(2,"수요일")
listbox.insert(3,"목요일")
listbox.insert(4,"금요일")
listbox.insert(5,"토요일")
listbox.insert(6,"일요일")
listbox.grid(column = 0, row = 0)

M1_label = tk.Label(window, text=' ')
M1_label.grid(column = 0, row = 3)
M2_label = tk.Label(window, text=' ')
M2_label.grid(column = 0, row = 4)
M3_label = tk.Label(window, text=' ')
M3_label.grid(column = 0, row = 5)
M4_label = tk.Label(window, text=' ')
M4_label.grid(column = 0, row = 6)
M5_label = tk.Label(window, text=' ')
M5_label.grid(column = 0, row = 7)

H1_label = tk.Label(window, text=' ')
H1_label.grid(column = 1, row = 3)
H2_label = tk.Label(window, text=' ')
H2_label.grid(column = 1, row = 4)
H3_label = tk.Label(window, text=' ')
H3_label.grid(column = 1, row = 5)
H4_label = tk.Label(window, text=' ')
H4_label.grid(column = 1, row = 6)
H5_label = tk.Label(window, text=' ')
H5_label.grid(column = 1, row = 7)

W1_label = tk.Label(window, text=' ')
W1_label.grid(column = 2, row = 3)
W2_label = tk.Label(window, text=' ')
W2_label.grid(column = 2, row = 4)
W3_label = tk.Label(window, text=' ')
W3_label.grid(column = 2, row = 5)
W4_label = tk.Label(window, text=' ')
W4_label.grid(column = 2, row = 6)
W5_label = tk.Label(window, text=' ')
W5_label.grid(column = 2, row = 7)

U1_label = tk.Label(window, text=' ')
U1_label.grid(column = 3, row = 3)
U2_label = tk.Label(window, text=' ')
U2_label.grid(column = 3, row = 4)
U3_label = tk.Label(window, text=' ')
U3_label.grid(column = 3, row = 5)
U4_label = tk.Label(window, text=' ')
U4_label.grid(column = 3, row = 6)
U5_label = tk.Label(window, text=' ')
U5_label.grid(column = 3, row = 7)

F1_label = tk.Label(window, text=' ')
F1_label.grid(column = 4, row = 3)
F2_label = tk.Label(window, text=' ')
F2_label.grid(column = 4, row = 4)
F3_label = tk.Label(window, text=' ')
F3_label.grid(column = 4, row = 5)
F4_label = tk.Label(window, text=' ')
F4_label.grid(column = 4, row = 6)
F5_label = tk.Label(window, text=' ')
F5_label.grid(column = 4, row = 7)

S1_label = tk.Label(window, text=' ')
S1_label.grid(column = 5, row = 3)
S2_label = tk.Label(window, text=' ')
S2_label.grid(column = 5, row = 4)
S3_label = tk.Label(window, text=' ')
S3_label.grid(column = 5, row = 5)
S4_label = tk.Label(window, text=' ')
S4_label.grid(column = 5, row = 6)
S5_label = tk.Label(window, text=' ')
S5_label.grid(column = 5, row = 7)

N1_label = tk.Label(window, text=' ')
N1_label.grid(column = 6, row = 3)
N2_label = tk.Label(window, text=' ')
N2_label.grid(column = 6, row = 4)
N3_label = tk.Label(window, text=' ')
N3_label.grid(column = 6, row = 5)
N4_label = tk.Label(window, text=' ')
N4_label.grid(column = 6, row = 6)
N5_label = tk.Label(window, text=' ')
N5_label.grid(column = 6, row = 7)

window.mainloop()