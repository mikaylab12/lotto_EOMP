# Mikayla Beelders End Of Module Project
# login screen
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime, timedelta, time, date
import rsaidnumber
import random
import requests
from tkinter import ttk
from email_validator import validate_email, EmailNotValidError
import uuid
import smtplib
from playsound import playsound

login_screen = Tk()
login_screen.geometry("800x800")
login_screen.title("User Credentials")
login_screen.config(bg="#ffde24")
# adding image
canvas = Canvas(login_screen, width=300, height=100, bg="#ffde24", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.3, rely=0.1)
img_logo = ImageTk.PhotoImage(Image.open("lotto_name.png"))
canvas.create_image(150, 5, anchor=N, image=img_logo)


# function to calculate age
class User:
    def __init__(self, master):
        # creating frame for labels and entries
        self.login_frame = Frame(master, bg="#bdbdbd", width=630, height=400)
        self.login_frame.place(relx=0.1, rely=0.27)
        # frame heading
        self.instruction_heading = Label(master, text="Please enter the following credentials inorder to play:",
                                         font=("Arial", 17, "bold"), bg="#bdbdbd")
        self.instruction_heading.place(relx=0.13, rely=0.31)
        # name label and entry
        self.name_label = Label(master, bg="#bdbdbd", fg="#000", text="Name and Surname:", font=("Arial", 15))
        self.name_label.place(relx=0.13, rely=0.41)
        self.name_entry = Entry(master, width=20, font=("Arial", 15))
        self.name_entry.place(relx=0.5, rely=0.41)
        # email address label and entry
        self.email_label = Label(master, bg="#bdbdbd", fg="#000", text="Email Address:", font=("Arial", 15))
        self.email_label.place(relx=0.13, rely=0.48)
        self.email_entry = Entry(master, width=20, font=("Arial", 15))
        self.email_entry.place(relx=0.5, rely=0.48)
        # id label and entry
        self.id_label = Label(master, bg="#bdbdbd", fg="#000", text="ID Number:", font=("Arial", 15))
        self.id_label.place(relx=0.13, rely=0.55)
        self.id_entry = Entry(master, width=20, font=("Arial", 15))
        self.id_entry.place(relx=0.5, rely=0.55)
        # telephone number label and entry
        self.telephone_number_label = Label(master, bg="#bdbdbd", fg="#000", text="Contact Number:", font=("Arial", 15))
        self.telephone_number_label.place(relx=0.13, rely=0.62)
        self.telephone_number_entry = Entry(master, width=20, font=("Arial", 15))
        self.telephone_number_entry.place(relx=0.5, rely=0.62)
        # residential address label and entry
        self.residential_address_label = Label(master, bg="#bdbdbd", fg="#000", text="Residential Address:",
                                               font=("Arial", 15))
        self.residential_address_label.place(relx=0.13, rely=0.69)
        self.residential_address_entry = Entry(master, width=20, font=("Arial", 15))
        self.residential_address_entry.place(relx=0.5, rely=0.69)
        # login button
        login_btn = Button(login_screen, borderwidth=5, padx=15, pady=10, fg="black", bg="#09bd27", text="Login",
                           font=("Arial", 17, "bold"), command=self.validating_inputs)
        login_btn.place(relx=0.1, rely=0.86)
        # clear button
        clear_btn = Button(login_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="#bdbdbd", text="Clear",
                           font=("Arial", 17, "bold"), command=self.clear)
        clear_btn.place(relx=0.43, rely=0.86)
        # exit button
        exit_btn = Button(login_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="red", text="Exit",
                          font=("Arial", 17, "bold"), command=self.exit)
        exit_btn.place(relx=0.755, rely=0.86)
        global name_entry
        global nr_of_games
        global telephone_number

    def player_id(self):
        player_id = uuid.uuid4()
        fh = open("Player_info.txt", "a")
        fh.write("New Player:\n")
        fh.write = ("Date: " + str(date.today()) + '\n')
        fh.write = ("Time: " + str(time) + '\n')
        fh.write = ("Player Unique ID: " + str(player_id) + "\n")
        fh.close()
        return player_id

    def validating_inputs(self):
        def age_calc():
            try:
                # current date
                current_date = datetime.today()
                # in order to validate id number entered
                id_number = rsaidnumber.parse(self.id_entry.get())
                valid_id = id_number
                while valid_id:
                    dob = id_number.date_of_birth
                    current_age = int((current_date - dob) // timedelta(days=365.25))
                    if int(current_age) >= 18:
                        return 1
                    else:
                        messagebox.showinfo("Underage", "You are too young to play.\nPlease try again in " + str(
                            18 - int(current_age)) + " years")
            except ValueError:
                messagebox.showinfo("Invalid ID", "\nPlease enter a valid South African ID number that consists of 13"
                                    " digits.")

        def email_validation():
            try:
                # validate email
                valid = validate_email(self.email_entry.get())
                while valid:
                    return 1
            except EmailNotValidError:
                messagebox.showinfo("Invalid Email Address", "\nPlease enter a valid email address.")

        def cell_num_validation():
            try:
                tel = (self.telephone_number_entry.get())
                if int(len(tel)) == 10:
                    return 1
                elif int(len(tel)) > 10:
                    messagebox.showinfo('Error', 'Please ensure that your cellphone number contains only 10 digits.')
                elif int(len(tel)) < 10:
                    messagebox.showinfo('Error', 'Please note that you have not entered 10 digits '
                                        'for your contact number')
            except ValueError:
                messagebox.showinfo('Error', 'Please enter a valid cellphone number that only consists of digits. ')

        if age_calc() == 1 and email_validation() == 1 and cell_num_validation() == 1:
            fh = open("Player_info.txt", "a")
            fh.write("Name and Surname: " + self.name_entry.get() + '\n')
            fh.write("ID Number: " + self.id_entry.get() + '\n')
            fh.write("Email Address: " + self.email_entry.get() + '\n')
            fh.write("Contact Number: " + self.telephone_number_entry.get() + '\n')
            fh.write("Player ID: " + str(self.player_id) + '\n')
            fh.write("Residential Address: " + self.residential_address_entry.get() + "\n")
            fh.close()
            messagebox.showinfo("Valid Details", "Let's Play!")
            login_screen.destroy()
            self.screen_2()


    def clear(self):
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telephone_number_entry.delete(0, END)
        self.residential_address_entry.delete(0, END)

    def exit(self):
        login_screen.destroy()

    # lotto screen
    def screen_2(self):
        # second window/screen
        numberSelection_screen = Tk()
        numberSelection_screen.geometry("800x800")
        numberSelection_screen.title("Select Your Numbers")
        numberSelection_screen.config(bg="#ffde24")
        # adding an image
        canvas = Canvas(numberSelection_screen, width=155, height=180, bg="#ffde24", borderwidth=0, highlightthickness=0)
        canvas.place(relx=0.4, rely=0.01)
        img_lotto_logo = ImageTk.PhotoImage(Image.open("slogan2.png"))
        canvas.create_image(80, 5, anchor=N, image=img_lotto_logo)
        # all sets chosen by client
        first_set = []
        second_set = []
        third_set = []

        # all widgets displayed on this window
        class Selection:
            def __init__(self, master):
                self.numberSelection_frame = Frame(master, bg="#bdbdbd", width=630, height=450)
                self.numberSelection_frame.place(relx=0.1, rely=0.27)
                # instruction heading
                self.instruction_heading = Label(master, text="Please select your 6 numbers for each set:",
                                                 font=("Arial", 18, "bold"), bg="#bdbdbd")
                self.instruction_heading.place(relx=0.13, rely=0.28)
                # number buttons
                self.btn_1 = Button(master, text="1", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                                    self.display_btn(1))
                self.btn_1.place(relx=0.15, rely=0.34)
                self.btn_2 = Button(master, text="2", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                                    self.display_btn(2))
                self.btn_2.place(relx=0.2135, rely=0.34)
                self.btn_3 = Button(master, text="3", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                                    self.display_btn(3))
                self.btn_3.place(relx=0.277, rely=0.34)
                self.btn_4 = Button(master, text="4", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(4))
                self.btn_4.place(relx=0.3405, rely=0.34)
                self.btn_5 = Button(master, text="5", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(5))
                self.btn_5.place(relx=0.404, rely=0.34)
                self.btn_6 = Button(master, text="6", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(6))
                self.btn_6.place(relx=0.4675, rely=0.34)
                self.btn_7 = Button(master, text="7", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(7))
                self.btn_7.place(relx=0.531, rely=0.34)
                self.btn_8 = Button(master, text="8", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(8))
                self.btn_8.place(relx=0.5945, rely=0.34)
                self.btn_9 = Button(master, text="9", padx=15, bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(9))
                self.btn_9.place(relx=0.658, rely=0.34)
                self.btn_10 = Button(master, text="10", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(10))
                self.btn_10.place(relx=0.7215, rely=0.34)
                self.btn_11 = Button(master, text="11", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(11))
                self.btn_11.place(relx=0.785, rely=0.34)
                self.btn_12 = Button(master, text="12", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(12))
                self.btn_12.place(relx=0.15, rely=0.4)
                self.btn_13 = Button(master, text="13", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(13))
                self.btn_13.place(relx=0.2135, rely=0.4)
                self.btn_14 = Button(master, text="14", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(14))
                self.btn_14.place(relx=0.277, rely=0.4)
                self.btn_15 = Button(master, text="15", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(15))
                self.btn_15.place(relx=0.3405, rely=0.4)
                self.btn_16 = Button(master, text="16", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(16))
                self.btn_16.place(relx=0.404, rely=0.4)
                self.btn_17 = Button(master, text="17", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(17))
                self.btn_17.place(relx=0.4675, rely=0.4)
                self.btn_18 = Button(master, text="18", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(18))
                self.btn_18.place(relx=0.531, rely=0.4)
                self.btn_19 = Button(master, text="19", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(19))
                self.btn_19.place(relx=0.5945, rely=0.4)
                self.btn_20 = Button(master, text="20", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(20))
                self.btn_20.place(relx=0.658, rely=0.4)
                self.btn_21 = Button(master, text="21", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(21))
                self.btn_21.place(relx=0.7215, rely=0.4)
                self.btn_22 = Button(master, text="22", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(22))
                self.btn_22.place(relx=0.785, rely=0.4)
                self.btn_23 = Button(master, text="23", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(23))
                self.btn_23.place(relx=0.15, rely=0.46)
                self.btn_24 = Button(master, text="24", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(24))
                self.btn_24.place(relx=0.2135, rely=0.46)
                self.btn_25 = Button(master, text="25", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(25))
                self.btn_25.place(relx=0.277, rely=0.46)
                self.btn_26 = Button(master, text="26", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(26))
                self.btn_26.place(relx=0.3405, rely=0.46)
                self.btn_27 = Button(master, text="27", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(27))
                self.btn_27.place(relx=0.404, rely=0.46)
                self.btn_28 = Button(master, text="28", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(28))
                self.btn_28.place(relx=0.4675, rely=0.46)
                self.btn_29 = Button(master, text="29", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(29))
                self.btn_29.place(relx=0.531, rely=0.46)
                self.btn_30 = Button(master, text="30", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(30))
                self.btn_30.place(relx=0.5945, rely=0.46)
                self.btn_31 = Button(master, text="31", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(31))
                self.btn_31.place(relx=0.658, rely=0.46)
                self.btn_32 = Button(master, text="32", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(32))
                self.btn_32.place(relx=0.7215, rely=0.46)
                self.btn_33 = Button(master, text="33", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(33))
                self.btn_33.place(relx=0.785, rely=0.46)
                self.btn_34 = Button(master, text="34", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(34))
                self.btn_34.place(relx=0.15, rely=0.52)
                self.btn_35 = Button(master, text="35", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(35))
                self.btn_35.place(relx=0.2135, rely=0.52)
                self.btn_36 = Button(master, text="36", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(36))
                self.btn_36.place(relx=0.277, rely=0.52)
                self.btn_37 = Button(master, text="37", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(37))
                self.btn_37.place(relx=0.3405, rely=0.52)
                self.btn_38 = Button(master, text="38", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(38))
                self.btn_38.place(relx=0.404, rely=0.52)
                self.btn_39 = Button(master, text="39", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(39))
                self.btn_39.place(relx=0.4675, rely=0.52)
                self.btn_40 = Button(master, text="40", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(40))
                self.btn_40.place(relx=0.531, rely=0.52)
                self.btn_41 = Button(master, text="41", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(41))
                self.btn_41.place(relx=0.5945, rely=0.52)
                self.btn_42 = Button(master, text="42", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(42))
                self.btn_42.place(relx=0.658, rely=0.52)
                self.btn_43 = Button(master, text="43", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(43))
                self.btn_43.place(relx=0.7215, rely=0.52)
                self.btn_44 = Button(master, text="44", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(44))
                self.btn_44.place(relx=0.785, rely=0.52)
                self.btn_45 = Button(master, text="45", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(45))
                self.btn_45.place(relx=0.3405, rely=0.58)
                self.btn_46 = Button(master, text="46", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(46))
                self.btn_46.place(relx=0.404, rely=0.58)
                self.btn_47 = Button(master, text="47", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(47))
                self.btn_47.place(relx=0.4675, rely=0.58)
                self.btn_48 = Button(master, text="48", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(48))
                self.btn_48.place(relx=0.531, rely=0.58)
                self.btn_49 = Button(master, text="49", bg="#ffde24", font=("Arial", 11, "bold"), command=lambda:
                self.display_btn(49))
                self.btn_49.place(relx=0.5945, rely=0.58)

                # labels for all 3 sets to be displayed.
                self.first_set_label = Label(master, text="Set 1: ", bg="#bdbdbd", width=10, font=('Arial', 14, 'bold'))
                self.first_set_label.place(relx=0.175, rely=0.64)
                self.first_set = Label(master, text="", bg="#bdbdbd", width=15, font=('Arial', 13))
                self.first_set.place(relx=0.15, rely=0.69)
                self.second_set_label = Label(master, text="Set 2: ", bg="#bdbdbd", width=10, font=('Arial', 14, 'bold'))
                self.second_set_label.place(relx=0.435, rely=0.64)
                self.second_set = Label(master, text="", bg="#bdbdbd", width=15, font=('Arial', 13))
                self.second_set.place(relx=0.4, rely=0.69)
                self.third_set_label = Label(master, text="Set 3: ", bg="#bdbdbd", width=10, font=('Arial', 14, 'bold'))
                self.third_set_label.place(relx=0.69, rely=0.64)
                self.third_set = Label(master, text="", bg="#bdbdbd", width=15, font=('Arial', 13))
                self.third_set.place(relx=0.65, rely=0.69)

                # winning numbers display
                self.winningNums_label = Label(master, text="Lotto numbers:", font=('Arial', 17, 'bold'), bg="#bdbdbd")
                self.winningNums_label.place(relx=0.13, rely=0.74)
                self.winningNums = Label(master, text="", bg="#bdbdbd", width=18, font=('Arial', 17, 'bold'))
                self.winningNums.place(relx=0.4, rely=0.74)

                # label for total earnings
                self.total_heading = Label(master, text="Total Amount Won:    R ", font=('Arial', 17, 'bold'), bg="#bdbdbd")
                self.total_heading.place(relx=0.13, rely=0.775)
                self.total_label = Label(master, text="", bg="#bdbdbd", width=10, font=('Arial', 17, 'bold'))
                self.total_label.place(relx=0.45, rely=0.775)
                # play button
                play_btn = Button(numberSelection_screen, borderwidth=5, padx=23, pady=10, fg="black", bg="#09bd27",
                                  text="Play"
                                  , font=("Arial", 17, "bold"), command=self.lotto_generator)
                play_btn.place(relx=0.1, rely=0.87)
                # play again button
                playAgain_btn = Button(numberSelection_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="#bdbdbd",
                                       text="Play Again", font=("Arial", 17, "bold"), command=self.play_again)
                playAgain_btn.place(relx=0.26, rely=0.87)
                # claim button
                claim_btn = Button(numberSelection_screen, borderwidth=5, padx=25, pady=10, fg="white", bg="black",
                                   text="Claim Prize", font=("Arial", 17, "bold"), command=self.claim_prize)
                claim_btn.place(relx=0.5, rely=0.87)
                # exit button
                exit_btn = Button(numberSelection_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="red",
                                  text="Exit",
                                  font=("Arial", 17, "bold"), command=self.exit)
                exit_btn.place(relx=0.755, rely=0.87)

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
                    messagebox.showinfo("Duplicate Number",
                                        "\nPlease note that we do not allow a number to be chosen twice in "
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
                global first_winnings
                global second_winnings
                global third_winnings
                global total_prize_amount
                self.nr_of_games = 0
                # function to see if any lotto numbers selected matches those numbers that were generated
                # only if FIRST set selected
                try:
                    if len(first_set) == 6 and len(second_set) < 6 and len(third_set) < 6:
                        # gets the value visible in the set and the generated numbers
                        same_match = set(first_set).intersection(set(lotto_numbers))
                        claim_prize = prizes
                        self.nr_of_games = 1
                        # function to determine the prize amount
                        if len(same_match) == 0:
                            first_winnings = float(claim_prize[0])
                            messagebox.showinfo('First Set Results', "Your correct matches are: " + "0" +
                                                "\nYou have won: R" + str(claim_prize[0]))
                            # play sound
                            playsound("ES_CashRegister5-SFXProducer.mp3")
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: 0" + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[0]) + "\n")
                            fh.close()
                        elif len(same_match) == 1:
                            first_winnings = float(claim_prize[1])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[1]))
                            # play sound
                            playsound("ES_CashRegister5-SFXProducer.mp3")
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[1]) + "\n")
                            fh.close()
                        elif len(same_match) == 2:
                            first_winnings = float(claim_prize[2])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[2]))
                            # play sound
                            playsound("ES_TrumpetSad-SFX Producer.mp3")
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[2]) + "\n")
                            fh.close()
                        elif len(same_match) == 3:
                            first_winnings = float(claim_prize[3])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[3]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[3]) + "\n")
                            fh.close()
                        elif len(same_match) == 4:
                            first_winnings = float(claim_prize[4])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[4]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[4]) + "\n")
                            fh.close()
                        elif len(same_match) == 5:
                            first_winnings = float(claim_prize[5])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[5]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[5]) + "\n")
                            fh.close()
                        else:
                            first_winnings = float(claim_prize[6])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[6]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[6]) + "\n")
                            fh.close()
                    # only if FIRST and SECOND set selected
                    elif len(first_set) == 6 and len(second_set) == 6 and len(third_set) < 6:
                        # gets the value visible in the sets and the generated numbers
                        same_match = set(first_set).intersection(set(lotto_numbers))
                        same_match2 = set(second_set).intersection(set(lotto_numbers))
                        claim_prize = prizes
                        self.nr_of_games = 2
                        # function to determine the prize amount for the FIRST set
                        if len(same_match) == 0:
                            first_winnings = float(claim_prize[0])
                            messagebox.showinfo('First Set Results', "Your correct matches are: " + "0" +
                                                "\nYou have won: R" + str(claim_prize[0]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: 0\n")
                            fh.write("The amount for the first set: " + str(claim_prize[0]) + "\n")
                            fh.close()
                        elif len(same_match) == 1:
                            first_winnings = float(claim_prize[1])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[1]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[1]) + "\n")
                            fh.close()
                        elif len(same_match) == 2:
                            first_winnings = float(claim_prize[2])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[2]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[2]) + "\n")
                            fh.close()
                        elif len(same_match) == 3:
                            first_winnings = float(claim_prize[3])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[3]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[3]) + "\n")
                            fh.close()
                        elif len(same_match) == 4:
                            first_winnings = float(claim_prize[4])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[4]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[4]) + "\n")
                            fh.close()
                        elif len(same_match) == 5:
                            first_winnings = float(claim_prize[5])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[5]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[5]) + "\n")
                            fh.close()
                        elif len(same_match) == 6:
                            first_winnings = float(claim_prize[6])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[6]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[6]) + "\n")
                            fh.close()
                        # function to determine the prize amount for the SECOND set
                        if len(same_match2) == 0:
                            second_winnings = float(claim_prize[0])
                            messagebox.showinfo('Second Set Results', "Your correct matches are: " + "0" +
                                                "\nYou have won: R" + str(claim_prize[0]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write("The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: 0\n")
                            fh.write("The amount for the second set: " + str(claim_prize[0]) + "\n")
                            fh.close()
                        elif len(same_match2) == 1:
                            second_winnings = float(claim_prize[1])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[1]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[1]) + "\n")
                            fh.close()
                        elif len(same_match2) == 2:
                            second_winnings = float(claim_prize[2])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[2]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[2]) + "\n")
                            fh.close()
                        elif len(same_match2) == 3:
                            second_winnings = float(claim_prize[3])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[3]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[3]) + "\n")
                            fh.close()
                        elif len(same_match2) == 4:
                            second_winnings = float(claim_prize[4])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[4]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[4]) + "\n")
                            fh.close()
                        elif len(same_match2) == 5:
                            second_winnings = float(claim_prize[5])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[5]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[5]) + "\n")
                            fh.close()
                        else:
                            second_winnings = float(claim_prize[6])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[6]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[6]) + "\n")
                            fh.close()

                    # only if FIRST, SECOND and THIRD set selected
                    elif len(first_set) == 6 and len(second_set) == 6 and len(third_set) == 6:
                        # gets the value visible in the sets and the generated numbers
                        same_match = set(first_set).intersection(set(lotto_numbers))
                        same_match2 = set(second_set).intersection(set(lotto_numbers))
                        same_match3 = set(third_set).intersection(set(lotto_numbers))
                        claim_prize = prizes
                        self.nr_of_games = 3
                        # function to determine prize amount for FIRST set
                        if len(same_match) == 0:
                            first_winnings = float(claim_prize[0])
                            messagebox.showinfo('First Set Results', "Your correct matches are: " + "0" +
                                                "\nYou have won: R" + str(claim_prize[0]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: 0\n")
                            fh.write("The amount for the first set: " + str(claim_prize[0]) + "\n")
                            fh.close()
                        elif len(same_match) == 1:
                            first_winnings = float(claim_prize[1])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[1]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[1]) + "\n")
                            fh.close()
                        elif len(same_match) == 2:
                            first_winnings = float(claim_prize[2])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[2]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[2]) + "\n")
                            fh.close()
                        elif len(same_match) == 3:
                            first_winnings = float(claim_prize[3])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[3]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[3]) + "\n")
                            fh.close()
                        elif len(same_match) == 4:
                            first_winnings = float(claim_prize[4])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[4]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[4]) + "\n")
                            fh.close()
                        elif len(same_match) == 5:
                            first_winnings = float(claim_prize[5])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[5]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[5]) + "\n")
                            fh.close()
                        elif len(same_match) == 6:
                            first_winnings = float(claim_prize[6])
                            messagebox.showinfo('First Set Results',
                                                "Your number of matches are " + str(len(same_match)) + ": " +
                                                str(same_match) + "\nYou have won: R" + str(claim_prize[6]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Sets Played: " + str(self.nr_of_games) + "\n")
                            fh.write('The winning numbers are: ' + str(lotto_numbers) + "\n")
                            fh.write("Client's numbers for the first set are: " + str(first_set) + "\n")
                            fh.write("The number of correct matches in the first set is: " + str(len(same_match)) + '\n')
                            fh.write("The correct matches for the first set are: " + str(same_match) + '\n')
                            fh.write("The amount for the first set: " + str(claim_prize[6]) + "\n")
                            fh.close()
                        # function to determine prize amount for SECOND set
                        if len(same_match2) == 0:
                            second_winnings = float(claim_prize[0])
                            messagebox.showinfo('Second Set Results', "Your correct matches are: " + "0" +
                                                "\nYou have won: R" + str(claim_prize[0]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: 0\n")
                            fh.write("The amount for the second set: " + str(claim_prize[0]) + "\n")
                            fh.close()
                        elif len(same_match2) == 1:
                            second_winnings = float(claim_prize[1])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[1]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[1]) + "\n")
                            fh.close()
                        elif len(same_match2) == 2:
                            second_winnings = float(claim_prize[2])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[2]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[2]) + "\n")
                            fh.close()
                        elif len(same_match2) == 3:
                            second_winnings = float(claim_prize[3])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[3]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[3]) + "\n")
                            fh.close()
                        elif len(same_match2) == 4:
                            second_winnings = float(claim_prize[4])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[4]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[4]) + "\n")
                            fh.close()
                        elif len(same_match2) == 5:
                            second_winnings = float(claim_prize[5])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[5]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[5]) + "\n")
                            fh.close()
                        elif len(same_match2) == 6:
                            second_winnings = float(claim_prize[6])
                            messagebox.showinfo('Second Set Results',
                                                "Your number of matches are " + str(len(same_match2)) + ": " +
                                                str(same_match2) + "\nYou have won: R" + str(claim_prize[6]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the second set are: " + str(second_set) + "\n")
                            fh.write(
                                "The number of correct matches in the second set is: " + str(len(same_match2)) + '\n')
                            fh.write("The correct matches for the second set are: " + str(same_match2) + '\n')
                            fh.write("The amount for the second set: " + str(claim_prize[6]) + "\n")
                            fh.close()
                        # function to determine prize amount for THIRD set
                        if len(same_match3) == 0:
                            third_winnings = float(claim_prize[0])
                            messagebox.showinfo('Third Set Results', "Your correct matches are: " + "0" +
                                                "\nYou have won: R" + str(claim_prize[0]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the third set are: " + str(third_set) + "\n")
                            fh.write("The number of correct matches in the third set is: " + str(len(same_match3)) + '\n')
                            fh.write("The correct matches for the third set are: 0\n")
                            fh.write("The amount for the third set: " + str(claim_prize[0]) + "\n")
                            fh.close()
                        elif len(same_match3) == 1:
                            third_winnings = float(claim_prize[1])
                            messagebox.showinfo('Third Set Results',
                                                "Your number of matches are " + str(len(same_match3)) + ": " +
                                                str(same_match3) + "\nYou have won: R" + str(claim_prize[1]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the third set are: " + str(third_set) + "\n")
                            fh.write("The number of correct matches in the third set is: " + str(len(same_match3)) + '\n')
                            fh.write("The correct matches for the third set are: " + str(same_match3) + '\n')
                            fh.write("The amount for the third set: " + str(claim_prize[1]) + "\n")
                            fh.close()
                        elif len(same_match3) == 2:
                            third_winnings = float(claim_prize[2])
                            messagebox.showinfo('Third Set Results',
                                                "Your number of matches are " + str(len(same_match3)) + ": " +
                                                str(same_match3) + "\nYou have won: R" + str(claim_prize[2]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the third set are: " + str(third_set) + "\n")
                            fh.write("The number of correct matches in the third set is: " + str(len(same_match3)) + '\n')
                            fh.write("The correct matches for the third set are: " + str(same_match3) + '\n')
                            fh.write("The amount for the third set: " + str(claim_prize[2]) + "\n")
                            fh.close()
                        elif len(same_match3) == 3:
                            third_winnings = float(claim_prize[3])
                            messagebox.showinfo('Third Set Results',
                                                "Your number of matches are " + str(len(same_match3)) + ": " +
                                                str(same_match3) + "\nYou have won: R" + str(claim_prize[3]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the third set are: " + str(third_set) + "\n")
                            fh.write("The number of correct matches in the third set is: " + str(len(same_match3)) + '\n')
                            fh.write("The correct matches for the third set are: " + str(same_match3) + '\n')
                            fh.write("The amount for the third set: " + str(claim_prize[3]) + "\n")
                            fh.close()
                        elif len(same_match3) == 4:
                            third_winnings = float(claim_prize[4])
                            messagebox.showinfo('Third Set Results',
                                                "Your number of matches are " + str(len(same_match3)) + ": " +
                                                str(same_match3) + "\nYou have won: R" + str(claim_prize[4]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the third set are: " + str(third_set) + "\n")
                            fh.write("The number of correct matches in the third set is: " + str(len(same_match3)) + '\n')
                            fh.write("The correct matches for the third set are: " + str(same_match3) + '\n')
                            fh.write("The amount for the third set: " + str(claim_prize[4]) + "\n")
                            fh.close()
                        elif len(same_match3) == 5:
                            third_winnings = float(claim_prize[5])
                            messagebox.showinfo('Third Set Results',
                                                "Your number of matches are " + str(len(same_match3)) + ": " +
                                                str(same_match3) + "\nYou have won: R" + str(claim_prize[5]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the third set are: " + str(third_set) + "\n")
                            fh.write("The number of correct matches in the third set is: " + str(len(same_match3)) + '\n')
                            fh.write("The correct matches for the third set are: " + str(same_match3) + '\n')
                            fh.write("The amount for the third set: " + str(claim_prize[5]) + "\n")
                            fh.close()
                        else:
                            third_winnings = float(claim_prize[6])
                            messagebox.showinfo('Third Set Results',
                                                "Your number of matches are " + str(len(same_match3)) + ": " +
                                                str(same_match3) + "\nYou have won: R" + str(claim_prize[6]))
                            # information that will be written on a separate text file
                            fh = open("Player_info.txt", "a")
                            fh.write("Client's numbers for the third set are: " + str(third_set) + "\n")
                            fh.write("The number of correct matches in the third set is: " + str(len(same_match3)) + '\n')
                            fh.write("The correct matches for the third set are: " + str(same_match3) + '\n')
                            fh.write("The amount for the third set: " + str(claim_prize[6]) + "\n")
                            fh.close()
                finally:
                    if len(first_set) == 6 and len(second_set) < 6 and len(third_set) < 6:
                        total_prize_amount = first_winnings
                        self.total_label.config(text=total_prize_amount)
                        # information that will be written on a separate text file
                        fh = open("Player_info.txt", "a")
                        fh.write("Total earnings in R: " + str(total_prize_amount) + '\n')
                        fh.close()
                        # separate text file with winners info
                        text = open("prize_winners_info.txt", "+a")
                        text.write("\nTotal Amount Won: " + str(total_prize_amount))
                        text.close()
                    elif len(first_set) == 6 and len(second_set) == 6 and len(third_set) < 6:
                        total_prize_amount = first_winnings + second_winnings
                        self.total_label.config(text=total_prize_amount)
                        # information that will be written on a separate text file
                        fh = open("Player_info.txt", "a")
                        fh.write("Total earnings in R: " + str(total_prize_amount) + '\n')
                        fh.close()
                        text = open("prize_winners_info.txt", "+a")
                        text.write("\nTotal Amount Won: " + str(total_prize_amount))
                        text.close()
                    elif len(first_set) == 6 and len(second_set) == 6 and len(third_set) == 6:
                        total_prize_amount = first_winnings + second_winnings + third_winnings
                        self.total_label.config(text=total_prize_amount)
                        # information that will be written on a separate text file
                        fh = open("Player_info.txt", "a")
                        fh.write("Total earnings in R: " + str(total_prize_amount) + '\n')
                        fh.close()
                        text = open("prize_winners_info.txt", "+a")
                        text.write("\nTotal Amount Won: " + str(total_prize_amount))
                        text.close()

            # function to claim prize
            def claim_prize(self):
                numberSelection_screen.destroy()
                self.screen_3()

            # function to replay
            def play_again(self):
                first_set.clear()
                second_set.clear()
                third_set.clear()
                self.first_set.config(text='', bg='#bdbdbd')
                self.second_set.config(text='', bg='#bdbdbd')
                self.third_set.config(text='', bg='#bdbdbd')
                self.total_label.config(text='')
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

            def screen_3(self):
                currency_conversion_screen = Tk()
                currency_conversion_screen.geometry("800x800")
                currency_conversion_screen.title("Currency Conversion")
                currency_conversion_screen.config(bg="#ffde24")
                # adding an image
                canvas = Canvas(currency_conversion_screen, width=500, height=300, bg="#ffde24", borderwidth=0,
                                highlightthickness=0)
                canvas.place(relx=0.3, rely=0.02)
                img_money = ImageTk.PhotoImage(Image.open("currency.jpeg"))
                canvas.create_image(150, 5, anchor=N, image=img_money)
                # making the request
                response = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/ZAR')
                data = response.json()
                standard_rate = data['conversion_rates']

                class Conversion:
                    def __init__(self, master):
                        self.conversion_frame = Frame(currency_conversion_screen, bg="#bdbdbd", width=630, height=450)
                        self.conversion_frame.place(relx=0.1, rely=0.27)

                        # instruction heading
                        self.instruction_heading = Label(master, text="Please select your desired currency:",
                                                         font=("Arial", 17, "bold"), bg="#bdbdbd")
                        self.instruction_heading.place(relx=0.13, rely=0.28)

                        # total heading and amount
                        self.total_heading = Label(master, text="Total amount in ZAR(R): ", font=("Arial", 15, "bold"),
                                                   bg="#bdbdbd")
                        self.total_heading.place(relx=0.15, rely=0.32)
                        self.total_amount = Label(master, text=total_prize_amount, font=("Arial", 15, "bold"), bg="#bdbdbd")
                        self.total_amount.place(relx=0.5, rely=0.32)

                        # covert label and listbox
                        self.convert_list = Listbox(master, width=20, font=("Arial", 15), bg="#bdbdbd",
                                                    selectbackground='#ffde24')
                        self.convert_list.place(relx=0.36, rely=0.4)
                        # self.scrollbar = Scrollbar(self.convert_list)
                        # self.scrollbar.pack(side="right", fill="y")
                        for i in standard_rate.keys():
                            self.convert_list.insert(END, str(i))
                        # self.scrollbar.config(command=self.convert_list.yview)
                        self.converted_label = Label(master, text="Converted Amount: ", font=("Arial", 15, "bold"),
                                                     bg="#bdbdbd")
                        self.converted_label.place(relx=0.15, rely=0.77)
                        self.converted_total = Label(master, text="", font=("Arial", 15, "bold"), bg="#bdbdbd")
                        self.converted_total.place(relx=0.5, rely=0.77)

                        # proceed button
                        self.proceed_btn = Button(master, borderwidth=5, padx=25, pady=10, fg="black", bg="#09bd27",
                                                  text="Proceed", font=("Arial", 17, "bold"), command=self.proceed)
                        self.proceed_btn.place(relx=0.52, rely=0.87)

                        # clear button
                        self.clear_btn = Button(master, borderwidth=5, padx=25, pady=10, fg="black",
                                                bg="#bdbdbd", text="Clear", font=("Arial", 17, "bold"),
                                                command=self.conversion_clear)
                        self.clear_btn.place(relx=0.1, rely=0.87)

                        # # converting button
                        self.convert_btn = Button(master, borderwidth=5, padx=25, pady=10, fg="white", bg="black",
                                                  text="Convert", font=("Arial", 17, "bold"), command=self.converting)
                        self.convert_btn.place(relx=0.3, rely=0.87)
                        # exit button
                        self.exit_btn = Button(master, borderwidth=5, padx=25, pady=10, fg="black", bg="red",
                                               text="Exit", font=("Arial", 17, "bold"), command=self.conversion_exit)
                        self.exit_btn.place(relx=0.755, rely=0.87)
                        # # making the request
                        # response = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/ZAR')
                        # data = response.json()
                        # standard_rate = data['conversion_rates']
                        # for i in standard_rate.keys():
                        #     self.convert_list.insert(END, str(i))
                        # print(data['conversion_rates'][self.convert_list.get(ACTIVE)])
                        # self.scrollbar = Scrollbar(master)
                        # self.scrollbar.pack(side="right", fill="y")
                        # for i in standard_rate.keys():
                        #     self.convert_list.insert(END, str(i))
                        # self.convert_list.pack(side="left", fill="both")
                        # self.scrollbar.config(command=self.convert_list.yview)
                        # print(data['conversion_rates'][self.convert_list.get(ACTIVE)])
                        self.total_amount.config(text=total_prize_amount)

                    def converting(self):
                        amount = float(total_prize_amount)
                        converted_amount = amount * standard_rate[self.convert_list.get(ACTIVE)]
                        # round conversion off to 2 decimal places

                        self.converted_total['text'] = round(converted_amount, 2)

                    def conversion_clear(self):
                        self.converted_total.config(text="")
                        self.convert_list.select_clear(0, END)

                    def conversion_exit(self):
                        currency_conversion_screen.destroy()

                    def proceed(self):
                        currency_conversion_screen.destroy()
                        self.screen_4()

                    def screen_4(self):
                        banking_details_screen = Tk()
                        banking_details_screen.geometry("800x800")
                        banking_details_screen.title("Banking Details")
                        banking_details_screen.config(bg="#ffde24")
                        # adding an image
                        canvas = Canvas(banking_details_screen, width=500, height=300, bg="#ffde24", borderwidth=0,
                                        highlightthickness=0)
                        canvas.place(relx=0.3, rely=0.02)
                        img_banks = ImageTk.PhotoImage(Image.open("banks2.jpeg"))
                        canvas.create_image(150, 5, anchor=N, image=img_banks)
                        # self.total = Conversion.converting(self.converted_total)


                        class Banking_details:
                            def __init__(self, master):
                                var_material = StringVar()
                                bank_options = {'ABSA': 632005, 'CAPITEC': 470010, 'FNB': 250655, 'NEDBANK': 198765}
                                self.banking_details_frame = Frame(banking_details_screen, bg="#bdbdbd", width=630,
                                                                   height=450)
                                self.banking_details_frame.place(relx=0.1, rely=0.27)

                                # instruction heading
                                self.banking_instruction_heading = Label(master,
                                                                         text="Please enter your valid banking details:"
                                                                         , font=("Arial", 17, "bold"), bg="#bdbdbd")
                                self.banking_instruction_heading.place(relx=0.13, rely=0.3)

                                # account name label and entry
                                self.account_name_label = Label(master, text="Account holder's name: ",
                                                                font=("Arial",
                                                                      15), bg="#bdbdbd")
                                self.account_name_label.place(relx=0.13, rely=0.4)
                                self.account_name_entry = Entry(master, font=("Arial", 15))
                                self.account_name_entry.place(relx=0.5, rely=0.4)

                                # account number entry and label
                                self.account_number_label = Label(master, text="Account number:"
                                                                  , font=("Arial", 15), bg="#bdbdbd")
                                self.account_number_label.place(relx=0.13, rely=0.47)
                                self.account_number_entry = Entry(master, font=("Arial", 15))
                                self.account_number_entry.place(relx=0.5, rely=0.47)

                                # total
                                # self.converted_total['text'] = round(converted_amount, 2)
                                # self.converted_total.config(text="")
                                # self.total = Label(master, text=""
                                #                                   , font=("Arial", 15), bg="#bdbdbd")
                                # self.total.place(relx=0.13, rely=0.74)
                                # self.total.config(text=self.converted_total)



                                # bank options
                                self.banking_options = ttk.Combobox(master, width=19, font=("Arial", 15),
                                                                    values=tuple(bank_options.keys()),
                                                                    textvariable=var_material)
                                self.banking_options.bind('<<ComboboxSelected>>', lambda event:
                                self.branch_code.config(text=bank_options[var_material.get()]))
                                self.banking_options.set('Please select...')

                                self.banking_options.place(relx=0.5, rely=0.54)
                                self.bank_options_label = Label(master, text="Bank Name: ", font=(
                                    "Arial", 15), bg="#bdbdbd")
                                self.bank_options_label.place(relx=0.13, rely=0.54)
                                # bank branch code labels
                                self.branch_code_label = Label(master, text="Branch Code ", font=(
                                    "Arial", 15), bg="#bdbdbd")
                                self.branch_code_label.place(relx=0.13, rely=0.61)
                                self.branch_code = Label(master, text="", font=("Arial", 15),
                                                         bg="#bdbdbd")
                                self.branch_code.place(relx=0.5, rely=0.61)
                                # proceed button
                                self.confirm_btn = Button(master, borderwidth=5, padx=25, pady=10, fg="black",
                                                          bg="#09bd27", text="Confirm", font=("Arial", 17, "bold"),
                                                          command=self.confirmation)
                                self.confirm_btn.place(relx=0.1, rely=0.87)

                                # clear button
                                self.clear_btn = Button(master, borderwidth=5, padx=25, pady=10, fg="black",
                                                        bg="#bdbdbd", text="Clear", font=("Arial", 17, "bold"),
                                                        command=self.banking_clear)
                                self.clear_btn.place(relx=0.425, rely=0.87)

                                # exit button
                                self.exit_btn = Button(master, borderwidth=5, padx=25, pady=10, fg="black", bg="red",
                                                       text="Exit", font=("Arial", 17, "bold"),
                                                       command=self.banking_exit)
                                self.exit_btn.place(relx=0.755, rely=0.87)

                                self.total = Conversion.converting(self.converted_total.cget('text'))

                            def confirmation(self):
                                def account_number_validation():
                                    try:
                                        valid_bankNr = int(self.account_number_entry.get())
                                        while valid_bankNr:
                                            return 1
                                        if valid_bankNr == '':
                                            messagebox.showinfo('Incomplete Inputs',
                                                                "Please fill in your account number.")
                                    except ValueError:
                                        messagebox.showinfo('Account Number Error',
                                                            'Please ensure that your account number only '
                                                            'contains digits.')

                                def account_name_validation():
                                    try:
                                        valid_accountName = str.isalpha(self.account_name_entry.get())
                                        if valid_accountName == '':
                                            messagebox.showinfo('Incomplete Inputs', "Please fill in your account name.")
                                        elif valid_accountName is False:
                                            messagebox.showinfo("Error", "Please ensure that your account name only "
                                                                         "consists of capital letters")
                                        while valid_accountName:
                                            return 1
                                    except ValueError:
                                        messagebox.showinfo('Account Name Error',
                                                            'Please ensure that your account number only contains digits.')

                                if account_name_validation() == 1 and account_number_validation() == 1:
                                    # play sound
                                    # playsound("./sounds/391539__mativve__electro-win-sound.wav")
                                    player_id = User.player_id(person_age)
                                    # send email
                                    s = smtplib.SMTP('smtp.gmail.com', 587)
                                    sender_email_id = 'mikaylabeelders@gmail.com'
                                    receiver_email_id = 'mikayla@trade245.com'
                                        # User(login_screen).email_entry
                                    password = 'Ashleemickey123*'

                                    s.starttls()

                                    s.login(sender_email_id, password)

                                    message = "Subject: Congratulations!!!\n"
                                    message = message + "Thank you for playing! " + "\nYour winnings are: " + str(self.total) + "\n\nBelow are your details:" + "\nPlayer ID: " + str(player_id) + "\nAccount name: " + str(self.account_name_entry.get()) + "\nAccount number: " + str(self.account_number_entry.get())

                                    s.sendmail(sender_email_id, receiver_email_id, message)
                                    # display instruction to player
                                    messagebox.showinfo('Thank you for playing!', 'Please refer to your emails for '
                                                                                  'confirmation of your details submitted.')

                            def banking_clear(self):
                                self.account_number_entry.delete(0, END)
                                self.account_name_entry. delete(0, END)


                            def banking_exit(self):
                                banking_details_screen.destroy()

                        banking_details = Banking_details(banking_details_screen)
                        banking_details_screen.mainloop()

                converting = Conversion(currency_conversion_screen)
                currency_conversion_screen.mainloop()

        selecting_numbers = Selection(numberSelection_screen)
        numberSelection_screen.mainloop()


person_age = User(login_screen)
login_screen.mainloop()
