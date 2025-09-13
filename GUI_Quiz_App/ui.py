from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
from tkinter import *
from data import question_data

class QuizInterface:
    def __init__(self,quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0",bg=THEME_COLOR,fg="White",font=("Arial",15,"bold"))
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0,background="White")
        self.question_text = self.canvas.create_text(150,125,
                                                     width=280,
                                                     text="Question",font=("Arial",15,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=40)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text,text=f"You have reached the end of the quiz.\nYour'e final score is {self.quiz.score}👍")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green")

        else:
            self.canvas.config(bg="Red")
        self.window.after(2000,self.get_next_question)
