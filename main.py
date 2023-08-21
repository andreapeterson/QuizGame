from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import GUI
import html

question_bank = []
for item in question_data:
    question = item["question"]
    question_reformatted = html.unescape(question)
    next_question = Question(question_reformatted, item["correct_answer"])
    question_bank.append(next_question)


quiz = QuizBrain(question_bank)
quiz_ui = GUI(quiz)
