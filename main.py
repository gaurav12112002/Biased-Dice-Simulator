import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Simulator")

dice = ["dice1.png", "dice2.png", "dice3.png",
        "dice4.png", "dice5.png", "dice6.png"]
biased_dice = ["dice1.png", "dice2.png", "dice3.png",
               "dice4.png", "dice5.png", "dice6.png", "dice6.png",
        "dice6.png","dice6.png","dice6.png","dice6.png","dice6.png"]

label = tk.Label(window)
label.place(x=200, y=200)


def dice_roll():
    image = None  # Initialize the image variable

    if dice_type.get() == "Normal":
        image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    elif dice_type.get() == "Biased":
        image = ImageTk.PhotoImage(Image.open(random.choice(biased_dice)))

    label.configure(image=image)
    label.image = image


dice_type = tk.StringVar()
dice_type.set("Normal")

option_menu = tk.OptionMenu(window, dice_type, "Normal", "Biased for 6")
option_menu.place(x=200, y=10)

button = tk.Button(window, text="ROLL", bg="white",
                   font="Times 20 bold", fg="green", command=dice_roll)
button.place(x=200, y=80)

window.mainloop()
