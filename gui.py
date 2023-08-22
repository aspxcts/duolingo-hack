import tkinter as tk
import sys
from main import mainscript


def fire():
    mainscript()


def kill():
    sys.exit()


def main():
    root = tk.Tk()
    root.title("fire da button")
    root.geometry("800x800")

    firebutton = tk.Button(root, text="FIRE", bg="green", fg="white", padx=350, pady=50, font=("Helvetica", 14),
                           command=fire)
    firebutton.place(x=20, y=640)
    killbutton = tk.Button(root, text="KILL", bg="red", fg="white", padx=350, pady=50, font=("Helvetica", 14),
                           command=kill)
    killbutton.place(x=20, y=20)
    res1200 = tk.Button(root, text="1980x1200", bg="white", fg="black", padx=50, pady=50, font=("Helvetica", 14))
    res1080 = tk.Button(root, text="1980x1080", bg="white", fg="black", padx=50, pady=50, font=("Helvetica", 14))
    res1200.place(x=40, y=200)
    res1080.place(x=550, y=200)
    duo = tk.Label(root, text="Duolingo Hack")
    maker = tk.Label(root, text="Made by aspectofsomething")
    duo.config(font=("Courier", 14))
    maker.config(font=("Courier", 14))
    duo.place(x=330, y=200)
    maker.place(x=265, y=250)

    root.mainloop()


main()