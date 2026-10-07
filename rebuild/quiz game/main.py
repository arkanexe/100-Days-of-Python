from data import question_data
from question_model import Question
from quizbrain import QuizBrain, OPTION



question_bank = []

# dictionary, and add it to question_bank

for question in question_data:
    new_question = Question(question["question"], question["choices"], question["answer"] , question["category"])

    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

print(f"answer using {OPTION}")
while quiz_brain.still_has_questions():

    quiz_brain.next_question()

