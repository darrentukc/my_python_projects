from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # main window
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # text field
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='hello world',
            font=('Ariel', 15, 'italic'),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # score label field
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # button fields
        self.check_img = PhotoImage(file='images/true.png')
        self.check_button = Button(image=self.check_img, highlightthickness=0, command=self.tick_reply)
        self.check_button.grid(row=2, column=0)
        self.cross_img = PhotoImage(file='images/false.png')
        self.cross_button = Button(image=self.cross_img, highlightthickness=0, command=self.cross_reply)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz. Your score is {self.quiz.score} out of 10")
            self.cross_button.config(state='disabled')
            self.check_button.config(state='disabled')



    def tick_reply(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def cross_reply(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(1000, func=self.get_next_question)


