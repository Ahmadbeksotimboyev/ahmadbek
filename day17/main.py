# class User:

#     def __init__(self, user_id, username):
#         # print("new user being created...")
#         self.id = user_id 
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1 
#         self.following += 1


# user_1 = User("001", "Ahmadbek")

# user_2 = User("002", "Sanjar")

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
