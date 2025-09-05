import math
from tkinter import *
#-------------------------Constants---------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps= 0
time = None
#------------TIME RESET------------------#
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
#-----------TIMER MECHANISM--------------#
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 ==0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg=PINK)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=RED)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

#----------COUNTDOWN MECHANISM----------#
def count_down(count):
    global time
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count>0:
        time = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks+="✔"
        check_marks.config(text=marks)

#------------UI SETUP------------#
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(window, width=600, height=340, bg=YELLOW,highlightthickness=0)

image = PhotoImage(file="my_tomato.png")
canvas.create_image(320, 150, image=image)
canvas.grid(row=1, column=1)

timer_text = canvas.create_text(320,180,text='00:00',fill="white",font=(FONT_NAME,35,"bold"))


timer = Label(text="TIMER", bg=YELLOW, fg=GREEN,font=(FONT_NAME,45,"bold"))
timer.grid(row=0, column=1)

start_buttton = Button(text="START",bg=GREEN,command=start_timer)
start_buttton.grid(row=2, column=0)

reset_button = Button(text="RESET",bg=GREEN,command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label()
check_marks.grid(row=3 ,column=1)

window.mainloop()