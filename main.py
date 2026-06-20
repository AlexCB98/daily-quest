import json
import tkinter as tk
from tkinter import messagebox
from constants import *
from datetime import date



def add():
    global current

    try:
        value = int(entry.get())

    except ValueError:
        messagebox.showwarning(title='Oupss', message='Make sure you inserted just numbers. ^^')
    else:
        if value > 0:
            current += value

            quest['pushups']['current'] = current

            with open('data.json', 'w') as data:
                json.dump(quest, data, indent=4)

            progress_label.config(text=f'Progress: {current} / {target}')
        else:
            messagebox.showwarning(title='Oupss', message='Please enter a number greater than 0. ^^')

    finally:
        entry.delete(0, tk.END)

try:
    with open('data.json', 'r') as data:
        quest = json.load(data)

except (FileNotFoundError, json.JSONDecodeError):
    quest = {
        "pushups": {
            "current": 0,
            "target": 20000,
            "start_date": str(date.today())
        }
    }

    with open('data.json', 'w') as data:
        json.dump(quest, data, indent= 4)


current    = quest['pushups']['current']
target     = quest['pushups']['target']
start_date = date.fromisoformat(quest['pushups']['start_date'])

today = date.today()

current_day = (today - start_date).days + 1


window = tk.Tk()
window.title('Daily Quest v0.1.0')
window.minsize(height= 500, width= 600)
window.config(padx= 20, pady= 20, bg=TEAL_BLUE)

date_label = tk.Label(
    text=f'Day of progression: {current_day} | Started: {start_date}',
    bg=TEAL_BLUE,
    fg=CREAM_SAND,
    font=PROGRESS_FONT
)

date_label.grid(row= 0, column= 0, columnspan= 3, pady= 20)


title_label = tk.Label(
    text='1. Push-ups',
    bg=TEAL_BLUE,
    fg=CREAM_SAND,
    font= TITLE_FONT
)
title_label.grid(row= 1, column= 0, columnspan= 3)

progress_label = tk.Label(
    text=f'Progress: {current} / {target}',
    bg=TEAL_BLUE,
    fg=CREAM_SAND,
    font= PROGRESS_FONT
)

progress_label.config(padx= 20, pady= 50)
progress_label.grid(row= 2, column= 0, columnspan= 3)

add_today_label = tk.Label(
    text='Add today:',
    bg=TEAL_BLUE,
    fg=CREAM_SAND,
    font= PROGRESS_FONT
)

add_today_label.grid(row= 3, column= 0)

entry = tk.Entry(width= 20, bg= CREAM_SAND)
entry.grid(row= 3, column= 1)

add_button = tk.Button(
    text='Add',
    command=add,
    bg=LIGHT_TURQUOISE
)

add_button.config(padx= 20, pady= 0)
add_button.grid(row=3, column=2, padx= 30)




window.mainloop()
