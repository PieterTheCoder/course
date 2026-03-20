from data import question_data
from question_model import Question
from quiz_brain import QuestBrain

question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    the_question = Question(q_text, q_answer)
    question_bank.append(the_question)

quiz = QuestBrain(question_bank)
while quiz.still_next_question():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.questions_number}")