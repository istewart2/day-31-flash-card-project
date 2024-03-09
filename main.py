import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA SETUP ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    
data_as_dictionary = data.to_dict(orient="records")

current_card = None


def known_word():
    data_as_dictionary.remove(current_card)
    words_to_learn = pandas.DataFrame(data_as_dictionary)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, delay_id
    window.after_cancel(delay_id)
    current_card = random.choice(data_as_dictionary)
    canvas.create_image(400, 263, image=card_front)
    french_word = current_card["French"]
    canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
    canvas.create_text(400, 263, text=french_word, font=("Arial", 60, "italic"), fill="black")
    delay_id = window.after(3000, flip_card)


def flip_card():
    canvas.create_image(400, 263, image=card_back)
    english_word = current_card["English"]
    canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"), fill="white")
    canvas.create_text(400, 263, text=english_word, font=("Arial", 60, "bold"), fill="white")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
right_button = Button(image=right, highlightthickness=0, command=known_word)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)

right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

delay_id = window.after(3000, flip_card)
next_card()

window.mainloop()
