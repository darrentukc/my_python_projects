from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q = Question(question['question'], question['correct_answer'])
    question_bank.append(new_q)

quizbrain = QuizBrain(question_bank)

print('\n' * 80)
quizbrain.next_question()

while quizbrain.still_has_questions():
    quizbrain.next_question()

print('\n' * 80)
print('Game Over!')
print(f'Your score is {quizbrain.score}/{quizbrain.question_number}')