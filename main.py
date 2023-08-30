from tkinter import Tk, Canvas, PhotoImage, Button

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"





# --------------------------------- UI SETUP --------------------------------- #

window = Tk()
window.title("Flashy")
window.config(height=500, width=300, padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating canvas in the window
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

#  Creating the image to put in the canvas
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(410, 270, image=card_image)   # Placing the image approx at the center of the canvas
title = canvas.create_text(390, 150, text="Title", fill="black", font=(FONT_NAME, 20, "italic", "bold"))    # Place the title in the upper center of the card
word_to_convert = canvas.create_text(390, 260, text="Word", fill="black", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

window.mainloop()