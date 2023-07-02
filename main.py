from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    formatted = item["question"].replace("&quot;", "'")
    next_question = Question(formatted, item["correct_answer"])
    question_bank.append(next_question)


quiz = QuizBrain(question_bank)


print("""
████████╗██████╗░██╗██╗░░░██╗██╗░█████╗░  ████████╗██╗███╗░░░███╗███████╗
╚══██╔══╝██╔══██╗██║██║░░░██║██║██╔══██╗  ╚══██╔══╝██║████╗░████║██╔════╝
░░░██║░░░██████╔╝██║╚██╗░██╔╝██║███████║  ░░░██║░░░██║██╔████╔██║█████╗░░
░░░██║░░░██╔══██╗██║░╚████╔╝░██║██╔══██║  ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░
░░░██║░░░██║░░██║██║░░╚██╔╝░░██║██║░░██║  ░░░██║░░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝
""")


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/ {len(question_bank)}")
