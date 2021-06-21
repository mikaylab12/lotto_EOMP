from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

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
                               text="Exit", font=("Arial", 17, "bold"), command=self.banking_exit)
        self.exit_btn.place(relx=0.755, rely=0.87)

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
                while valid_accountName:
                    return 1
                if valid_accountName == '':
                    messagebox.showinfo('Incomplete Inputs', "Please fill in your account name.")
                elif valid_accountName is False:
                    messagebox.showinfo("Error", "Please ensure that your account name only "
                                                 "consists of capital letters")
            except ValueError:
                messagebox.showinfo('Account Name Error',
                                    'Please ensure that your account number only contains digits.')

        if account_name_validation() == 1 and account_number_validation() == 1:
            messagebox.showinfo('Thank you for playing!', 'Please refer to your emails for '
                                                          'confirmation of your details submitted.')
            print('Good')
            # global name_entry
            # global email_entry
            # global id_entry
            # global telephone_number_entry
            # global player_id
            # name = 'Miks'
            # email = 'miks@gmail.com'
            # number = '0826889551'
            # playerId = '645347'
            # amount_won = '400'
            # sets = '3'
            # text file
            # text = open("prize_winners_info.txt", "+a")
            # text.write("\n\nDate:" + str(date) + "  " + "Time:" + str(time) +
            #            "\nPlayer Name: " + str(name) + "\n"
            #            + "\nEmail: " + str(email)
            #            + "\nContact Number:" + str(number)
            #            + "\nNumber of games played:" + str(sets)
            #            + "\nTotal Amount Won: " + str(amount_won))
            # text.close()
            # # play sound
            # # playsound("./sounds/391539__mativve__electro-win-sound.wav")
            # # send email
            # s = smtplib.SMTP('smtp.gmail.com', 587)
            # sender_email_id = 'mikaylabeelders@gmail.com'
            # receiver_email_id = 'mikayla@trade245.com'
            # password = 'Ashleemickey123*'
            #
            # s.starttls()
            #
            # s.login(sender_email_id, password)
            #
            # message = "Subject: Congratulations!!!\n"
            # message = message + "Thank you for playing " + str(name) + "\nYour winnings are: " + str(
            #     amount_won) + "\n\nBelow are your details:" + "\nPlayer ID: " + str(
            #     playerId) + "\nAccount name: " + self.account_name_entry.get() + "\nAccount number: " + str(
            #     self.account_number_entry.get())
            #
            # s.sendmail(sender_email_id, receiver_email_id, message)
            # send email
            # play sound

    def banking_clear(self):
        self.account_number_entry.delete(0, END)
        self.account_name_entry.delete(0, END)

    def banking_exit(self):
        banking_details_screen.destroy()

banking_details = Banking_details(banking_details_screen)
banking_details_screen.mainloop()
