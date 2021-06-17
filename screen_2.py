# Mikayla Beelders End Of Module Project
# selecting lotto numbers screen
from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
numberSelection_screen = Tk()
numberSelection_screen.geometry("800x800")
numberSelection_screen.title("Select Your Numbers")
numberSelection_screen.config(bg="#fcf00d")
# adding an image
canvas = Canvas(numberSelection_screen, width=500, height=300, bg="#fcf00d", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.3, rely=0.02)
img_numBalls = ImageTk.PhotoImage(Image.open("lotto_nums.jpeg"))
canvas.create_image(150, 5, anchor=N, image=img_numBalls)
# lotto sets will append to these lists
first_set = []
second_set = []
third_set = []
# all widgets displayed on this window
class Selection:
    def __init__(self, master):
        self.numberSelection_frame = Frame(master, bg="#bdbdbd", width=630, height=450)
        self.numberSelection_frame.place(relx=0.1, rely=0.3)
        # instruction heading
        self.instruction_heading = Label(master, text="Please select your 6 numbers:",
                                         font=("Arial", 13, "bold"), bg="#bdbdbd")
        self.instruction_heading.place(relx=0.13, rely=0.31)
        # number buttons
        self.btn_1 = Button(master, text="1", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(1))
        self.btn_1.place(relx=0.15, rely=0.36)
        self.btn_2 = Button(master, text="2", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(2))
        self.btn_2.place(relx=0.2135, rely=0.36)
        self.btn_3 = Button(master, text="3", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(3))
        self.btn_3.place(relx=0.277, rely=0.36)
        self.btn_4 = Button(master, text="4", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(4))
        self.btn_4.place(relx=0.3405, rely=0.36)
        self.btn_5 = Button(master, text="5", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(5))
        self.btn_5.place(relx=0.404, rely=0.36)
        self.btn_6 = Button(master, text="6", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(6))
        self.btn_6.place(relx=0.4675, rely=0.36)
        self.btn_7 = Button(master, text="7", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(7))
        self.btn_7.place(relx=0.531, rely=0.36)
        self.btn_8 = Button(master, text="8", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(8))
        self.btn_8.place(relx=0.5945, rely=0.36)
        self.btn_9 = Button(master, text="9", padx=15, bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                            self.display_btn(9))
        self.btn_9.place(relx=0.658, rely=0.36)
        self.btn_10 = Button(master, text="10", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(10))
        self.btn_10.place(relx=0.7215, rely=0.36)
        self.btn_11 = Button(master, text="11", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(11))
        self.btn_11.place(relx=0.785, rely=0.36)
        self.btn_12 = Button(master, text="12", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(12))
        self.btn_12.place(relx=0.15, rely=0.42)
        self.btn_13 = Button(master, text="13", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(13))
        self.btn_13.place(relx=0.2135, rely=0.42)
        self.btn_14 = Button(master, text="14", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(14))
        self.btn_14.place(relx=0.277, rely=0.42)
        self.btn_15 = Button(master, text="15", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(15))
        self.btn_15.place(relx=0.3405, rely=0.42)
        self.btn_16 = Button(master, text="16", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(16))
        self.btn_16.place(relx=0.404, rely=0.42)
        self.btn_17 = Button(master, text="17", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(17))
        self.btn_17.place(relx=0.4675, rely=0.42)
        self.btn_18 = Button(master, text="18", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(18))
        self.btn_18.place(relx=0.531, rely=0.42)
        self.btn_19 = Button(master, text="19", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(19))
        self.btn_19.place(relx=0.5945, rely=0.42)
        self.btn_20 = Button(master, text="20", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(20))
        self.btn_20.place(relx=0.658, rely=0.42)
        self.btn_21 = Button(master, text="21", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(21))
        self.btn_21.place(relx=0.7215, rely=0.42)
        self.btn_22 = Button(master, text="22", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(22))
        self.btn_22.place(relx=0.785, rely=0.42)
        self.btn_23 = Button(master, text="23", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(23))
        self.btn_23.place(relx=0.15, rely=0.48)
        self.btn_24 = Button(master, text="24", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(24))
        self.btn_24.place(relx=0.2135, rely=0.48)
        self.btn_25 = Button(master, text="25", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(25))
        self.btn_25.place(relx=0.277, rely=0.48)
        self.btn_26 = Button(master, text="26", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(26))
        self.btn_26.place(relx=0.3405, rely=0.48)
        self.btn_27 = Button(master, text="27", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(27))
        self.btn_27.place(relx=0.404, rely=0.48)
        self.btn_28 = Button(master, text="28", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(28))
        self.btn_28.place(relx=0.4675, rely=0.48)
        self.btn_29 = Button(master, text="29", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(29))
        self.btn_29.place(relx=0.531, rely=0.48)
        self.btn_30 = Button(master, text="30", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(30))
        self.btn_30.place(relx=0.5945, rely=0.48)
        self.btn_31 = Button(master, text="31", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(31))
        self.btn_31.place(relx=0.658, rely=0.48)
        self.btn_32 = Button(master, text="32", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(32))
        self.btn_32.place(relx=0.7215, rely=0.48)
        self.btn_33 = Button(master, text="33", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(33))
        self.btn_33.place(relx=0.785, rely=0.48)
        self.btn_34 = Button(master, text="34", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(34))
        self.btn_34.place(relx=0.15, rely=0.54)
        self.btn_35 = Button(master, text="35", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(35))
        self.btn_35.place(relx=0.2135, rely=0.54)
        self.btn_36 = Button(master, text="36", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(36))
        self.btn_36.place(relx=0.277, rely=0.54)
        self.btn_37 = Button(master, text="37", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(37))
        self.btn_37.place(relx=0.3405, rely=0.54)
        self.btn_38 = Button(master, text="38", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(38))
        self.btn_38.place(relx=0.404, rely=0.54)
        self.btn_39 = Button(master, text="39", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(39))
        self.btn_39.place(relx=0.4675, rely=0.54)
        self.btn_40 = Button(master, text="40", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(40))
        self.btn_40.place(relx=0.531, rely=0.54)
        self.btn_41 = Button(master, text="41", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(41))
        self.btn_41.place(relx=0.5945, rely=0.54)
        self.btn_42 = Button(master, text="42", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(42))
        self.btn_42.place(relx=0.658, rely=0.54)
        self.btn_43 = Button(master, text="43", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(43))
        self.btn_43.place(relx=0.7215, rely=0.54)
        self.btn_44 = Button(master, text="44", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(44))
        self.btn_44.place(relx=0.785, rely=0.54)
        self.btn_45 = Button(master, text="45", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(45))
        self.btn_45.place(relx=0.3405, rely=0.6)
        self.btn_46 = Button(master, text="46", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(46))
        self.btn_46.place(relx=0.404, rely=0.6)
        self.btn_47 = Button(master, text="47", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(47))
        self.btn_47.place(relx=0.4675, rely=0.6)
        self.btn_48 = Button(master, text="48", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(48))
        self.btn_48.place(relx=0.531, rely=0.6)
        self.btn_49 = Button(master, text="49", bg="#fcf00d", font=("Arial", 11, "bold"), command=lambda:
                             self.display_btn(49))
        self.btn_49.place(relx=0.5945, rely=0.6)

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
        play_btn = Button(numberSelection_screen, borderwidth=5, padx=23, pady=10, fg="black", bg="#09bd27", text="Play"
                          , font=("Arial", 17, "bold"), command=self.lotto_generator())
        play_btn.place(relx=0.1, rely=0.9)
        # play again button
        playAgain_btn = Button(numberSelection_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="#bdbdbd",
                               text="Play Again", font=("Arial", 17, "bold"), command=self.play_again)
        playAgain_btn.place(relx=0.26, rely=0.9)
        # claim button
        claim_btn = Button(numberSelection_screen, borderwidth=5, padx=25, pady=10, fg="white", bg="black",
                           text="Claim Prize", font=("Arial", 17, "bold"), command=self.claim_prize)
        claim_btn.place(relx=0.5, rely=0.9)
        # exit button
        exit_btn = Button(numberSelection_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="red", text="Exit",
                          font=("Arial", 17, "bold"), command=self.exit)
        exit_btn.place(relx=0.755, rely=0.9)

    # function to allow button values to display once selected
    def display_btn(self, num):
        if len(first_set) < 6 and num not in first_set:
            first_set.append(num)
            self.first_set.config(text=first_set, bg="#fcf00d")
        elif len(first_set) == 6 and len(second_set) < 6 and num not in second_set:
            second_set.append(num)
            self.second_set.config(text=second_set, bg="#fcf00d")
        elif len(second_set) == 6 and len(third_set) < 6 and num not in third_set:
            third_set.append(num)
            self.third_set.config(text=third_set, bg="#fcf00d")
        elif len(third_set) == 6:
            messagebox.showinfo('Error', 'Please note that you may only select 6 numbers for each set.')
        else:
            messagebox.showinfo("Duplicate Number", "\nPlease note that we do not allow a number to be chosen twice in "
                                                    "a single set.")

    # function to generate lotto numbers and if the client's set/s match
    def lotto_generator(self):
        # prizes to be won
        prizes = [0, 0, 20.00, 100.50, 2384.00, 8584.00, 10000000.00]
        # code to generate random numbers consisting of 6 digits
        lotto_numbers = random.sample(range(1, 49), 6)
        # sorting lotto numbers from smallest to largest
        lotto_numbers.sort()
        self.winningNums.config(text=lotto_numbers)

        # function to see if any lotto numbers selected matches those numbers that were generated
        # only if first set selected
        if len(first_set) == 6 and len(second_set) < 6 and len(third_set) < 6:
            # gets the value visible in the set and the generated numbers
            same_match = set(first_set).intersection(set(lotto_numbers))
            claim_prize = prizes
            if len(same_match) == 0:
                messagebox.showinfo('First Set Results', "Your correct matches are: " + "0" +
                                    "\nYou have won: " + str(claim_prize[0]))
            elif len(same_match) == 1:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[1]))
            elif len(same_match) == 2:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[2]))
            elif len(same_match) == 3:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[3]))
            elif len(same_match) == 4:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[4]))
            elif len(same_match) == 5:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[5]))
            else:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[6]))
        # only if first AND second set selected
        elif len(first_set) == 6 and len(second_set) == 6 and len(third_set) < 6:
            # gets the value visible in the sets and the generated numbers
            same_match = set(first_set).intersection(set(lotto_numbers))
            same_match2 = set(second_set).intersection(set(lotto_numbers))
            claim_prize = prizes
            if len(same_match) == 0:
                messagebox.showinfo('First Set Results', "Your correct matches are: " + "0" +
                                    "\nYou have won: " + str(claim_prize[0]))
            elif len(same_match) == 1:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[1]))
            elif len(same_match) == 2:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[2]))
            elif len(same_match) == 3:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[3]))
            elif len(same_match) == 4:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[4]))
            elif len(same_match) == 5:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[5]))
            elif len(same_match) == 6:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[6]))
            if len(same_match2) == 0:
                messagebox.showinfo('Second Set Results', "Your correct matches are: " + "0" +
                                    "\nYou have won: " + str(claim_prize[0]))
            elif len(same_match2) == 1:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[1]))
            elif len(same_match2) == 2:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[2]))
            elif len(same_match2) == 3:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[3]))
            elif len(same_match2) == 4:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[4]))
            elif len(same_match2) == 5:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[5]))
            else:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[6]))

        # only if first, second AND third set selected
        elif len(first_set) == 6 and len(second_set) == 6 and len(third_set) == 6:
            # gets the value visible in the sets and the generated numbers
            same_match = set(first_set).intersection(set(lotto_numbers))
            same_match2 = set(second_set).intersection(set(lotto_numbers))
            same_match3 = set(third_set).intersection(set(lotto_numbers))
            claim_prize = prizes
            if len(same_match) == 0:
                messagebox.showinfo('First Set Results', "Your correct matches are: " + "0" +
                                    "\nYou have won: " + str(claim_prize[0]))
            elif len(same_match) == 1:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[1]))
            elif len(same_match) == 2:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[2]))
            elif len(same_match) == 3:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[3]))

            elif len(same_match) == 4:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[4]))

            elif len(same_match) == 5:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[5]))

            elif len(same_match) == 6:
                messagebox.showinfo('First Set Results', "Your number of matches are " + str(len(same_match)) + ": " +
                                    str(same_match) + "\nYou have won: " + str(claim_prize[6]))

            if len(same_match2) == 0:
                messagebox.showinfo('Second Set Results', "Your correct matches are: " + "0" +
                                    "\nYou have won: " + str(claim_prize[0]))
            elif len(same_match2) == 1:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[1]))
            elif len(same_match2) == 2:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[2]))
            elif len(same_match2) == 3:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[3]))
            elif len(same_match2) == 4:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[4]))
            elif len(same_match2) == 5:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[5]))
            else:
                messagebox.showinfo('Second Set Results', "Your number of matches are " + str(len(same_match2)) + ": " +
                                    str(same_match2) + "\nYou have won: " + str(claim_prize[6]))
            if len(same_match3) == 0:
                messagebox.showinfo('Third Set Results', "Your correct matches are: " + "0" +
                                    "\nYou have won: " + str(claim_prize[0]))
            elif len(same_match3) == 1:
                messagebox.showinfo('Third Set Results', "Your number of matches are " + str(len(same_match3)) + ": " +
                                    str(same_match3) + "\nYou have won: " + str(claim_prize[1]))
            elif len(same_match3) == 2:
                messagebox.showinfo('Third Set Results', "Your number of matches are " + str(len(same_match3)) + ": " +
                                    str(same_match3) + "\nYou have won: " + str(claim_prize[2]))
            elif len(same_match3) == 3:
                messagebox.showinfo('Third Set Results', "Your number of matches are " + str(len(same_match3)) + ": " +
                                    str(same_match3) + "\nYou have won: " + str(claim_prize[3]))
            elif len(same_match3) == 4:
                messagebox.showinfo('Third Set Results', "Your number of matches are " + str(len(same_match3)) + ": " +
                                    str(same_match3) + "\nYou have won: " + str(claim_prize[4]))
            elif len(same_match3) == 5:
                messagebox.showinfo('Third Set Results', "Your number of matches are " + str(len(same_match3)) + ": " +
                                    str(same_match3) + "\nYou have won: " + str(claim_prize[5]))
            else:
                messagebox.showinfo('Third Set Results', "Your number of matches are " + str(len(same_match3)) + ": " +
                                    str(same_match3) + "\nYou have won: " + str(claim_prize[6]))

    # function to claim prize
    def claim_prize(self):
        numberSelection_screen.withdraw()
        import screen_3

    # function to replay
    def play_again(self):
        first_set.clear()
        second_set.clear()
        third_set.clear()
        self.first_set.config(text='', bg='#bdbdbd')
        self.second_set.config(text='', bg='#bdbdbd')
        self.third_set.config(text='', bg='#bdbdbd')
        self.btn_1.config(state=NORMAL)
        self.btn_2.config(state=NORMAL)
        self.btn_3.config(state=NORMAL)
        self.btn_4.config(state=NORMAL)
        self.btn_5.config(state=NORMAL)
        self.btn_6.config(state=NORMAL)
        self.btn_7.config(state=NORMAL)
        self.btn_8.config(state=NORMAL)
        self.btn_9.config(state=NORMAL)
        self.btn_10.config(state=NORMAL)
        self.btn_11.config(state=NORMAL)
        self.btn_12.config(state=NORMAL)
        self.btn_13.config(state=NORMAL)
        self.btn_14.config(state=NORMAL)
        self.btn_15.config(state=NORMAL)
        self.btn_16.config(state=NORMAL)
        self.btn_17.config(state=NORMAL)
        self.btn_18.config(state=NORMAL)
        self.btn_19.config(state=NORMAL)
        self.btn_20.config(state=NORMAL)
        self.btn_21.config(state=NORMAL)
        self.btn_22.config(state=NORMAL)
        self.btn_23.config(state=NORMAL)
        self.btn_24.config(state=NORMAL)
        self.btn_25.config(state=NORMAL)
        self.btn_26.config(state=NORMAL)
        self.btn_27.config(state=NORMAL)
        self.btn_28.config(state=NORMAL)
        self.btn_29.config(state=NORMAL)
        self.btn_30.config(state=NORMAL)
        self.btn_31.config(state=NORMAL)
        self.btn_32.config(state=NORMAL)
        self.btn_33.config(state=NORMAL)
        self.btn_34.config(state=NORMAL)
        self.btn_35.config(state=NORMAL)
        self.btn_36.config(state=NORMAL)
        self.btn_37.config(state=NORMAL)
        self.btn_38.config(state=NORMAL)
        self.btn_39.config(state=NORMAL)
        self.btn_40.config(state=NORMAL)
        self.btn_41.config(state=NORMAL)
        self.btn_42.config(state=NORMAL)
        self.btn_44.config(state=NORMAL)
        self.btn_43.config(state=NORMAL)
        self.btn_45.config(state=NORMAL)
        self.btn_46.config(state=NORMAL)
        self.btn_47.config(state=NORMAL)
        self.btn_48.config(state=NORMAL)
        self.btn_49.config(state=NORMAL)
        self.winningNums.config(text='')

    # function to exit
    def exit(self):
        numberSelection_screen.destroy()


selecting_numbers = Selection(numberSelection_screen)
numberSelection_screen.mainloop()
