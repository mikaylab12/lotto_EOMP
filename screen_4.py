# Mikayla Beelders End Of Module Project
# converting currency screen
from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk

converting_screen = Tk()
converting_screen.geometry("800x800")
converting_screen.title("Banking Details")
converting_screen.config(bg="#fcf00d")



class Earnings:
    def __init__(self, master):
        # labels for all 3 sets to be displayed.
        self.first_set = Label(master, text="", bg="#bdbdbd", width=15, font=('Arial', 13))
        self.first_set.place(relx=0.15, rely=0.72)
        self.second_set = Label(master, text="", bg="#bdbdbd", width=15, font=('Arial', 13))
        self.second_set.place(relx=0.4, rely=0.72)
        self.third_set = Label(master, text="", bg="#bdbdbd", width=15, font=('Arial', 13))
        self.third_set.place(relx=0.65, rely=0.72)
        # winning numbers display
        self.winningNums = Label(master, text="", bg="#bdbdbd", width=20, font=('Arial', 18, 'bold'))
        self.winningNums.place(relx=0.35, rely=0.8)

        # play button
        play_btn = Button(converting_screen, borderwidth=5, padx=23, pady=10, fg="black", bg="#09bd27", text="Play"
                          , font=("Arial", 17, "bold"))
        play_btn.place(relx=0.1, rely=0.9)
        # play again button
        playAgain_btn = Button(converting_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="#bdbdbd",
                               text="Play Again", font=("Arial", 17, "bold"))
        playAgain_btn.place(relx=0.26, rely=0.9)
        # claim button
        claim_btn = Button(converting_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="#adacac",
                           text="Claim Prize", font=("Arial", 17, "bold"))
        claim_btn.place(relx=0.5, rely=0.9)
        # exit button
        exit_btn = Button(converting_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="red", text="Exit",
                          font=("Arial", 17, "bold"))
        exit_btn.place(relx=0.755, rely=0.9)
    # Python program to create a table




converting_screen.mainloop()
