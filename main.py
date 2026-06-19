import tkinter as tk
from constants import *


def add():
    pass

window = tk.Tk()
window.title('Daily Quest v0.1.0')
window.minsize(height= 500, width= 600)
window.config(padx= 20, pady= 20, bg=TEAL_BLUE)

title_label = tk.Label(text='Push-ups', bg=TEAL_BLUE,
                       fg=CREAM_SAND, font= TITLE_FONT)
title_label.grid(row= 0, column= 0, columnspan= 3)

progress_label = tk.Label(text='Progress: 12930 / 20000', bg=TEAL_BLUE,
                          fg=CREAM_SAND, font= PROGRESS_FONT)
progress_label.config(padx= 20, pady= 50)
progress_label.grid(row= 1, column= 0, columnspan= 3)

add_today_label = tk.Label(text='Add today:', bg=TEAL_BLUE,
                           fg=CREAM_SAND, font= PROGRESS_FONT)
add_today_label.grid(row= 2, column= 0)

entry = tk.Entry(width= 20, bg= CREAM_SAND)
entry.grid(row= 2, column= 1)

add_button = tk.Button(text='Add', command=add, bg=LIGHT_TURQUOISE)
add_button.config(padx= 20, pady= 0)
add_button.grid(row=2, column=2, padx= 30)




window.mainloop()
