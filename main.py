import random
from tkinter import Tk, Canvas, PhotoImage, Button
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
WORDS_DATA_FILE = "C:/Users/aallouche/PycharmProjects/flash-card-app/data/french_words.csv"



# --------------------------------- DATA PROCESSING --------------------------------- #
def acces_data():
    """This method read the csv file and returns the language and random word"""
    # Read the csv file
    data_frame = pandas.read_csv(WORDS_DATA_FILE)
    display_data(data_frame)

def display_data(dataframe=None):
    """This method displays the data in the flash card"""
    title_to_display = dataframe["French"].name
    canvas.itemconfig(title, text=title_to_display)
    words_list = dataframe.to_dict(orient="records")
    word_to_display = (random.choice(words_list)).get(title_to_display)
    canvas.itemconfig(word_to_convert, text=word_to_display)


# --------------------------------- UI SETUP --------------------------------- #

window = Tk()
window.title("Flashy")
window.config(height=500, width=300, padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating canvas in the window
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

#  Creating the image to put in the canvas
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(410, 270, image=card_image)   # Placing the image approx at the center of the canvas
title = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))    # Place the title in the upper center of the card
word_to_convert = canvas.create_text(400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=acces_data)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=acces_data)
wrong_button.grid(row=1, column=0)

window.mainloop()