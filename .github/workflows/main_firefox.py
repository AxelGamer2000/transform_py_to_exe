import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()
ff = tk.BooleanVar()

checkbox = ttk.Checkbutton(root, text="flatpak run org.mozilla.firefox ?", variable=ff)

def click():
    orig = ["flatpak", "run", "org.mozilla.firefox"] if ff.get() else ["firefox"]
    result = orig + [root.clipboard_get()]

    subprocess.Popen(result)
    root.destroy()

ttk.Button(root, text="Web Search", command=click).pack()
checkbox.pack()

root.mainloop()