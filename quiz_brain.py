class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list  # will input question_bank so the question bank will be under this attribute
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False
