# class User:

#     def __init__(self, username, id):
#         self.id = id
#         self.username = username
#         self.followers = 0
#         self.following = 0
    
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
        

# user1 = User(1, "Alice")
# user2 = User(2, "Bob")

# user1.follow(user2)

# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)

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

