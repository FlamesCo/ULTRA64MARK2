import tkinter as tk
from tkinter import filedialog

def open_rom():
    file_path = filedialog.askopenfilename(filetypes=[("ROM Files", "*.z64;*.n64")])
    print(f"Opening ROM: {file_path}")


def settings():
    print("Settings menu")


def about():
    print("About EmulAI64")


app = tk.Tk()
app.geometry("600x400")
app.title("EmulAI64")

menu_bar = tk.Menu(app)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open ROM", command=open_rom)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Controls", command=settings)
settings_menu.add_command(label="Audio", command=settings)
settings_menu.add_command(label="Video", command=settings)
settings_menu.add_command(label="Plug-Ins", command=settings)
menu_bar.add_cascade(label="Settings", menu=settings_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

app.config(menu=menu_bar)

app.mainloop()

## @FLAMES LLC LILY @ FLAMES 20XX FLAMES AI AI RIGHTS RESERVED [c] 20XX
