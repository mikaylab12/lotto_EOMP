# Mikayla Beelders End Of Module Project
# currency conversion screen
from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
currency_conversion_screen = Tk()
currency_conversion_screen.geometry("800x800")
currency_conversion_screen.title("Currency Conversion")
currency_conversion_screen.config(bg="#fcf00d")
# adding an image
canvas = Canvas(currency_conversion_screen, width=500, height=300, bg="#fcf00d", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.3, rely=0.02)
img_numBalls = ImageTk.PhotoImage(Image.open("lotto_nums.jpeg"))
canvas.create_image(150, 5, anchor=N, image=img_numBalls)


winnings_screen.mainloop()