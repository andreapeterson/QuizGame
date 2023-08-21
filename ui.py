THEME_COLOR = "#5c90cc"
import tkinter as tk
from quiz_brain import QuizBrain


class GUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=270, text="hi", font=("Arial", 22, "italic"),
                                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.score_label = tk.Label(text="Score:0", bg=THEME_COLOR, highlightthickness=0, font=("Arial", 20, "italic"))
        self.score_label.grid(column=1, row=0)

        self.true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=self.true_image, command=self.pressed_true)
        self.true_button.grid(column=1, row=2)

        self.false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=self.false_image, command=self.pressed_false)
        self.false_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def pressed_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def pressed_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
