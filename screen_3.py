# Mikayla Beelders End Of Module Project
# currency conversion screen
from tkinter import *
from tkinter import messagebox
from screen_2 import total_prize_amount
from PIL import Image, ImageTk
currency_conversion_screen = Tk()
currency_conversion_screen.geometry("800x800")
currency_conversion_screen.title("Currency Conversion")
currency_conversion_screen.config(bg="#ffde24")
# adding an image
canvas = Canvas(currency_conversion_screen, width=500, height=300, bg="#fcf00d", borderwidth=0, highlightthickness=0)
canvas.place(relx=0.3, rely=0.02)
img_numBalls = ImageTk.PhotoImage(Image.open("money.jpeg"))
canvas.create_image(150, 5, anchor=N, image=img_numBalls)

class Conversion:
    def __init__(self, master):
        self.conversion_frame = Frame(master, bg="#bdbdbd", width=630, height=450)
        self.conversion_frame.place(relx=0.1, rely=0.3)
        # instruction heading
        self.instruction_heading = Label(master, text="Please select your desired currency:",
                                         font=("Arial", 13, "bold"), bg="#bdbdbd")
        self.instruction_heading.place(relx=0.13, rely=0.31)

    def converting(self):

        # making the request
        response = requests.get('https://prime.exchangerate-api.com/v5/d15f5d23ca3cd1c7094c5e89/latest/USD')
        data = response.json()
        standard_rate = data['conversion_rates']
        print(standard_rate)

        # covert label and listbox
        convert_label = Label(root, text="Please select a currency: ", bg="#6dc9a9", fg="white",
                              font=("Helvertica", 15))
        convert_label.place(relx=0.3, rely=0.25)
        convert_list = Listbox(root, width=20)
        for i in standard_rate.keys():
            convert_list.insert(END, str(i))
        convert_list.place(relx=0.36, rely=0.3)

        # convert function
    def convert(self):
        try:
            amount = float(total_prize_amount)
            print(data['conversion_rates'][convert_list.get(ACTIVE)])
            converted_amount = amount / data['conversion_rates'][convert_list.get(ACTIVE)]
            usd_answer['text'] = round(converted_amount, 2)  # round conversion off to 2 decimal places
        except ValueError:
            messagebox.showerror("Error", "Invalid input.\nPlease enter integers.")
            amount_entry.delete(0, END)
            usd_answer.config(text="")
            convert_list.select_clear(0, END)


converting = Conversion(currency_conversion_screen)
currency_conversion_screen.mainloop()
