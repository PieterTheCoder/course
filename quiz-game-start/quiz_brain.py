class QuestBrain:

    def __init__(self, q_list):
        self.questions_number = 0
        self.score = 0
        self.questions_list = q_list

    def still_next_question(self):
        return self.questions_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        self.questions_number += 1
        user_answer = input(f"Q.{self.questions_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.questions_number}")
        print("\n")