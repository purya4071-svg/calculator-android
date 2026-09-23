import tkinter as tk
from tkinter import colorchooser

window = tk.Tk()
window.title("ماشین حساب")

width = 360
height = 650

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(True, True)
window.configure(bg="#202124")


def change_background():
    color = colorchooser.askcolor(title="انتخاب رنگ پس زمینه")

    if color[1]:
        window.configure(bg=color[1])


def click(text):

    if text == "C":
        entry.delete(0, tk.END)

    elif text == "⌫":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])

    elif text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "خطا")

    else:
        entry.insert(tk.END, text)


entry = tk.Entry(
    window,
    font=("Arial", 30, "bold"),
    justify="right",
    bd=8,
    relief="sunken",
    bg="#303134",
    fg="white"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=12,
    pady=15,
    ipady=15,
    sticky="nsew"
)


buttons = [
    ("C", 1, 0, "#d9534f"),
    ("⌫", 1, 1, "#5f6368"),
    ("/", 1, 2, "#f0a500"),
    ("*", 1, 3, "#f0a500"),

    ("7", 2, 0, "#3c4043"),
    ("8", 2, 1, "#3c4043"),
    ("9", 2, 2, "#3c4043"),
    ("-", 2, 3, "#f0a500"),

    ("4", 3, 0, "#3c4043"),
    ("5", 3, 1, "#3c4043"),
    ("6", 3, 2, "#3c4043"),
    ("+", 3, 3, "#f0a500"),

    ("1", 4, 0, "#3c4043"),
    ("2", 4, 1, "#3c4043"),
    ("3", 4, 2, "#3c4043"),
    ("=", 4, 3, "#34a853"),

    ("0", 5, 0, "#3c4043"),
    (".", 5, 1, "#3c4043")
]


for text, row, column, color in buttons:

    button = tk.Button(
        window,
        text=text,
        font=("Arial", 20, "bold"),
        fg="white",
        bg=color,
        activebackground=color,
        activeforeground="white",
        bd=3,
        relief="raised",
        width=5,
        height=2,
        command=lambda b=text: click(b)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


color_button = tk.Button(
    window,
    text="🎨  انتخاب رنگ پس زمینه",
    font=("Arial", 14, "bold"),
    bg="#5f6368",
    fg="white",
    activebackground="#777777",
    activeforeground="white",
    bd=3,
    relief="raised",
    command=change_background
)

color_button.grid(
    row=6,
    column=0,
    columnspan=4,
    padx=10,
    pady=10,
    sticky="nsew"
)


for column in range(4):
    window.grid_columnconfigure(column, weight=1)

for row in range(1, 7):
    window.grid_rowconfigure(row, weight=1)


window.mainloop()
