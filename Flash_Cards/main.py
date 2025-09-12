from tkinter import *
import pandas
import random
try:
    data = pandas.read_csv('data/Words_to_Learn.csv')

except FileNotFoundError:
    original_data = pandas.read_csv('data/japanese_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
BACKGROUND_COLOR = '#B1DDC6'
current_card = {}

def flip_card():
    canvas.itemconfig(card_title, text = "English",fill="White")
    canvas.itemconfig(card_word, text = current_card['English'],fill="White")
    canvas.itemconfig(card_romaji, text = "")
    canvas.itemconfig(card_background, image=card_back_image)

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="Japanese",fill="Black")
    canvas.itemconfig(card_word,text=current_card['Japanese'],fill="Black")
    canvas.itemconfig(card_romaji,text=current_card["Romaji"],fill="Black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data= pandas.DataFrame(to_learn)
    data.to_csv("data/Words_to_Learn.csv",index=FALSE)
    next_card()
window =Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR,highlightthickness=0)
card_front_image = PhotoImage(file='images/green_box.png')
card_back_image = PhotoImage(file='images/blue_box.png')
card_background=canvas.create_image(400,263, image=card_front_image)
canvas.grid(row=0, column=0,columnspan=2)

card_title = canvas.create_text(400,190,text="",font=('Arial',20))
card_word = canvas.create_text(400,263,text="",font=("Arial",30,"bold"))
card_romaji = canvas.create_text(400,320,text="",font=("Arial",15))

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image,command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file='images/correct.png')
known_button = Button(image=check_image,command=is_known)
known_button.grid(column=1, row=1)


next_card()
window.mainloop()