from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
    df_dict = df.to_dict(orient="records")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
    df_dict = df.to_dict(orient="records")
finally:
    ran_dict = {}


def generate_word():
    global ran_dict, flip_timer
    window.after_cancel(flip_timer)
    ran_dict = random.choice(df_dict)
    ran_word = ran_dict["French"]
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=ran_word, fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=ran_dict["English"], fill="white")


def combine_fun():
    generate_word()
    remove()


def remove():
    df_dict.remove(ran_dict)
    data = pandas.DataFrame(df_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(410, 278, image=card_front_img)
title_txt = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 253, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=combine_fun)
right_button.grid(row=1, column=1, pady=50, padx=50)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0, pady=50, padx=50)

generate_word()


window.mainloop()
