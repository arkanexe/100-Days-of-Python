from data import question_data
from question_model import Question


question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])

    question_bank.append(new_question)

print(question_bank)

from data import question_data
from quiz_brain import QuizBrain
from question_model import Question


question_bank = []

data = question_data

for question in question_data:

    question_text = question['text']
    question_answer = question['answer']

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
still_has_question = quiz.still_has_question()

while quiz.still_has_question():
    quiz.next_question()
question_number = 0
question_list = []
