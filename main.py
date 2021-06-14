# Mikayla Beelders End Of Module Project
# login screen
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime, timedelta
import rsaidnumber
from validate_email import validate_email

login_screen = Tk()
login_screen.geometry("800x800")
login_screen.title("User Credentials")
login_screen.config(bg="#fcf00d")
# adding image
canvas = Canvas(login_screen, width=300, height=100, bg="#fcf00d", borderwidth=0, highlightthickness=0)
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
        self.instruction_heading = Label(master, text="Please enter the following credentials inorder to play:", font=("Arial", 17, "bold"), bg="#bdbdbd")
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
        login_btn = Button(login_screen, borderwidth=5, padx=15, pady=10, fg="black", bg="#adacac", text="Login",
                           font=("Arial", 17, "bold"), command=self.age_calc)
        login_btn.place(relx=0.43, rely=0.82)
        # exit button
        exit_btn = Button(login_screen, borderwidth=5, padx=25, pady=10, fg="black", bg="#adacac", text="Exit",
                          font=("Arial", 17, "bold"), command=self.exit)
        exit_btn.place(relx=0.43, rely=0.9)

    # def age_calc(self):
    #     try:
    #         date = datetime.today()
    #         email = validate_email(self.email_entry.get())
    #         id_number = rsaidnumber.parse(self.id_entry.get())
    #         found = True
    #         if len(self.id_entry.get()) != 13:
    #             # messagebox.showerror("Inv", "must be 13")
    #             if found:
    #                 dob = id_number.date_of_birth
    #                 current_age = int((date - dob) // timedelta(days=365.25))
    #                 if int(current_age) >= 18:
    #                     messagebox.showinfo("Valid Details", "Let's Play!")
    #                 # import screen_2
    #                 else:
    #                     messagebox.showinfo("Underage", "You are too young to play.\nPlease try again in " + str(
    #                         18 - int(current_age)) + " years")
    #             else:
    #                 messagebox.showinfo("Invalid Details", "Invalid ID number. Try again.")
    #         else:
    #             messagebox.showinfo("Invalid ID", "\nPlease enter your valid South African ID number")
    #     except ValueError:
    #         messagebox.showinfo("Invalid ID", "\nInput ID in numbers.")

    def age_calc(self):
        try:
            date = datetime.today()
            email = validate_email(self.email_entry.get())
            id_number = rsaidnumber.parse(self.id_entry.get())
            found = True
            dob = id_number.date_of_birth
            current_age = int((date - dob) // timedelta(days=365.25))
            if len(self.id_entry.get()) != 13:
                messagebox.showerror("Inv", "Please enter 13 digits")
            elif self.id_entry.get() == str(self.id_entry.get()) :
                messagebox.showinfo("Invalid Details", "Invalid ID number, enter digits. Try again.")
            elif found == False:
                messagebox.showinfo("Invalid ID", "\nPlease enter your valid South African ID number")
            # elif int(current_age) >= 18:
            #     messagebox.showinfo("Valid Details", "Let's Play!")
            #             # import screen_2
        except int(current_age) >= 18:
                messagebox.showinfo("Valid Details", "Let's Play!")
                        # import screen_2
        else:
            messagebox.showinfo("Underage", "You are too young to play.\nPlease try again in " + str(
                            18 - int(current_age)) + " years")
        # except ValueError:
        #     messagebox.showinfo("Invalid ID", "\nPlease enter 13 digits")

    def exit(self):
        login_screen.destroy()


age = User(login_screen)
login_screen.mainloop()