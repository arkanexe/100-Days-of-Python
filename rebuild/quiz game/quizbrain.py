OPTION = ["A", "B", "C", "D"]

class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question = self.question_list[self.question_number]

        self.question_number += 1

        self.answer = input(f"{self.question.text} \n options: {self.question.choices}: ")
        self.change_ops()
        self.check_answer(self.answer)
        print(f"score: {self.score}")

    def check_answer(self, answer):
        if answer == self.question.answer:
            self.score += 1

    def change_ops(self):
        for option in range(len(self.question.choices)):
            if self.question.answer == self.question.choices[option]:
                self.question.answer = OPTION[option]
