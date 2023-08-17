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
    root.geometry("400x300")

    firebutton = tk.Button(root, text="FIRE", bg="green", fg="white", padx=20, pady=10, font=("Helvetica", 14),
                           command=fire)
    firebutton.pack(pady=10)
    killbutton = tk.Button(root, text="KILL", bg="red", fg="white", padx=20, pady=10, font=("Helvetica", 14),
                           command=kill)
    killbutton.pack(pady=90)

    root.mainloop()


main()
